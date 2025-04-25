"""
Data Security Module
This module implements security measures to protect sensitive student and parent information.
"""

import os
import json
import hashlib
import base64
import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import logging
from datetime import datetime

class DataSecurityManager:
    """
    Manages data security for the diagnostic program.
    """
    
    def __init__(self, data_dir):
        """
        Initialize the data security manager.
        
        Args:
            data_dir (str): Directory to store security-related data
        """
        self.data_dir = data_dir
        self.keys_dir = os.path.join(data_dir, "keys")
        self.logs_dir = os.path.join(data_dir, "logs")
        self.access_logs_file = os.path.join(self.logs_dir, "access_logs.json")
        
        # Create necessary directories
        os.makedirs(self.keys_dir, exist_ok=True)
        os.makedirs(self.logs_dir, exist_ok=True)
        
        # Initialize encryption key
        self.encryption_key = self._load_or_create_encryption_key()
        
        # Set up logging
        self._setup_logging()
    
    def encrypt_sensitive_data(self, data):
        """
        Encrypts sensitive data in the provided dictionary.
        
        Args:
            data (dict): Data containing sensitive information
            
        Returns:
            dict: Data with sensitive fields encrypted
        """
        # Create a copy of the data to avoid modifying the original
        secure_data = data.copy()
        
        # Encrypt sensitive fields in student information
        if "student" in secure_data:
            student = secure_data["student"].copy()
            if "email" in student:
                student["email"] = self._encrypt_value(student["email"])
            if "phone" in student:
                student["phone"] = self._encrypt_value(student["phone"])
            if "address" in student:
                student["address"] = self._encrypt_value(student["address"])
            secure_data["student"] = student
        
        # Encrypt sensitive fields in parent information
        if "parent" in secure_data:
            parent = secure_data["parent"].copy()
            if "email" in parent:
                parent["email"] = self._encrypt_value(parent["email"])
            if "phone" in parent:
                parent["phone"] = self._encrypt_value(parent["phone"])
            if "address" in parent:
                parent["address"] = self._encrypt_value(parent["address"])
            secure_data["parent"] = parent
        
        # Add security metadata
        secure_data["_security"] = {
            "encrypted": True,
            "timestamp": datetime.now().isoformat(),
            "version": "1.0"
        }
        
        return secure_data
    
    def decrypt_sensitive_data(self, secure_data):
        """
        Decrypts sensitive data in the provided dictionary.
        
        Args:
            secure_data (dict): Data with encrypted sensitive fields
            
        Returns:
            dict: Data with sensitive fields decrypted
        """
        # Check if data is encrypted
        if not secure_data.get("_security", {}).get("encrypted", False):
            return secure_data
        
        # Create a copy of the data to avoid modifying the original
        data = secure_data.copy()
        
        # Decrypt sensitive fields in student information
        if "student" in data:
            student = data["student"].copy()
            if "email" in student:
                student["email"] = self._decrypt_value(student["email"])
            if "phone" in student:
                student["phone"] = self._decrypt_value(student["phone"])
            if "address" in student:
                student["address"] = self._decrypt_value(student["address"])
            data["student"] = student
        
        # Decrypt sensitive fields in parent information
        if "parent" in data:
            parent = data["parent"].copy()
            if "email" in parent:
                parent["email"] = self._decrypt_value(parent["email"])
            if "phone" in parent:
                parent["phone"] = self._decrypt_value(parent["phone"])
            if "address" in parent:
                parent["address"] = self._decrypt_value(parent["address"])
            data["parent"] = parent
        
        # Remove security metadata
        if "_security" in data:
            del data["_security"]
        
        return data
    
    def anonymize_data_for_analytics(self, data):
        """
        Anonymizes data for analytics purposes.
        
        Args:
            data (dict): Original data with sensitive information
            
        Returns:
            dict: Anonymized data safe for analytics
        """
        # Create a copy of the data to avoid modifying the original
        anon_data = data.copy()
        
        # Generate a consistent but anonymous ID
        if "student" in anon_data and "id" in anon_data["student"]:
            original_id = anon_data["student"]["id"]
            anon_data["student"]["id"] = self._generate_anonymous_id(original_id)
        
        # Remove or anonymize sensitive fields in student information
        if "student" in anon_data:
            student = anon_data["student"].copy()
            if "name" in student:
                student["name"] = "Student_" + student.get("id", "Unknown")
            if "email" in student:
                student["email"] = "student@example.com"
            if "phone" in student:
                student["phone"] = "000-000-0000"
            if "address" in student:
                student["address"] = "Anonymous Location"
            # Keep age and grade for analytics
            anon_data["student"] = student
        
        # Remove parent information entirely
        if "parent" in anon_data:
            del anon_data["parent"]
        
        # Add anonymization metadata
        anon_data["_anonymized"] = {
            "timestamp": datetime.now().isoformat(),
            "version": "1.0"
        }
        
        return anon_data
    
    def log_data_access(self, user_id, data_type, action, record_id=None):
        """
        Logs data access for audit purposes.
        
        Args:
            user_id (str): ID of the user accessing the data
            data_type (str): Type of data being accessed (e.g., "student", "parent", "report")
            action (str): Action being performed (e.g., "view", "edit", "delete")
            record_id (str, optional): ID of the specific record being accessed
            
        Returns:
            bool: Success status
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_id": user_id,
            "data_type": data_type,
            "action": action,
            "record_id": record_id,
            "ip_address": "127.0.0.1"  # In a real system, this would be the actual IP
        }
        
        # Load existing logs
        logs = []
        if os.path.exists(self.access_logs_file):
            try:
                with open(self.access_logs_file, 'r') as f:
                    logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
        
        # Add new log entry
        logs.append(log_entry)
        
        # Save updated logs
        try:
            with open(self.access_logs_file, 'w') as f:
                json.dump(logs, f, indent=2)
            return True
        except Exception as e:
            logging.error(f"Failed to log data access: {e}")
            return False
    
    def generate_access_token(self, user_id, role, expiry_hours=24):
        """
        Generates a secure access token for API access.
        
        Args:
            user_id (str): ID of the user
            role (str): Role of the user (e.g., "admin", "teacher", "parent")
            expiry_hours (int): Token validity in hours
            
        Returns:
            str: Access token
        """
        # Generate a random token
        token = secrets.token_hex(16)
        
        # Create token data
        token_data = {
            "user_id": user_id,
            "role": role,
            "created": datetime.now().isoformat(),
            "expires": (datetime.now() + datetime.timedelta(hours=expiry_hours)).isoformat(),
            "token": token
        }
        
        # Save token data
        token_file = os.path.join(self.keys_dir, f"token_{token}.json")
        with open(token_file, 'w') as f:
            json.dump(token_data, f, indent=2)
        
        return token
    
    def validate_access_token(self, token):
        """
        Validates an access token.
        
        Args:
            token (str): Access token to validate
            
        Returns:
            dict: Token data if valid, None otherwise
        """
        # Check if token file exists
        token_file = os.path.join(self.keys_dir, f"token_{token}.json")
        if not os.path.exists(token_file):
            return None
        
        # Load token data
        with open(token_file, 'r') as f:
            token_data = json.load(f)
        
        # Check if token has expired
        expires = datetime.fromisoformat(token_data["expires"])
        if datetime.now() > expires:
            # Token has expired, delete it
            os.remove(token_file)
            return None
        
        return token_data
    
    def _load_or_create_encryption_key(self):
        """
        Loads the encryption key or creates a new one if it doesn't exist.
        
        Returns:
            bytes: Encryption key
        """
        key_file = os.path.join(self.keys_dir, "encryption_key.key")
        
        if os.path.exists(key_file):
            # Load existing key
            with open(key_file, 'rb') as f:
                key = f.read()
        else:
            # Generate a new key
            key = Fernet.generate_key()
            
            # Save the key
            with open(key_file, 'wb') as f:
                f.write(key)
        
        return key
    
    def _encrypt_value(self, value):
        """
        Encrypts a single value.
        
        Args:
            value (str): Value to encrypt
            
        Returns:
            str: Encrypted value (base64 encoded)
        """
        if not value:
            return value
        
        # Create a Fernet cipher with the encryption key
        cipher = Fernet(self.encryption_key)
        
        # Encrypt the value
        encrypted_value = cipher.encrypt(value.encode())
        
        # Return base64 encoded encrypted value
        return base64.b64encode(encrypted_value).decode()
    
    def _decrypt_value(self, encrypted_value):
        """
        Decrypts a single value.
        
        Args:
            encrypted_value (str): Encrypted value (base64 encoded)
            
        Returns:
            str: Decrypted value
        """
        if not encrypted_value:
            return encrypted_value
        
        try:
            # Create a Fernet cipher with the encryption key
            cipher = Fernet(self.encryption_key)
            
            # Decode base64 and decrypt the value
            decrypted_value = cipher.decrypt(base64.b64decode(encrypted_value))
            
            # Return decoded value
            return decrypted_value.decode()
        except Exception as e:
            logging.error(f"Failed to decrypt value: {e}")
            return "[DECRYPTION_ERROR]"
    
    def _generate_anonymous_id(self, original_id):
        """
        Generates a consistent anonymous ID from an original ID.
        
        Args:
            original_id (str): Original ID
            
        Returns:
            str: Anonymous ID
        """
        # Create a hash of the original ID with a salt
        salt = "shining_star_salt"  # In a real system, this would be a secure, stored salt
        hash_input = (original_id + salt).encode()
        hash_output = hashlib.sha256(hash_input).hexdigest()
        
        # Return a portion of the hash as the anonymous ID
        return "anon_" + hash_output[:10]
    
    def _setup_logging(self):
        """
        Sets up logging for security events.
        """
        log_file = os.path.join(self.logs_dir, "security.log")
        
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )


class UserAccessControl:
    """
    Manages user access control for the diagnostic program.
    """
    
    def __init__(self, data_dir):
        """
        Initialize the user access control.
        
        Args:
            data_dir (str): Directory to store user access data
        """
        self.data_dir = data_dir
        self.users_dir = os.path.join(data_dir, "users")
        
        # Create necessary directories
        os.makedirs(self.users_dir, exist_ok=True)
        
        # Define role permissions
        self.role_permissions = {
            "admin": {
                "view_all_reports": True,
                "edit_all_reports": True,
                "delete_reports": True,
                "manage_users": True,
                "view_logs": True,
                "export_data": True
            },
            "teacher": {
                "view_all_reports": True,
                "edit_all_reports": False,
                "delete_reports": False,
                "manage_users": False,
                "view_logs": False,
                "export_data": True
            },
            "parent": {
                "view_all_reports": False,
                "edit_all_reports": False,
                "delete_reports": False,
                "manage_users": False,
                "view_logs": False,
                "export_data": False
            }
        }
    
    def create_user(self, username, role, password, email=None, name=None):
        """
        Creates a new user.
        
        Args:
            username (str): Username
            role (str): User role (admin, teacher, parent)
            password (str): User password
            email (str, optional): User email
            name (str, optional): User name
            
        Returns:
            dict: User data
        """
        # Check if username already exists
        user_file = os.path.join(self.users_dir, f"{username}.json")
        if os.path.exists(user_file):
            raise ValueError(f"Username '{username}' already exists")
        
        # Check if role is valid
        if role not in self.role_permissions:
            raise ValueError(f"Invalid role: {role}")
        
        # Hash the password
        password_hash = self._hash_password(password)
        
        # Create user data
        user_data = {
            "username": username,
            "role": role,
            "password_hash": password_hash,
            "email": email,
            "name": name,
            "created": datetime.now().isoformat(),
            "last_login": None,
            "active": True
        }
        
        # Save user data
        with open(user_file, 'w') as f:
            json.dump(user_data, f, indent=2)
        
        # Return user data without password hash
        user_data_safe = user_data.copy()
        del user_data_safe["password_hash"]
        return user_data_safe
    
    def authenticate_user(self, username, password):
        """
        Authenticates a user.
        
        Args:
            username (str): Username
            password (str): Password
            
        Returns:
            dict: User data if authentication successful, None otherwise
        """
        # Check if user exists
        user_file = os.path.join(self.users_dir, f"{username}.json")
        if not os.path.exists(user_file):
            return None
        
        # Load user data
        with open(user_file, 'r') as f:
            user_data = json.load(f)
        
        # Check if user is active
        if not user_data.get("active", True):
            return None
        
        # Verify password
        if not self._verify_password(password, user_data["password_hash"]):
            return None
        
        # Update last login time
        user_data["last_login"] = datetime.now().isoformat()
        with open(user_file, 'w') as f:
            json.dump(user_data, f, indent=2)
        
        # Return user data without password hash
        user_data_safe = user_data.copy()
        del user_data_safe["password_hash"]
        return user_data_safe
    
    def check_permission(self, username, permission):
        """
        Checks if a user has a specific permission.
        
        Args:
            username (str): Username
            permission (str): Permission to check
            
        Returns:
            bool: True if user has permission, False otherwise
        """
        # Check if user exists
        user_file = os.path.join(self.users_dir, f"{username}.json")
        if not os.path.exists(user_file):
            return False
        
        # Load user data
        with open(user_file, 'r') as f:
            user_data = json.load(f)
        
        # Check if user is active
        if not user_data.get("active", True):
            return False
        
        # Get user role
        role = user_data.get("role")
        
        # Check if role has permission
        if role in self.role_permissions:
            return self.role_permissions[role].get(permission, False)
        
        return False
    
    def get_user_specific_data_access(self, username):
        """
        Gets the specific data a user can access.
        
        Args:
            username (str): Username
            
        Returns:
            dict: Data access information
        """
        # Check if user exists
        user_file = os.path.join(self.users_dir, f"{username}.json")
        if not os.path.exists(user_file):
            return {}
        
        # Load user data
        with open(user_file, 'r') as f:
            user_data = json.load(f)
        
        # Check if user is active
        if not user_data.get("active", True):
            return {}
        
        # Get user role
        role = user_data.get("role")
        
        # Define data access based on role
        if role == "admin":
            # Admins can access all data
            return {"all_access": True}
        elif role == "teacher":
            # Teachers can access data for their assigned students
            return {
                "all_access": False,
                "student_ids": user_data.get("assigned_students", [])
            }
        elif role == "parent":
            # Parents can only access data for their children
            return {
                "all_access": False,
                "student_ids": user_data.get("children", [])
            }
        
        return {}
    
    def _hash_password(self, password):
        """
        Hashes a password.
        
        Args:
            password (str): Password to hash
            
        Returns:
            str: Password hash
        """
        # Generate a random salt
        salt = os.urandom(16)
        
        # Hash the password with the salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        key = kdf.derive(password.encode())
        
        # Combine salt and key for storage
        password_hash = {
            "salt": base64.b64encode(salt).decode(),
            "key": base64.b64encode(key).decode(),
            "iterations": 100000
        }
        
        return password_hash
    
    def _verify_password(self, password, password_hash):
        """
        Verifies a password against a hash.
        
        Args:
            password (str): Password to verify
            password_hash (dict): Password hash data
            
        Returns:
            bool: True if password is correct, False otherwise
        """
        # Extract salt and iterations from hash data
        salt = base64.b64decode(password_hash["salt"])
        iterations = password_hash["iterations"]
        stored_key = base64.b64decode(password_hash["key"])
        
        # Hash the provided password with the same salt and iterations
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=iterations
        )
        
        try:
            # Verify the password
            kdf.verify(password.encode(), stored_key)
            return True
        except Exception:
            return False
