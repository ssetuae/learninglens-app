"""
Shining Star Education Training LLC - AI-Driven Diagnostic Program
Main application that integrates all components of the diagnostic system.
"""

import os
import json
import argparse
from datetime import datetime
import logging

# Import all components
from data.questionnaire import get_questions_for_age, get_parent_questions
from data.analysis import LearningStyleAnalyzer, generate_learning_badges
from data.pathway_mapper import LearningPathwayMapper
from data.career_advisor import CareerAffinityAdvisor
from data.course_recommender import CourseRecommender
from data.report_generator import ReportGenerator
from data.report_delivery import ReportDeliveryManager
from data.security import DataSecurityManager, UserAccessControl

class ShiningStarDiagnosticSystem:
    """
    Main class that integrates all components of the diagnostic system.
    """
    
    def __init__(self, base_dir=None):
        """
        Initialize the diagnostic system.
        
        Args:
            base_dir (str, optional): Base directory for the application
        """
        # Set up directories
        self.base_dir = base_dir or os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(self.base_dir, "data")
        self.templates_dir = os.path.join(self.base_dir, "templates")
        self.output_dir = os.path.join(self.base_dir, "output")
        self.static_dir = os.path.join(self.base_dir, "static")
        
        # Create directories if they don't exist
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "reports"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "data"), exist_ok=True)
        
        # Set up logging
        self._setup_logging()
        
        # Initialize components
        self.analyzer = LearningStyleAnalyzer()
        self.pathway_mapper = LearningPathwayMapper()
        self.career_advisor = CareerAffinityAdvisor()
        self.course_recommender = CourseRecommender()
        self.report_generator = ReportGenerator(self.templates_dir)
        self.report_delivery = ReportDeliveryManager(
            os.path.join(self.output_dir, "reports"),
            self.templates_dir
        )
        self.security_manager = DataSecurityManager(os.path.join(self.output_dir, "security"))
        self.access_control = UserAccessControl(os.path.join(self.output_dir, "security"))
        
        logging.info("Shining Star Diagnostic System initialized")
    
    def process_student_assessment(self, student_info, student_responses, parent_info=None, parent_responses=None):
        """
        Processes a complete student assessment.
        
        Args:
            student_info (dict): Student information
            student_responses (dict): Student's questionnaire responses
            parent_info (dict, optional): Parent information
            parent_responses (dict, optional): Parent's questionnaire responses
            
        Returns:
            dict: Processing results including report paths
        """
        try:
            logging.info(f"Processing assessment for student ID: {student_info.get('id')}")
            
            # Validate inputs
            self._validate_student_info(student_info)
            self._validate_responses(student_responses)
            
            if parent_info:
                self._validate_parent_info(parent_info)
            
            if parent_responses:
                self._validate_responses(parent_responses)
            
            # Analyze student responses
            analysis_results = self.analyzer.analyze_responses(
                student_responses, 
                student_info.get("age", 10)
            )
            
            # Generate learning badges
            badges = generate_learning_badges(analysis_results)
            analysis_results["badges"] = badges
            
            # Generate parent comparison if parent responses provided
            parent_comparison = None
            if parent_responses:
                parent_comparison = self.analyzer.compare_parent_responses(
                    parent_responses,
                    analysis_results
                )
            
            # Generate learning pathway
            pathway_results = self.pathway_mapper.generate_pathway(
                student_info,
                analysis_results
            )
            
            # Generate career affinities
            career_results = self.career_advisor.generate_career_affinities(
                analysis_results
            )
            
            # Generate course recommendations
            course_recommendations = self.course_recommender.recommend_courses(
                student_info,
                analysis_results,
                pathway_results
            )
            
            # Add recommended courses to analysis results for reports
            analysis_results["recommended_courses"] = course_recommendations
            
            # Save all results securely
            assessment_results = {
                "student_info": student_info,
                "parent_info": parent_info,
                "analysis_results": analysis_results,
                "parent_comparison": parent_comparison,
                "pathway_results": pathway_results,
                "career_results": career_results,
                "timestamp": datetime.now().isoformat()
            }
            
            # Encrypt sensitive data
            secure_results = self.security_manager.encrypt_sensitive_data(assessment_results)
            
            # Save secure results
            results_file = os.path.join(
                self.output_dir, 
                "data", 
                f"assessment_{student_info.get('id')}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
            )
            
            with open(results_file, 'w') as f:
                json.dump(secure_results, f, indent=2)
            
            # Generate and deliver reports
            delivery_results = None
            if parent_info:
                delivery_results = self.report_delivery.generate_and_deliver_reports(
                    student_info,
                    parent_info,
                    analysis_results,
                    parent_comparison,
                    pathway_results,
                    career_results,
                    course_recommendations
                )
            
            # Log the assessment completion
            self.security_manager.log_data_access(
                "system",
                "assessment",
                "complete",
                student_info.get("id")
            )
            
            # Return results
            return {
                "status": "success",
                "student_id": student_info.get("id"),
                "results_file": results_file,
                "delivery_results": delivery_results
            }
            
        except Exception as e:
            logging.error(f"Error processing assessment: {e}")
            return {
                "status": "error",
                "message": str(e)
            }
    
    def get_questionnaire_for_student(self, age):
        """
        Gets the appropriate questionnaire for a student based on age.
        
        Args:
            age (int): Student's age
            
        Returns:
            list: List of questions
        """
        return get_questions_for_age(age)
    
    def get_questionnaire_for_parent(self):
        """
        Gets the questionnaire for parents.
        
        Returns:
            list: List of questions
        """
        return get_parent_questions()
    
    def retrieve_assessment_results(self, student_id, user_id, user_role):
        """
        Retrieves assessment results for a student.
        
        Args:
            student_id (str): Student ID
            user_id (str): ID of the user requesting the results
            user_role (str): Role of the user requesting the results
            
        Returns:
            dict: Assessment results
        """
        # Check if user has permission to access this student's data
        if user_role == "admin":
            # Admins can access all data
            pass
        elif user_role == "teacher":
            # Check if teacher is assigned to this student
            teacher_access = self.access_control.get_user_specific_data_access(user_id)
            if not teacher_access.get("all_access") and student_id not in teacher_access.get("student_ids", []):
                return {
                    "status": "error",
                    "message": "Access denied: You are not authorized to access this student's data"
                }
        elif user_role == "parent":
            # Check if parent is associated with this student
            parent_access = self.access_control.get_user_specific_data_access(user_id)
            if not parent_access.get("all_access") and student_id not in parent_access.get("student_ids", []):
                return {
                    "status": "error",
                    "message": "Access denied: You are not authorized to access this student's data"
                }
        else:
            return {
                "status": "error",
                "message": "Access denied: Invalid user role"
            }
        
        # Log the data access
        self.security_manager.log_data_access(
            user_id,
            "assessment",
            "view",
            student_id
        )
        
        # Find the latest assessment file for this student
        data_dir = os.path.join(self.output_dir, "data")
        assessment_files = [f for f in os.listdir(data_dir) if f.startswith(f"assessment_{student_id}_")]
        
        if not assessment_files:
            return {
                "status": "error",
                "message": f"No assessment found for student ID: {student_id}"
            }
        
        # Sort files by timestamp (newest first)
        assessment_files.sort(reverse=True)
        latest_file = os.path.join(data_dir, assessment_files[0])
        
        # Load and decrypt the assessment results
        with open(latest_file, 'r') as f:
            secure_results = json.load(f)
        
        # Decrypt sensitive data
        results = self.security_manager.decrypt_sensitive_data(secure_results)
        
        return {
            "status": "success",
            "results": results
        }
    
    def create_user_account(self, admin_id, username, role, password, email=None, name=None):
        """
        Creates a new user account.
        
        Args:
            admin_id (str): ID of the admin creating the account
            username (str): Username for the new account
            role (str): Role for the new account
            password (str): Password for the new account
            email (str, optional): Email for the new account
            name (str, optional): Name for the new account
            
        Returns:
            dict: User creation result
        """
        # Check if the requesting user is an admin
        if not self.access_control.check_permission(admin_id, "manage_users"):
            return {
                "status": "error",
                "message": "Access denied: You do not have permission to create user accounts"
            }
        
        try:
            # Create the user account
            user_data = self.access_control.create_user(
                username,
                role,
                password,
                email,
                name
            )
            
            # Log the user creation
            self.security_manager.log_data_access(
                admin_id,
                "user",
                "create",
                username
            )
            
            return {
                "status": "success",
                "user": user_data
            }
        except Exception as e:
            logging.error(f"Error creating user account: {e}")
            return {
                "status": "error",
                "message": str(e)
            }
    
    def authenticate_user(self, username, password):
        """
        Authenticates a user.
        
        Args:
            username (str): Username
            password (str): Password
            
        Returns:
            dict: Authentication result
        """
        try:
            # Authenticate the user
            user_data = self.access_control.authenticate_user(username, password)
            
            if not user_data:
                return {
                    "status": "error",
                    "message": "Authentication failed: Invalid username or password"
                }
            
            # Generate an access token
            token = self.security_manager.generate_access_token(
                username,
                user_data["role"]
            )
            
            # Log the authentication
            self.security_manager.log_data_access(
                username,
                "auth",
                "login"
            )
            
            return {
                "status": "success",
                "user": user_data,
                "token": token
            }
        except Exception as e:
            logging.error(f"Error authenticating user: {e}")
            return {
                "status": "error",
                "message": str(e)
            }
    
    def _validate_student_info(self, student_info):
        """
        Validates student information.
        
        Args:
            student_info (dict): Student information to validate
            
        Raises:
            ValueError: If student information is invalid
        """
        required_fields = ["id", "name", "age"]
        for field in required_fields:
            if field not in student_info:
                raise ValueError(f"Missing required student information: {field}")
        
        # Validate age
        age = student_info.get("age")
        if not isinstance(age, int) or age < 5 or age > 18:
            raise ValueError(f"Invalid student age: {age}. Age must be between 5 and 18.")
    
    def _validate_parent_info(self, parent_info):
        """
        Validates parent information.
        
        Args:
            parent_info (dict): Parent information to validate
            
        Raises:
            ValueError: If parent information is invalid
        """
        required_fields = ["id", "name"]
        for field in required_fields:
            if field not in parent_info:
                raise ValueError(f"Missing required parent information: {field}")
        
        # At least one contact method is required
        if "email" not in parent_info and "phone" not in parent_info:
            raise ValueError("Parent must have either email or phone contact information")
    
    def _validate_responses(self, responses):
        """
        Validates questionnaire responses.
        
        Args:
            responses (dict): Responses to validate
            
        Raises:
            ValueError: If responses are invalid
        """
        if not responses:
            raise ValueError("Responses cannot be empty")
        
        for question_id, answer in responses.items():
            if not isinstance(question_id, str):
                raise ValueError(f"Invalid question ID: {question_id}")
            
            if not isinstance(answer, int) and not isinstance(answer, str):
                raise ValueError(f"Invalid answer for question {question_id}: {answer}")
    
    def _setup_logging(self):
        """
        Sets up logging for the application.
        """
        log_dir = os.path.join(self.output_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)
        
        log_file = os.path.join(log_dir, f"app_{datetime.now().strftime('%Y%m%d')}.log")
        
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )


