from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sqlite3
import json
from datetime import datetime
import secrets

# Import application modules
from models import db, User, Student, Assessment, Report
from data.questionnaire import get_questionnaire_for_age_group
from data.analysis import analyze_responses
from data.report_generator import generate_student_report, generate_parent_report
from data.teacher_report import generate_teacher_report
from data.pathway_mapper import generate_learning_pathway
from data.career_advisor import suggest_careers
from data.course_recommender import recommend_courses
from data.global_exams import suggest_exams
from data.math_pathway import generate_math_pathway
from data.report_delivery import deliver_report
from data.security import encrypt_data, decrypt_data, log_activity

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'learninglens-development-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///learninglens.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ensure the instance folder exists
os.makedirs(os.path.join(app.instance_path), exist_ok=True)

# Initialize database
db.init_app(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()
    # Create admin user if not exists
    if not User.query.filter_by(username='admin').first():
        admin = User(
            username='admin',
            email='admin@shiningstaronline.com',
            password_hash=generate_password_hash('admin123'),
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()
        log_activity('system', 'admin_created', 'Created default admin user')

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
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            log_activity(user.username, 'login', 'User logged in')
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    log_activity(current_user.username, 'logout', 'User logged out')
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    elif current_user.role == 'teacher':
        return redirect(url_for('teacher_dashboard'))
    else:
        return redirect(url_for('user_dashboard'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('dashboard'))
    
    users = User.query.all()
    students = Student.query.all()
    assessments = Assessment.query.all()
    
    return render_template('admin/dashboard.html', 
                          users=users, 
                          students=students, 
                          assessments=assessments)

@app.route('/admin/users')
@login_required
def admin_users():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('dashboard'))
    
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@app.route('/admin/add_user', methods=['GET', 'POST'])
@login_required
def admin_add_user():
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('admin_add_user'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'danger')
            return redirect(url_for('admin_add_user'))
        
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            role=role
        )
        
        db.session.add(new_user)
        db.session.commit()
        log_activity(current_user.username, 'user_created', f'Created user: {username}')
        
        flash('User added successfully', 'success')
        return redirect(url_for('admin_users'))
    
    return render_template('admin/add_user.html')

@app.route('/admin/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def admin_edit_user(user_id):
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('dashboard'))
    
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        user.username = request.form.get('username')
        user.email = request.form.get('email')
        user.role = request.form.get('role')
        
        if request.form.get('password'):
            user.password_hash = generate_password_hash(request.form.get('password'))
        
        db.session.commit()
        log_activity(current_user.username, 'user_updated', f'Updated user: {user.username}')
        
        flash('User updated successfully', 'success')
        return redirect(url_for('admin_users'))
    
    return render_template('admin/edit_user.html', user=user)

@app.route('/admin/delete_user/<int:user_id>')
@login_required
def admin_delete_user(user_id):
    if current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('dashboard'))
    
    user = User.query.get_or_404(user_id)
    
    if user.username == 'admin':
        flash('Cannot delete admin user', 'danger')
        return redirect(url_for('admin_users'))
    
    db.session.delete(user)
    db.session.commit()
    log_activity(current_user.username, 'user_deleted', f'Deleted user: {user.username}')
    
    flash('User deleted successfully', 'success')
    return redirect(url_for('admin_users'))

@app.route('/assessment/<age_group>')
@login_required
def assessment(age_group):
    questionnaire = get_questionnaire_for_age_group(age_group)
    return render_template('assessment.html', 
                          questionnaire=questionnaire, 
                          age_group=age_group)

@app.route('/submit_assessment', methods=['POST'])
@login_required
def submit_assessment():
    data = request.form.to_dict()
    age_group = data.pop('age_group')
    student_name = data.pop('student_name')
    student_age = data.pop('student_age')
    
    # Create or get student
    student = Student.query.filter_by(name=student_name, age=student_age).first()
    if not student:
        student = Student(
            name=student_name,
            age=student_age,
            parent_id=current_user.id
        )
        db.session.add(student)
        db.session.commit()
    
    # Create assessment
    assessment = Assessment(
        student_id=student.id,
        responses=json.dumps(data),
        age_group=age_group,
        created_by=current_user.id
    )
    db.session.add(assessment)
    db.session.commit()
    
    # Analyze responses
    analysis_results = analyze_responses(data, age_group)
    
    # Generate reports
    student_report = generate_student_report(student, analysis_results)
    parent_report = generate_parent_report(student, analysis_results)
    teacher_report = generate_teacher_report(student, analysis_results)
    
    # Generate learning pathway
    learning_pathway = generate_learning_pathway(analysis_results)
    
    # Generate math pathway if applicable
    math_pathway = generate_math_pathway(analysis_results)
    
    # Suggest careers
    career_suggestions = suggest_careers(analysis_results, student_age)
    
    # Recommend courses
    course_recommendations = recommend_courses(analysis_results)
    
    # Suggest global exams
    exam_suggestions = suggest_exams(analysis_results, student_age)
    
    # Create report
    report = Report(
        assessment_id=assessment.id,
        student_report=json.dumps(student_report),
        parent_report=json.dumps(parent_report),
        teacher_report=json.dumps(teacher_report),
        learning_pathway=json.dumps(learning_pathway),
        math_pathway=json.dumps(math_pathway),
        career_suggestions=json.dumps(career_suggestions),
        course_recommendations=json.dumps(course_recommendations),
        exam_suggestions=json.dumps(exam_suggestions)
    )
    db.session.add(report)
    db.session.commit()
    
    log_activity(current_user.username, 'assessment_submitted', f'Assessment submitted for student: {student_name}')
    
    # Deliver report if requested
    if 'deliver_email' in data:
        deliver_report(report, 'email', data.get('email'))
    
    if 'deliver_whatsapp' in data:
        deliver_report(report, 'whatsapp', data.get('phone'))
    
    flash('Assessment submitted successfully', 'success')
    return redirect(url_for('view_report', report_id=report.id))

@app.route('/view_report/<int:report_id>')
@login_required
def view_report(report_id):
    report = Report.query.get_or_404(report_id)
    assessment = Assessment.query.get(report.assessment_id)
    student = Student.query.get(assessment.student_id)
    
    # Check permissions
    if current_user.role != 'admin' and current_user.id != student.parent_id:
        flash('Access denied', 'danger')
        return redirect(url_for('dashboard'))
    
    student_report = json.loads(report.student_report)
    parent_report = json.loads(report.parent_report)
    learning_pathway = json.loads(report.learning_pathway)
    career_suggestions = json.loads(report.career_suggestions)
    course_recommendations = json.loads(report.course_recommendations)
    
    return render_template('view_report.html',
                          student=student,
                          student_report=student_report,
                          parent_report=parent_report,
                          learning_pathway=learning_pathway,
                          career_suggestions=career_suggestions,
                          course_recommendations=course_recommendations)

@app.route('/teacher/view_report/<int:report_id>')
@login_required
def teacher_view_report(report_id):
    if current_user.role != 'teacher' and current_user.role != 'admin':
        flash('Access denied', 'danger')
        return redirect(url_for('dashboard'))
    
    report = Report.query.get_or_404(report_id)
    assessment = Assessment.query.get(report.assessment_id)
    student = Student.query.get(assessment.student_id)
    
    teacher_report = json.loads(report.teacher_report)
    
    return render_template('teacher/teacher_report.html',
                          student=student,
                          teacher_report=teacher_report)

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
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
