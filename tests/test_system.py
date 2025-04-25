"""
Test and Validation Module
This module tests and validates the AI-driven diagnostic system.
"""

import os
import sys
import json
import unittest
import random
from datetime import datetime

# Add parent directory to path to import main module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import ShiningStarDiagnosticSystem

class TestDiagnosticSystem(unittest.TestCase):
    """
    Test cases for the Shining Star Diagnostic System.
    """
    
    @classmethod
    def setUpClass(cls):
        """
        Set up test environment once before all tests.
        """
        # Create a test directory
        cls.test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_output")
        os.makedirs(cls.test_dir, exist_ok=True)
        
        # Initialize the diagnostic system with test directory
        cls.system = ShiningStarDiagnosticSystem(cls.test_dir)
        
        # Create test data
        cls.create_test_data()
    
    @classmethod
    def tearDownClass(cls):
        """
        Clean up after all tests.
        """
        # In a real test environment, we might delete test files here
        # For this implementation, we'll keep them for inspection
        pass
    
    @classmethod
    def create_test_data(cls):
        """
        Create test data for the test cases.
        """
        # Create test students
        cls.test_students = [
            {
                "id": "test_student_001",
                "name": "Alex Johnson",
                "age": 8,
                "grade": 3,
                "school": "Sunshine Elementary",
                "email": "alex.j@example.com"
            },
            {
                "id": "test_student_002",
                "name": "Taylor Smith",
                "age": 12,
                "grade": 7,
                "school": "Lincoln Middle School",
                "email": "taylor.s@example.com"
            },
            {
                "id": "test_student_003",
                "name": "Jordan Lee",
                "age": 16,
                "grade": 11,
                "school": "Washington High School",
                "email": "jordan.l@example.com"
            }
        ]
        
        # Create test parents
        cls.test_parents = [
            {
                "id": "test_parent_001",
                "name": "Sam Johnson",
                "email": "sam.j@example.com",
                "phone": "555-123-4567",
                "relationship": "Parent"
            },
            {
                "id": "test_parent_002",
                "name": "Casey Smith",
                "email": "casey.s@example.com",
                "phone": "555-234-5678",
                "relationship": "Parent"
            },
            {
                "id": "test_parent_003",
                "name": "Morgan Lee",
                "email": "morgan.l@example.com",
                "phone": "555-345-6789",
                "relationship": "Parent"
            }
        ]
        
        # Create test users
        cls.test_users = [
            {
                "username": "test_admin",
                "role": "admin",
                "password": "AdminPass123!",
                "email": "admin@test.com",
                "name": "Test Administrator"
            },
            {
                "username": "test_teacher",
                "role": "teacher",
                "password": "TeacherPass123!",
                "email": "teacher@test.com",
                "name": "Test Teacher"
            },
            {
                "username": "test_parent",
                "role": "parent",
                "password": "ParentPass123!",
                "email": "parent@test.com",
                "name": "Test Parent"
            }
        ]
    
    def generate_random_responses(self, questions):
        """
        Generate random responses for a set of questions.
        
        Args:
            questions (list): List of question dictionaries
            
        Returns:
            dict: Dictionary of question IDs and responses
        """
        responses = {}
        
        for question in questions:
            if question["type"] == "multiple_choice" or question["type"] == "situational":
                options = question.get("options", [])
                if options:
                    responses[question["id"]] = random.randint(0, len(options) - 1)
            elif question["type"] == "logic_puzzle":
                # For logic puzzles, select the correct answer 70% of the time
                if random.random() < 0.7:
                    correct_index = question["options"].index(question["correct_answer"])
                    responses[question["id"]] = correct_index
                else:
                    responses[question["id"]] = random.randint(0, len(question["options"]) - 1)
            elif question["type"] == "open_ended":
                # Skip open-ended questions in the test
                pass
        
        return responses
    
    def test_01_system_initialization(self):
        """
        Test that the system initializes correctly.
        """
        self.assertIsNotNone(self.system)
        self.assertIsNotNone(self.system.analyzer)
        self.assertIsNotNone(self.system.pathway_mapper)
        self.assertIsNotNone(self.system.career_advisor)
        self.assertIsNotNone(self.system.course_recommender)
        self.assertIsNotNone(self.system.report_generator)
        self.assertIsNotNone(self.system.report_delivery)
        self.assertIsNotNone(self.system.security_manager)
        self.assertIsNotNone(self.system.access_control)
    
    def test_02_user_creation(self):
        """
        Test user account creation.
        """
        # Create admin user first
        admin_result = self.system.create_user_account(
            "system",
            self.test_users[0]["username"],
            self.test_users[0]["role"],
            self.test_users[0]["password"],
            self.test_users[0]["email"],
            self.test_users[0]["name"]
        )
        
        self.assertEqual(admin_result["status"], "success")
        
        # Use admin to create other users
        for user in self.test_users[1:]:
            result = self.system.create_user_account(
                self.test_users[0]["username"],
                user["username"],
                user["role"],
                user["password"],
                user["email"],
                user["name"]
            )
            
            self.assertEqual(result["status"], "success")
    
    def test_03_user_authentication(self):
        """
        Test user authentication.
        """
        for user in self.test_users:
            result = self.system.authenticate_user(
                user["username"],
                user["password"]
            )
            
            self.assertEqual(result["status"], "success")
            self.assertEqual(result["user"]["username"], user["username"])
            self.assertEqual(result["user"]["role"], user["role"])
            self.assertIn("token", result)
    
    def test_04_questionnaire_retrieval(self):
        """
        Test questionnaire retrieval for different age groups.
        """
        # Test elementary school questionnaire
        elementary_questions = self.system.get_questionnaire_for_student(8)
        self.assertIsNotNone(elementary_questions)
        self.assertGreater(len(elementary_questions), 0)
        
        # Test middle school questionnaire
        middle_questions = self.system.get_questionnaire_for_student(12)
        self.assertIsNotNone(middle_questions)
        self.assertGreater(len(middle_questions), 0)
        
        # Test high school questionnaire
        high_questions = self.system.get_questionnaire_for_student(16)
        self.assertIsNotNone(high_questions)
        self.assertGreater(len(high_questions), 0)
        
        # Test parent questionnaire
        parent_questions = self.system.get_questionnaire_for_parent()
        self.assertIsNotNone(parent_questions)
        self.assertGreater(len(parent_questions), 0)
    
    def test_05_assessment_processing(self):
        """
        Test complete assessment processing.
        """
        for i, student in enumerate(self.test_students):
            # Get questions for this student's age
            student_questions = self.system.get_questionnaire_for_student(student["age"])
            parent_questions = self.system.get_questionnaire_for_parent()
            
            # Generate random responses
            student_responses = self.generate_random_responses(student_questions)
            parent_responses = self.generate_random_responses(parent_questions)
            
            # Process the assessment
            result = self.system.process_student_assessment(
                student,
                student_responses,
                self.test_parents[i],
                parent_responses
            )
            
            self.assertEqual(result["status"], "success")
            self.assertEqual(result["student_id"], student["id"])
            self.assertIn("results_file", result)
            self.assertTrue(os.path.exists(result["results_file"]))
            
            # Check if delivery results are included
            self.assertIn("delivery_results", result)
            if result["delivery_results"]:
                self.assertIn("student_report", result["delivery_results"])
                self.assertIn("parent_report", result["delivery_results"])
    
    def test_06_results_retrieval(self):
        """
        Test assessment results retrieval.
        """
        # Admin should be able to access all student results
        for student in self.test_students:
            result = self.system.retrieve_assessment_results(
                student["id"],
                self.test_users[0]["username"],
                self.test_users[0]["role"]
            )
            
            self.assertEqual(result["status"], "success")
            self.assertIn("results", result)
            self.assertEqual(result["results"]["student_info"]["id"], student["id"])
    
    def test_07_data_security(self):
        """
        Test data security features.
        """
        # Test data encryption
        test_data = {
            "student": {
                "id": "test_id",
                "name": "Test Student",
                "email": "test@example.com",
                "phone": "555-123-4567"
            },
            "parent": {
                "id": "parent_test_id",
                "name": "Test Parent",
                "email": "parent@example.com",
                "phone": "555-987-6543"
            }
        }
        
        # Encrypt the data
        encrypted_data = self.system.security_manager.encrypt_sensitive_data(test_data)
        
        # Check that sensitive fields are encrypted
        self.assertNotEqual(encrypted_data["student"]["email"], test_data["student"]["email"])
        self.assertNotEqual(encrypted_data["parent"]["email"], test_data["parent"]["email"])
        self.assertNotEqual(encrypted_data["parent"]["phone"], test_data["parent"]["phone"])
        
        # Decrypt the data
        decrypted_data = self.system.security_manager.decrypt_sensitive_data(encrypted_data)
        
        # Check that decrypted data matches original
        self.assertEqual(decrypted_data["student"]["email"], test_data["student"]["email"])
        self.assertEqual(decrypted_data["parent"]["email"], test_data["parent"]["email"])
        self.assertEqual(decrypted_data["parent"]["phone"], test_data["parent"]["phone"])
        
        # Test data anonymization
        anonymized_data = self.system.security_manager.anonymize_data_for_analytics(test_data)
        
        # Check that sensitive fields are anonymized
        self.assertNotEqual(anonymized_data["student"]["name"], test_data["student"]["name"])
        self.assertNotEqual(anonymized_data["student"]["email"], test_data["student"]["email"])
        self.assertNotIn("parent", anonymized_data)
    
    def test_08_access_control(self):
        """
        Test role-based access control.
        """
        # Admin should have all permissions
        admin_permissions = [
            "view_all_reports",
            "edit_all_reports",
            "delete_reports",
            "manage_users",
            "view_logs",
            "export_data"
        ]
        
        for permission in admin_permissions:
            has_permission = self.system.access_control.check_permission(
                self.test_users[0]["username"],
                permission
            )
            self.assertTrue(has_permission)
        
        # Teacher should have limited permissions
        teacher_permissions = {
            "view_all_reports": True,
            "edit_all_reports": False,
            "delete_reports": False,
            "manage_users": False,
            "view_logs": False,
            "export_data": True
        }
        
        for permission, expected in teacher_permissions.items():
            has_permission = self.system.access_control.check_permission(
                self.test_users[1]["username"],
                permission
            )
            self.assertEqual(has_permission, expected)
        
        # Parent should have minimal permissions
        parent_permissions = {
            "view_all_reports": False,
            "edit_all_reports": False,
            "delete_reports": False,
            "manage_users": False,
            "view_logs": False,
            "export_data": False
        }
        
        for permission, expected in parent_permissions.items():
            has_permission = self.system.access_control.check_permission(
                self.test_users[2]["username"],
                permission
            )
            self.assertEqual(has_permission, expected)


def run_tests():
    """
    Run all test cases.
    """
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


if __name__ == "__main__":
    run_tests()
