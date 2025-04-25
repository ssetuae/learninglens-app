from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')  # admin, teacher, user
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    students = db.relationship('Student', backref='parent', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    assessments = db.relationship('Assessment', backref='student', lazy=True)
    
    def __repr__(self):
        return f'<Student {self.name}>'

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    responses = db.Column(db.Text, nullable=False)  # JSON string of responses
    age_group = db.Column(db.String(20), nullable=False)  # elementary, middle, high
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    report = db.relationship('Report', backref='assessment', lazy=True, uselist=False)
    
    def __repr__(self):
        return f'<Assessment {self.id} for Student {self.student_id}>'

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessment.id'), nullable=False)
    student_report = db.Column(db.Text, nullable=False)  # JSON string
    parent_report = db.Column(db.Text, nullable=False)  # JSON string
    teacher_report = db.Column(db.Text, nullable=False)  # JSON string
    learning_pathway = db.Column(db.Text, nullable=False)  # JSON string
    math_pathway = db.Column(db.Text, nullable=True)  # JSON string
    career_suggestions = db.Column(db.Text, nullable=False)  # JSON string
    course_recommendations = db.Column(db.Text, nullable=False)  # JSON string
    exam_suggestions = db.Column(db.Text, nullable=False)  # JSON string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Report {self.id} for Assessment {self.assessment_id}>'

class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    action = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ActivityLog {self.id} by {self.username}>'
