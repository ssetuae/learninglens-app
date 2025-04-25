"""
Minimal working Flask application for Render deployment
"""

from flask import Flask, render_template, jsonify

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'render-deployment-test-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
