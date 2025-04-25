"""
Report Delivery Module
This module handles the generation and delivery of reports to students and parents.
"""

import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pdfkit
import requests
from datetime import datetime

class ReportDeliveryManager:
    """
    Manages the generation and delivery of reports to students and parents.
    """
    
    def __init__(self, output_dir, templates_dir):
        """
        Initialize the report delivery manager.
        
        Args:
            output_dir (str): Directory to save generated reports
            templates_dir (str): Directory containing report templates
        """
        self.output_dir = output_dir
        self.templates_dir = templates_dir
        self.pdf_output_dir = os.path.join(output_dir, "pdf")
        
        # Create output directories if they don't exist
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.pdf_output_dir, exist_ok=True)
        
        # Email configuration (would be loaded from secure config in production)
        self.email_config = {
            "smtp_server": "smtp.example.com",
            "smtp_port": 587,
            "username": "reports@shiningstar.edu",
            "password": "secure_password_here",
            "sender_email": "reports@shiningstar.edu",
            "sender_name": "Shining Star Education"
        }
        
        # WhatsApp API configuration (would be loaded from secure config in production)
        self.whatsapp_config = {
            "api_url": "https://api.whatsapp.com/send",
            "business_phone": "+1234567890"
        }
    
    def generate_and_deliver_reports(self, student_info, parent_info, analysis_results, 
                                    parent_comparison, pathway_results, career_results, 
                                    course_recommendations):
        """
        Generates and delivers reports to both student and parent.
        
        Args:
            student_info (dict): Student information
            parent_info (dict): Parent information
            analysis_results (dict): Results from learning style analysis
            parent_comparison (dict): Results from parent-student comparison
            pathway_results (dict): Results from learning pathway mapping
            career_results (dict): Results from career affinity advisor
            course_recommendations (list): Recommended courses
            
        Returns:
            dict: Delivery status and report paths
        """
        # Prepare complete data for reports
        report_data = {
            "student": student_info,
            "parent": parent_info,
            "results": analysis_results,
            "comparison": parent_comparison,
            "pathway": pathway_results,
            "careers": career_results,
            "recommended_courses": course_recommendations,
            "date": datetime.now().strftime("%B %d, %Y"),
            "report_id": f"SSR-{datetime.now().strftime('%Y%m%d')}-{student_info['id']}"
        }
        
        # Generate student report
        student_html_path, student_pdf_path = self._generate_student_report(report_data)
        
        # Generate parent report
        parent_html_path, parent_pdf_path = self._generate_parent_report(report_data)
        
        # Deliver reports
        student_delivery_status = self._deliver_student_report(student_info, student_pdf_path)
        parent_delivery_status = self._deliver_parent_report(parent_info, parent_pdf_path)
        
        # Save report data for future reference
        self._save_report_data(report_data)
        
        return {
            "student_report": {
                "html_path": student_html_path,
                "pdf_path": student_pdf_path,
                "delivery_status": student_delivery_status
            },
            "parent_report": {
                "html_path": parent_html_path,
                "pdf_path": parent_pdf_path,
                "delivery_status": parent_delivery_status
            }
        }
    
    def _generate_student_report(self, report_data):
        """
        Generates the student report in HTML and PDF formats.
        
        Args:
            report_data (dict): Complete data for the report
            
        Returns:
            tuple: Paths to the HTML and PDF reports
        """
        from data.report_generator import ReportGenerator
        
        # Generate HTML report
        report_generator = ReportGenerator(self.templates_dir)
        html_path = report_generator.generate_student_report(
            report_data["student"], 
            report_data["results"], 
            self.output_dir
        )
        
        # Generate PDF from HTML
        pdf_filename = f"student_report_{report_data['student']['id']}.pdf"
        pdf_path = os.path.join(self.pdf_output_dir, pdf_filename)
        
        try:
            pdfkit.from_file(html_path, pdf_path)
        except Exception as e:
            print(f"Error generating PDF: {e}")
            # Fallback: use HTML only
            pdf_path = None
        
        return html_path, pdf_path
    
    def _generate_parent_report(self, report_data):
        """
        Generates the parent report in HTML and PDF formats.
        
        Args:
            report_data (dict): Complete data for the report
            
        Returns:
            tuple: Paths to the HTML and PDF reports
        """
        from data.report_generator import ReportGenerator
        
        # Generate HTML report
        report_generator = ReportGenerator(self.templates_dir)
        html_path = report_generator.generate_parent_report(
            report_data["student"], 
            report_data["results"], 
            report_data["comparison"],
            self.output_dir
        )
        
        # Generate PDF from HTML
        pdf_filename = f"parent_report_{report_data['student']['id']}.pdf"
        pdf_path = os.path.join(self.pdf_output_dir, pdf_filename)
        
        try:
            pdfkit.from_file(html_path, pdf_path)
        except Exception as e:
            print(f"Error generating PDF: {e}")
            # Fallback: use HTML only
            pdf_path = None
        
        return html_path, pdf_path
    
    def _deliver_student_report(self, student_info, report_path):
        """
        Delivers the report to the student via email.
        
        Args:
            student_info (dict): Student information
            report_path (str): Path to the report PDF
            
        Returns:
            dict: Delivery status
        """
        if not report_path:
            return {"success": False, "message": "Report PDF not available"}
        
        # Check if student has email (for older students)
        if "email" in student_info and student_info["email"]:
            # Send email to student
            email_status = self._send_email(
                recipient_email=student_info["email"],
                recipient_name=student_info["name"],
                subject="Your Learning Superpowers Report - Shining Star Education",
                body=f"""
                Hi {student_info['name']},
                
                Congratulations on completing your learning style assessment! 
                
                We've analyzed your responses and created a personalized report that reveals your unique learning superpowers. 
                Attached is your full report with insights about your learning style, strengths, and recommended courses.
                
                We hope you enjoy discovering more about yourself and your learning journey!
                
                Best regards,
                The Shining Star Education Team
                """,
                attachment_path=report_path
            )
            
            return email_status
        
        # If student doesn't have email, we'll consider it delivered through the parent
        return {"success": True, "message": "Report will be delivered through parent"}
    
    def _deliver_parent_report(self, parent_info, report_path):
        """
        Delivers the report to the parent via email and WhatsApp.
        
        Args:
            parent_info (dict): Parent information
            report_path (str): Path to the report PDF
            
        Returns:
            dict: Delivery status
        """
        if not report_path:
            return {"success": False, "message": "Report PDF not available"}
        
        delivery_status = {"email": None, "whatsapp": None}
        
        # Send email to parent
        if "email" in parent_info and parent_info["email"]:
            email_status = self._send_email(
                recipient_email=parent_info["email"],
                recipient_name=parent_info["name"],
                subject="Your Child's Learning Profile Report - Shining Star Education",
                body=f"""
                Dear {parent_info['name']},
                
                Thank you for having your child complete our learning style assessment. 
                
                We've analyzed the responses and created a personalized report that provides insights into your child's learning style, strengths, and potential. The report also includes a comparison between your perceptions and your child's actual responses, which we hope you'll find valuable.
                
                Attached is the full report with recommendations for courses that match your child's learning profile.
                
                We've also sent a separate, more playful version of the report to your child (if an email was provided).
                
                To discuss these results or explore course options, please book a free consultation with one of our academic advisors.
                
                Best regards,
                The Shining Star Education Team
                """,
                attachment_path=report_path
            )
            
            delivery_status["email"] = email_status
        
        # Send WhatsApp message to parent
        if "phone" in parent_info and parent_info["phone"]:
            whatsapp_status = self._send_whatsapp(
                phone_number=parent_info["phone"],
                message=f"""
                Dear {parent_info['name']},
                
                Your child's learning profile report from Shining Star Education is ready! We've sent it to your email.
                
                To discuss the results or explore recommended courses, reply to this message or call us at +1234567890.
                
                Thank you!
                """
            )
            
            delivery_status["whatsapp"] = whatsapp_status
        
        return delivery_status
    
    def _send_email(self, recipient_email, recipient_name, subject, body, attachment_path=None):
        """
        Sends an email with optional attachment.
        
        Args:
            recipient_email (str): Recipient's email address
            recipient_name (str): Recipient's name
            subject (str): Email subject
            body (str): Email body
            attachment_path (str, optional): Path to attachment file
            
        Returns:
            dict: Email sending status
        """
        # In a real implementation, this would use the configured SMTP server
        # For this implementation, we'll simulate success
        
        print(f"Sending email to {recipient_name} <{recipient_email}>")
        print(f"Subject: {subject}")
        print(f"Attachment: {attachment_path}")
        
        # Simulate email sending
        # In a real implementation, this would use smtplib to send the email
        
        return {"success": True, "message": f"Email sent to {recipient_email}"}
    
    def _send_whatsapp(self, phone_number, message):
        """
        Sends a WhatsApp message.
        
        Args:
            phone_number (str): Recipient's phone number
            message (str): Message content
            
        Returns:
            dict: WhatsApp sending status
        """
        # In a real implementation, this would use the WhatsApp Business API
        # For this implementation, we'll simulate success
        
        print(f"Sending WhatsApp message to {phone_number}")
        print(f"Message: {message}")
        
        # Simulate WhatsApp sending
        # In a real implementation, this would use the WhatsApp API
        
        return {"success": True, "message": f"WhatsApp message sent to {phone_number}"}
    
    def _save_report_data(self, report_data):
        """
        Saves the report data for future reference.
        
        Args:
            report_data (dict): Complete report data
            
        Returns:
            str: Path to the saved data file
        """
        # Create a copy of the data without any sensitive information
        safe_data = report_data.copy()
        
        # Remove sensitive information
        if "parent" in safe_data:
            if "email" in safe_data["parent"]:
                safe_data["parent"]["email"] = "***@***.com"  # Redact email
            if "phone" in safe_data["parent"]:
                safe_data["parent"]["phone"] = "***-***-****"  # Redact phone
        
        if "student" in safe_data:
            if "email" in safe_data["student"]:
                safe_data["student"]["email"] = "***@***.com"  # Redact email
        
        # Save to JSON file
        data_filename = f"report_data_{report_data['student']['id']}.json"
        data_path = os.path.join(self.output_dir, data_filename)
        
        with open(data_path, 'w') as f:
            json.dump(safe_data, f, indent=2)
        
        return data_path