def main():
    """
    Main function to run the diagnostic system from the command line.
    """
    parser = argparse.ArgumentParser(description='Shining Star Education Diagnostic System')
    parser.add_argument('--init', action='store_true', help='Initialize the system with default admin user')
    parser.add_argument('--demo', action='store_true', help='Run a demo assessment')
    
    args = parser.parse_args()
    
    # Create the diagnostic system
    system = ShiningStarDiagnosticSystem()
    
    if args.init:
        # Initialize the system with a default admin user
        result = system.create_user_account(
            "system",
            "admin",
            "admin",
            "ShiningStarAdmin123!",
            "admin@shiningstar.edu",
            "System Administrator"
        )
        
        print(f"System initialization: {result['status']}")
        if result['status'] == 'success':
            print(f"Default admin user created: {result['user']['username']}")
        else:
            print(f"Error: {result['message']}")
    
    if args.demo:
        # Run a demo assessment
        student_info = {
            "id": "demo_student_001",
            "name": "Alex Smith",
            "age": 12,
            "grade": 7,
            "school": "Lincoln Middle School",
            "email": "alex.smith@example.com"
        }
        
        parent_info = {
            "id": "demo_parent_001",
            "name": "Jamie Smith",
            "email": "jamie.smith@example.com",
            "phone": "555-123-4567",
            "relationship": "Parent"
        }
        
        # Get questions for this student's age
        student_questions = system.get_questionnaire_for_student(student_info["age"])
        parent_questions = system.get_questionnaire_for_parent()
        
        # Generate some demo responses
        import random
        
        student_responses = {}
        for question in student_questions:
            if question["type"] == "multiple_choice" or question["type"] == "situational":
                options = question.get("options", [])
                if options:
                    student_responses[question["id"]] = random.randint(0, len(options) - 1)
            elif question["type"] == "logic_puzzle":
                # For logic puzzles, select the correct answer 70% of the time
                if random.random() < 0.7:
                    correct_index = question["options"].index(question["correct_answer"])
                    student_responses[question["id"]] = correct_index
                else:
                    student_responses[question["id"]] = random.randint(0, len(question["options"]) - 1)
            elif question["type"] == "open_ended":
                # Skip open-ended questions in the demo
                pass
        
        parent_responses = {}
        for question in parent_questions:
            if question["type"] == "multiple_choice":
                options = question.get("options", [])
                if options:
                    parent_responses[question["id"]] = random.randint(0, len(options) - 1)
        
        # Process the assessment
        result = system.process_student_assessment(
            student_info,
            student_responses,
            parent_info,
            parent_responses
        )
        
        print(f"Demo assessment: {result['status']}")
        if result['status'] == 'success':
            print(f"Assessment completed for student: {result['student_id']}")
            print(f"Results saved to: {result['results_file']}")
            if result['delivery_results']:
                print("Reports generated and delivery simulated")
        else:
            print(f"Error: {result['message']}")


if __name__ == "__main__":
    main()
