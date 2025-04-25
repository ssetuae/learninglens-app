"""
Production application entry point for the LearningLens system.
This file is used by Gunicorn to serve the application in production.
"""

from web_app import app as application
from config import get_config

# Load configuration
config = get_config()

# Configure the application
application.config.from_object(config)

# Create necessary directories
import os
os.makedirs(application.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(application.config['REPORTS_FOLDER'], exist_ok=True)

# Initialize the database if it doesn't exist
from web_app import db, User
with application.app_context():
    db.create_all()
    
    # Create admin user if not exists
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            email=application.config['ADMIN_EMAIL'],
            role='admin'
        )
        admin.set_password('admin123')  # Default password, should be changed
        db.session.add(admin)
        db.session.commit()
        print('Admin user created.')

# This is used by Gunicorn
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
