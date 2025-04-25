"""
Models for LearningLens application using SQLite
"""
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from database import db

class Role(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    users = db.relationship('User', backref='role', lazy=True)
    
    def __repr__(self):
        return f'<Role {self.name}>'

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    @staticmethod
    def generate_password_hash(password):
        return generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(20), nullable=False)
    parent_email = db.Column(db.String(100))
    parent_phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    assessments = db.relationship('Assessment', backref='student', lazy=True)
    
    def __repr__(self):
        return f'<Student {self.first_name} {self.last_name}>'

class Assessment(db.Model):
    __tablename__ = 'assessments'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    assessment_date = db.Column(db.DateTime, default=datetime.utcnow)
    learning_style = db.Column(db.String(50))
    cognitive_strengths = db.Column(db.Text)
    behavior_patterns = db.Column(db.Text)
    interests = db.Column(db.Text)
    parent_responses = db.Column(db.Text)
    teacher_responses = db.Column(db.Text)
    recommendations = db.Column(db.Text)
    career_affinities = db.Column(db.Text)
    math_pathway = db.Column(db.Text)
    global_exams = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Assessment {self.id} for Student {self.student_id}>'

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50))
    age_range = db.Column(db.String(50))
    learning_styles = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<Course {self.name}>'

class Report(db.Model):
    __tablename__ = 'reports'
    
    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('assessments.id'), nullable=False)
    report_type = db.Column(db.String(20), nullable=False)  # student, parent, teacher
    generated_at = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)
    delivered = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Report {self.id} for Assessment {self.assessment_id}>'
