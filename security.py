"""
Security enhancements for the LearningLens production deployment
"""

import os
import secrets
from flask import Flask, request, abort
from flask_wtf.csrf import CSRFProtect
from werkzeug.middleware.proxy_fix import ProxyFix
import logging
from logging.handlers import RotatingFileHandler

def configure_security(app):
    """Configure security enhancements for the Flask application."""
    # Enable CSRF protection
    csrf = CSRFProtect(app)
    
    # Fix for proxy headers (important for Render)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
    
    # Set secure cookies in production
    if app.config['ENV'] == 'production':
        app.config['SESSION_COOKIE_SECURE'] = True
        app.config['REMEMBER_COOKIE_SECURE'] = True
        app.config['SESSION_COOKIE_HTTPONLY'] = True
        app.config['REMEMBER_COOKIE_HTTPONLY'] = True
        app.config['PREFERRED_URL_SCHEME'] = 'https'
    
    # Configure Content Security Policy
    @app.after_request
    def set_security_headers(response):
        response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://cdn.jsdelivr.net; style-src 'self' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; font-src 'self' https://cdnjs.cloudflare.com; img-src 'self' data:;"
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response
    
    # Rate limiting for sensitive endpoints
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address
    
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["200 per day", "50 per hour"],
        storage_uri="memory://",
    )
    
    # Apply stricter limits to authentication endpoints
    @app.route('/login', methods=['POST'])
    @limiter.limit("10 per minute")
    def login_rate_limited():
        # This is just for rate limiting, the actual route is defined elsewhere
        pass
    
    # Configure logging
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    file_handler = RotatingFileHandler('logs/learninglens.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    
    app.logger.setLevel(logging.INFO)
    app.logger.info('LearningLens startup')
    
    # Log all errors
    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(f'Unhandled exception: {str(e)}', exc_info=True)
        return "An unexpected error occurred", 500
    
    return app

def generate_env_file():
    """Generate a .env file with secure random values for production."""
    env_content = f"""# Production environment variables for LearningLens
FLASK_ENV=production
SECRET_KEY={secrets.token_hex(32)}
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/learninglens
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=noreply@shiningstar.edu
ADMIN_EMAIL=admin@shiningstar.edu
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("Generated .env file with secure random values")
