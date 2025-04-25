"""
Web Application Module for Shining Star Diagnostic System
This module implements the web interface and deployment components.
"""

import os
import json
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import secrets

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shining_star.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'

# Define database models
class User(UserMixin, db.Model):
    """User model for authentication and access control."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')  # 'admin', 'teacher', 'user'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    def set_password(self, password):
        """Set password hash."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check password against hash."""
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self):
        """Check if user has admin role."""
        return self.role == 'admin'
    
    def is_teacher(self):
        """Check if user has teacher role."""
        return self.role == 'teacher'

class Student(db.Model):
    """Student model for storing student information."""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    parent_email = db.Column(db.String(100))
    parent_phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    assessments = db.relationship('Assessment', backref='student', lazy=True)

class Assessment(db.Model):
    """Assessment model for storing assessment results."""
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'in_progress', 'completed'
    
    # Assessment data (stored as JSON)
    student_responses = db.Column(db.Text)  # JSON string
    parent_responses = db.Column(db.Text)  # JSON string
    teacher_responses = db.Column(db.Text)  # JSON string
    
    # Analysis results (stored as JSON)
    learning_styles = db.Column(db.Text)  # JSON string
    traits = db.Column(db.Text)  # JSON string
    interests = db.Column(db.Text)  # JSON string
    
    # Reports
    student_report_path = db.Column(db.String(255))
    parent_report_path = db.Column(db.String(255))
    teacher_report_path = db.Column(db.String(255))
    
    # Recommendations
    course_recommendations = db.Column(db.Text)  # JSON string
    math_pathway = db.Column(db.Text)  # JSON string
    exam_recommendations = db.Column(db.Text)  # JSON string

