"""
SQLite database configuration for LearningLens application
"""
import os
import sqlite3
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database configuration
SQLITE_DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'learninglens.db')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLITE_DB_PATH}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Initialize SQLAlchemy
db = SQLAlchemy()

# Create engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db(app):
    """Initialize the database with the app context"""
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        # Initialize admin user if not exists
        from models import User, Role
        if not User.query.filter_by(username='admin').first():
            admin_role = Role(name='admin')
            db_session.add(admin_role)
            db_session.commit()
            
            admin_user = User(
                username='admin',
                email='admin@learninglens.com',
                password_hash=User.generate_password_hash('admin123'),
                role_id=admin_role.id,
                created_at=datetime.now()
            )
            db_session.add(admin_user)
            db_session.commit()

def get_db_connection():
    """Get a direct SQLite connection for raw queries"""
    conn = sqlite3.connect(SQLITE_DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
