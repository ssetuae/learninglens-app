"""
Main application file for LearningLens with SQLite database
"""
import os
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from datetime import datetime

from database import init_db, db_session
from models import User, Role, Student, Assessment, Course, Report

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'learninglens_default_secret_key')

# Initialize database
init_db(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            user.last_login = datetime.utcnow()
            db_session.commit()
            
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin_dashboard'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    students_count = Student.query.count()
    assessments_count = Assessment.query.count()
    reports_count = Report.query.count()
    
    return render_template('admin/dashboard.html', 
                          students_count=students_count,
                          assessments_count=assessments_count,
                          reports_count=reports_count)

@app.route('/admin/students')
@login_required
def admin_students():
    students = Student.query.all()
    return render_template('admin/students.html', students=students)

@app.route('/admin/assessments')
@login_required
def admin_assessments():
    assessments = Assessment.query.all()
    return render_template('admin/assessments.html', assessments=assessments)

@app.route('/admin/reports')
@login_required
def admin_reports():
    reports = Report.query.all()
    return render_template('admin/reports.html', reports=reports)

@app.route('/admin/users')
@login_required
def admin_users():
    if current_user.role.name != 'admin':
        flash('Access denied')
        return redirect(url_for('admin_dashboard'))
    
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@app.route('/api/health')
def health_check():
    return jsonify({"status": "healthy", "timestamp": datetime.utcnow().isoformat()})

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