class ActivityLog(db.Model):
    """Activity log for audit trail."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    action = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text)
    ip_address = db.Column(db.String(45))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    user = db.relationship('User', backref='activities')

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    """Home page route."""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login route."""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = 'remember' in request.form
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user, remember=remember)
            user.last_login = datetime.utcnow()
            db.session.commit()
            
            # Log activity
            log_activity(user.id, 'login', 'User logged in', request.remote_addr)
            
            next_page = request.args.get('next')
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('dashboard')
            return redirect(next_page)
        
        flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """Logout route."""
    # Log activity
    log_activity(current_user.id, 'logout', 'User logged out', request.remote_addr)
    
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    """Dashboard route."""
    if current_user.is_admin():
        return redirect(url_for('admin_dashboard'))
    elif current_user.is_teacher():
        return redirect(url_for('teacher_dashboard'))
    else:
        return redirect(url_for('user_dashboard'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """Admin dashboard route."""
    if not current_user.is_admin():
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    users = User.query.all()
    students = Student.query.all()
    assessments = Assessment.query.all()
    
    recent_activities = ActivityLog.query.order_by(ActivityLog.timestamp.desc()).limit(10).all()
    
    return render_template('admin/dashboard.html', 
                          users=users, 
                          students=students, 
                          assessments=assessments,
                          recent_activities=recent_activities)

@app.route('/teacher/dashboard')
@login_required
def teacher_dashboard():
    """Teacher dashboard route."""
    if not current_user.is_teacher() and not current_user.is_admin():
        flash('Access denied. Teacher privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    students = Student.query.all()
    assessments = Assessment.query.all()
    
    return render_template('teacher/dashboard.html', 
                          students=students, 
                          assessments=assessments)

@app.route('/user/dashboard')
@login_required
def user_dashboard():
    """User dashboard route."""
    return render_template('user/dashboard.html')

@app.route('/admin/users')
@login_required
def admin_users():
    """Admin users management route."""
    if not current_user.is_admin():
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@app.route('/admin/users/add', methods=['GET', 'POST'])
@login_required
def admin_add_user():
    """Admin add user route."""
    if not current_user.is_admin():
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role')
        
        # Check if username or email already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return render_template('admin/add_user.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'danger')
            return render_template('admin/add_user.html')
        
        # Create new user
        user = User(username=username, email=email, role=role)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        # Log activity
        log_activity(current_user.id, 'add_user', f'Added user: {username}', request.remote_addr)
        
        flash('User added successfully', 'success')
        return redirect(url_for('admin_users'))
    
    return render_template('admin/add_user.html')

@app.route('/admin/users/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def admin_edit_user(user_id):
    """Admin edit user route."""
    if not current_user.is_admin():
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        role = request.form.get('role')
        password = request.form.get('password')
        
        # Check if username already exists (for another user)
        existing_user = User.query.filter_by(username=username).first()
        if existing_user and existing_user.id != user_id:
            flash('Username already exists', 'danger')
            return render_template('admin/edit_user.html', user=user)
        
        # Check if email already exists (for another user)
        existing_user = User.query.filter_by(email=email).first()
        if existing_user and existing_user.id != user_id:
            flash('Email already exists', 'danger')
            return render_template('admin/edit_user.html', user=user)
        
        # Update user
        user.username = username
        user.email = email
        user.role = role
        
        if password:
            user.set_password(password)
        
        db.session.commit()
        
        # Log activity
        log_activity(current_user.id, 'edit_user', f'Edited user: {username}', request.remote_addr)
        
        flash('User updated successfully', 'success')
        return redirect(url_for('admin_users'))
    
    return render_template('admin/edit_user.html', user=user)

@app.route('/admin/users/delete/<int:user_id>', methods=['POST'])
@login_required
def admin_delete_user(user_id):
    """Admin delete user route."""
    if not current_user.is_admin():
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    user = User.query.get_or_404(user_id)
    
    # Prevent self-deletion
    if user.id == current_user.id:
        flash('You cannot delete your own account', 'danger')
        return redirect(url_for('admin_users'))
    
    username = user.username
    
    db.session.delete(user)
    db.session.commit()
    
    # Log activity
    log_activity(current_user.id, 'delete_user', f'Deleted user: {username}', request.remote_addr)
    
    flash('User deleted successfully', 'success')
    return redirect(url_for('admin_users'))

@app.route('/admin/students')
@login_required
def admin_students():
    """Admin students management route."""
    if not current_user.is_admin() and not current_user.is_teacher():
        flash('Access denied. Admin or teacher privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    students = Student.query.all()
    return render_template('admin/students.html', students=students)

@app.route('/admin/students/add', methods=['GET', 'POST'])
@login_required
def admin_add_student():
    """Admin add student route."""
    if not current_user.is_admin() and not current_user.is_teacher():
        flash('Access denied. Admin or teacher privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        age = request.form.get('age')
        grade = request.form.get('grade')
        parent_email = request.form.get('parent_email')
        parent_phone = request.form.get('parent_phone')
        
        # Create new student
        student = Student(
            first_name=first_name,
            last_name=last_name,
            age=int(age),
            grade=int(grade),
            parent_email=parent_email,
            parent_phone=parent_phone
        )
        
        db.session.add(student)
        db.session.commit()
        
        # Log activity
        log_activity(current_user.id, 'add_student', f'Added student: {first_name} {last_name}', request.remote_addr)
        
        flash('Student added successfully', 'success')
        return redirect(url_for('admin_students'))
    
    return render_template('admin/add_student.html')

@app.route('/admin/students/edit/<int:student_id>', methods=['GET', 'POST'])
@login_required
def admin_edit_student(student_id):
    """Admin edit student route."""
    if not current_user.is_admin() and not current_user.is_teacher():
        flash('Access denied. Admin or teacher privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    student = Student.query.get_or_404(student_id)
    
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        age = request.form.get('age')
        grade = request.form.get('grade')
        parent_email = request.form.get('parent_email')
        parent_phone = request.form.get('parent_phone')
        
        # Update student
        student.first_name = first_name
        student.last_name = last_name
        student.age = int(age)
        student.grade = int(grade)
        student.parent_email = parent_email
        student.parent_phone = parent_phone
        
        db.session.commit()
        
        # Log activity
        log_activity(current_user.id, 'edit_student', f'Edited student: {first_name} {last_name}', request.remote_addr)
        
        flash('Student updated successfully', 'success')
        return redirect(url_for('admin_students'))
    
    return render_template('admin/edit_student.html', student=student)

@app.route('/admin/students/delete/<int:student_id>', methods=['POST'])
@login_required
def admin_delete_student(student_id):
    """Admin delete student route."""
    if not current_user.is_admin():
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    student = Student.query.get_or_404(student_id)
    name = f"{student.first_name} {student.last_name}"
    
    db.session.delete(student)
    db.session.commit()
    
    # Log activity
    log_activity(current_user.id, 'delete_student', f'Deleted student: {name}', request.remote_addr)
    
    flash('Student deleted successfully', 'success')
    return redirect(url_for('admin_students'))

@app.route('/admin/assessments')
@login_required
def admin_assessments():
    """Admin assessments management route."""
    if not current_user.is_admin() and not current_user.is_teacher():
        flash('Access denied. Admin or teacher privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    assessments = Assessment.query.all()
    return render_template('admin/assessments.html', assessments=assessments)

@app.route('/admin/assessments/create/<int:student_id>', methods=['GET', 'POST'])
@login_required
def admin_create_assessment(student_id):
    """Admin create assessment route."""
    if not current_user.is_admin() and not current_user.is_teacher():
        flash('Access denied. Admin or teacher privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    student = Student.query.get_or_404(student_id)
    
    if request.method == 'POST':
        # Create new assessment
        assessment = Assessment(student_id=student_id)
        
        db.session.add(assessment)
        db.session.commit()
        
        # Log activity
        log_activity(current_user.id, 'create_assessment', f'Created assessment for student: {student.first_name} {student.last_name}', request.remote_addr)
        
        flash('Assessment created successfully', 'success')
        return redirect(url_for('admin_assessments'))
    
    return render_template('admin/create_assessment.html', student=student)

@app.route('/admin/assessments/view/<int:assessment_id>')
@login_required
def admin_view_assessment(assessment_id):
    """Admin view assessment route."""
    if not current_user.is_admin() and not current_user.is_teacher():
        flash('Access denied. Admin or teacher privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    assessment = Assessment.query.get_or_404(assessment_id)
    student = Student.query.get(assessment.student_id)
    
    # Parse JSON data
    learning_styles = json.loads(assessment.learning_styles) if assessment.learning_styles else {}
    traits = json.loads(assessment.traits) if assessment.traits else {}
    interests = json.loads(assessment.interests) if assessment.interests else {}
    course_recommendations = json.loads(assessment.course_recommendations) if assessment.course_recommendations else {}
    math_pathway = json.loads(assessment.math_pathway) if assessment.math_pathway else {}
    exam_recommendations = json.loads(assessment.exam_recommendations) if assessment.exam_recommendations else {}
    
    return render_template('admin/view_assessment.html', 
                          assessment=assessment,
                          student=student,
                          learning_styles=learning_styles,
                          traits=traits,
                          interests=interests,
                          course_recommendations=course_recommendations,
                          math_pathway=math_pathway,
                          exam_recommendations=exam_recommendations)

@app.route('/admin/assessments/delete/<int:assessment_id>', methods=['POST'])
@login_required
def admin_delete_assessment(assessment_id):
    """Admin delete assessment route."""
    if not current_user.is_admin():
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    assessment = Assessment.query.get_or_404(assessment_id)
    student = Student.query.get(assessment.student_id)
    
    db.session.delete(assessment)
    db.session.commit()
    
    # Log activity
    log_activity(current_user.id, 'delete_assessment', f'Deleted assessment for student: {student.first_name} {student.last_name}', request.remote_addr)
    
    flash('Assessment deleted successfully', 'success')
    return redirect(url_for('admin_assessments'))

@app.route('/admin/logs')
@login_required
def admin_logs():
    """Admin activity logs route."""
    if not current_user.is_admin():
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('dashboard'))
    
    logs = ActivityLog.query.order_by(ActivityLog.timestamp.desc()).all()
    return render_template('admin/logs.html', logs=logs)

@app.route('/questionnaire/<int:assessment_id>')
@login_required
def questionnaire(assessment_id):
    """Questionnaire route."""
    assessment = Assessment.query.get_or_404(assessment_id)
    student = Student.query.get(assessment.student_id)
    
    # Check if user has permission to access this assessment
    if not current_user.is_admin() and not current_user.is_teacher():
        flash('Access denied.', 'danger')
        return redirect(url_for('dashboard'))
    
    # Update assessment status
    if assessment.status == 'pending':
        assessment.status = 'in_progress'
        db.session.commit()
    
    return render_template('questionnaire.html', assessment=assessment, student=student)

@app.route('/api/submit_questionnaire/<int:assessment_id>', methods=['POST'])
@login_required
def api_submit_questionnaire(assessment_id):
    """API endpoint for submitting questionnaire responses."""
    assessment = Assessment.query.get_or_404(assessment_id)
    
    # Check if user has permission to access this assessment
    if not current_user.is_admin() and not current_user.is_teacher():
        return jsonify({'success': False, 'message': 'Access denied.'}), 403
    
    # Get data from request
    data = request.json
    
    # Update assessment with responses
    if 'student_responses' in data:
        assessment.student_responses = json.dumps(data['student_responses'])
    
    if 'parent_responses' in data:
        assessment.parent_responses = json.dumps(data['parent_responses'])
    
    if 'teacher_responses' in data:
        assessment.teacher_responses = json.dumps(data['teacher_responses'])
    
    # Update status if all responses are submitted
    if (assessment.student_responses and 
        assessment.parent_responses and 
        assessment.teacher_responses):
        assessment.status = 'completed'
    
    db.session.commit()
    
    # Log activity
    log_activity(current_user.id, 'submit_questionnaire', f'Submitted questionnaire for assessment ID: {assessment_id}', request.remote_addr)
    
    return jsonify({'success': True, 'message': 'Questionnaire submitted successfully.'})

@app.route('/api/analyze_assessment/<int:assessment_id>', methods=['POST'])
@login_required
def api_analyze_assessment(assessment_id):
    """API endpoint for analyzing assessment responses."""
    assessment = Assessment.query.get_or_404(assessment_id)
    
    # Check if user has permission to access this assessment
    if not current_user.is_admin() and not current_user.is_teacher():
        return jsonify({'success': False, 'message': 'Access denied.'}), 403
    
    # Check if assessment is complete
    if assessment.status != 'completed':
        return jsonify({'success': False, 'message': 'Assessment is not complete.'}), 400
    
    # Get student info
    student = Student.query.get(assessment.student_id)
    student_info = {
        'id': student.id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'age': student.age,
        'grade': student.grade
    }
    
    # Parse responses
    student_responses = json.loads(assessment.student_responses) if assessment.student_responses else {}
    parent_responses = json.loads(assessment.parent_responses) if assessment.parent_responses else {}
    teacher_responses = json.loads(assessment.teacher_responses) if assessment.teacher_responses else {}
    
    # TODO: Implement actual analysis logic here
    # For now, we'll use placeholder data
    
    # Learning styles analysis
    learning_styles = {
        'primary': 'visual',
        'secondary': ['logical', 'kinesthetic'],
        'scores': {
            'visual': 85,
            'auditory': 60,
            'kinesthetic': 75,
            'logical': 80,
            'social': 65,
            'independent': 70
        }
    }
    
    # Traits analysis
    traits = {
        'top_traits': ['analytical', 'persistent', 'creative'],
        'scores': {
            'analytical': 90,
            'creative': 75,
            'persistent': 85,
            'leadership': 60,
            'collaborative': 65,
            'organized': 70
        }
    }
    
    # Interests analysis
    interests = {
        'top_interests': ['technology', 'mathematics', 'science'],
        'scores': {
            'technology': 90,
            'arts': 60,
            'entrepreneurship': 65,
            'science': 85,
            'language': 70,
            'mathematics': 95
        }
    }
    
    # Update assessment with analysis results
    assessment.learning_styles = json.dumps(learning_styles)
    assessment.traits = json.dumps(traits)
    assessment.interests = json.dumps(interests)
    
    # Generate course recommendations
    from data.course_recommender import CourseRecommender
    course_recommender = CourseRecommender()
    course_recommendations = course_recommender.recommend_courses(student_info, {
        'learning_styles': learning_styles,
        'traits': traits,
        'interests': interests
    })
    assessment.course_recommendations = json.dumps(course_recommendations)
    
    # Generate math pathway
    from data.math_pathway import MathematicsPathwayGenerator
    math_pathway_generator = MathematicsPathwayGenerator()
    math_pathway = math_pathway_generator.generate_math_pathway(student_info, {
        'learning_styles': learning_styles,
        'traits': traits,
        'interests': interests
    })
    assessment.math_pathway = json.dumps(math_pathway)
    
    # Generate exam recommendations
    from data.global_exams import GlobalExamRecommender
    exam_recommender = GlobalExamRecommender()
    exam_recommendations = exam_recommender.recommend_examinations(student_info, {
        'learning_styles': learning_styles,
        'traits': traits,
        'interests': interests
    })
    assessment.exam_recommendations = json.dumps(exam_recommendations)
    
    db.session.commit()
    
    # Log activity
    log_activity(current_user.id, 'analyze_assessment', f'Analyzed assessment ID: {assessment_id}', request.remote_addr)
    
    return jsonify({
        'success': True, 
        'message': 'Assessment analyzed successfully.',
        'learning_styles': learning_styles,
        'traits': traits,
        'interests': interests,
        'course_recommendations': course_recommendations,
        'math_pathway': math_pathway,
        'exam_recommendations': exam_recommendations
    })

@app.route('/api/generate_reports/<int:assessment_id>', methods=['POST'])
@login_required
def api_generate_reports(assessment_id):
    """API endpoint for generating reports."""
    assessment = Assessment.query.get_or_404(assessment_id)
    
    # Check if user has permission to access this assessment
    if not current_user.is_admin() and not current_user.is_teacher():
        return jsonify({'success': False, 'message': 'Access denied.'}), 403
    
    # Check if assessment has been analyzed
    if not assessment.learning_styles or not assessment.traits or not assessment.interests:
        return jsonify({'success': False, 'message': 'Assessment has not been analyzed.'}), 400
    
    # Get student info
    student = Student.query.get(assessment.student_id)
    student_info = {
        'id': student.id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'age': student.age,
        'grade': student.grade,
        'parent_email': student.parent_email,
        'parent_phone': student.parent_phone
    }
    
    # Parse analysis results
    learning_styles = json.loads(assessment.learning_styles)
    traits = json.loads(assessment.traits)
    interests = json.loads(assessment.interests)
    course_recommendations = json.loads(assessment.course_recommendations) if assessment.course_recommendations else {}
    math_pathway = json.loads(assessment.math_pathway) if assessment.math_pathway else {}
    exam_recommendations = json.loads(assessment.exam_recommendations) if assessment.exam_recommendations else {}
    
    analysis_results = {
        'learning_styles': learning_styles,
        'traits': traits,
        'interests': interests,
        'course_recommendations': course_recommendations,
        'math_pathway': math_pathway,
        'exam_recommendations': exam_recommendations
    }
    
    # Parse responses for parent comparison
    student_responses = json.loads(assessment.student_responses) if assessment.student_responses else {}
    parent_responses = json.loads(assessment.parent_responses) if assessment.parent_responses else {}
    
    # Generate parent comparison
    parent_comparison = {
        'alignment_areas': ['Learning style preferences', 'Interest in technology'],
        'difference_areas': ['Persistence level', 'Social interaction preferences']
    }
    
    # Generate reports
    reports_dir = os.path.join(app.root_path, 'reports', str(assessment.id))
    os.makedirs(reports_dir, exist_ok=True)
    
    # Student report
    from data.report_generator import ReportGenerator
    report_generator = ReportGenerator(os.path.join(app.root_path, 'templates'))
    
    student_report_path = report_generator.generate_student_report(
        student_info,
        analysis_results,
        reports_dir
    )
    assessment.student_report_path = student_report_path
    
    # Parent report
    parent_report_path = report_generator.generate_parent_report(
        student_info,
        analysis_results,
        parent_comparison,
        reports_dir
    )
    assessment.parent_report_path = parent_report_path
    
    # Teacher report
    from data.teacher_report import TeacherReportGenerator
    teacher_report_generator = TeacherReportGenerator(os.path.join(app.root_path, 'templates'))
    
    teacher_report_path = teacher_report_generator.generate_teacher_report(
        student_info,
        analysis_results,
        parent_comparison,
        reports_dir
    )
    assessment.teacher_report_path = teacher_report_path
    
    db.session.commit()
    
    # Log activity
    log_activity(current_user.id, 'generate_reports', f'Generated reports for assessment ID: {assessment_id}', request.remote_addr)
    
    return jsonify({
        'success': True, 
        'message': 'Reports generated successfully.',
        'student_report_path': student_report_path,
        'parent_report_path': parent_report_path,
        'teacher_report_path': teacher_report_path
    })

# Helper functions
def log_activity(user_id, action, details, ip_address):
    """Log user activity."""
    activity = ActivityLog(
        user_id=user_id,
        action=action,
        details=details,
        ip_address=ip_address
    )
    db.session.add(activity)
    db.session.commit()

# Create initial admin user if not exists
def create_admin_user():
    """Create initial admin user if not exists."""
    with app.app_context():
        # Create tables if not exist
        db.create_all()
        
        # Check if admin user exists
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@shiningstar.edu',
                role='admin'
            )
            admin.set_password('admin123')  # Default password, should be changed
            db.session.add(admin)
            db.session.commit()
            print('Admin user created.')

# Run the app
if __name__ == '__main__':
    create_admin_user()
    app.run(host='0.0.0.0', port=5000, debug=True)
