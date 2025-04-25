"""
Report Generator Module
This module generates personalized insight reports based on analysis results.
"""

import os
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO

class ReportGenerator:
    """
    Generates personalized reports based on learning style analysis results.
    """
    
    def __init__(self, templates_dir):
        """
        Initialize the report generator with templates directory.
        
        Args:
            templates_dir (str): Path to the templates directory
        """
        self.templates_dir = templates_dir
        self.env = Environment(loader=FileSystemLoader(templates_dir))
        
    def generate_student_report(self, student_info, analysis_results, output_dir):
        """
        Generates a personalized student report.
        
        Args:
            student_info (dict): Student information (name, age, etc.)
            analysis_results (dict): Results from the learning style analysis
            output_dir (str): Directory to save the report
            
        Returns:
            str: Path to the generated report
        """
        # Generate charts for the report
        charts = self._generate_charts(analysis_results)
        
        # Prepare template data
        template_data = {
            "student": student_info,
            "results": analysis_results,
            "charts": charts,
            "date": datetime.now().strftime("%B %d, %Y"),
            "report_id": f"SSR-{datetime.now().strftime('%Y%m%d')}-{student_info['id']}"
        }
        
        # Render the template
        template = self.env.get_template("student_report.html")
        report_html = template.render(**template_data)
        
        # Save the report
        report_path = os.path.join(output_dir, f"student_report_{student_info['id']}.html")
        with open(report_path, "w") as f:
            f.write(report_html)
            
        return report_path
    
    def generate_parent_report(self, student_info, analysis_results, parent_comparison, output_dir):
        """
        Generates a personalized parent report.
        
        Args:
            student_info (dict): Student information (name, age, etc.)
            analysis_results (dict): Results from the learning style analysis
            parent_comparison (dict): Results from parent-student comparison
            output_dir (str): Directory to save the report
            
        Returns:
            str: Path to the generated report
        """
        # Generate charts for the report
        charts = self._generate_charts(analysis_results)
        
        # Prepare template data
        template_data = {
            "student": student_info,
            "results": analysis_results,
            "comparison": parent_comparison,
            "charts": charts,
            "date": datetime.now().strftime("%B %d, %Y"),
            "report_id": f"SPR-{datetime.now().strftime('%Y%m%d')}-{student_info['id']}"
        }
        
        # Render the template
        template = self.env.get_template("parent_report.html")
        report_html = template.render(**template_data)
        
        # Save the report
        report_path = os.path.join(output_dir, f"parent_report_{student_info['id']}.html")
        with open(report_path, "w") as f:
            f.write(report_html)
            
        return report_path
    
    def _generate_charts(self, analysis_results):
        """
        Generates charts based on analysis results.
        
        Args:
            analysis_results (dict): Results from the learning style analysis
            
        Returns:
            dict: Dictionary of chart images encoded as base64 strings
        """
        charts = {}
        
        # Generate dimension scores radar chart
        charts["dimension_radar"] = self._generate_radar_chart(analysis_results["dimension_scores"])
        
        # Generate learning styles bar chart
        # This would require additional data not currently available in the analysis results
        # For now, we'll use a placeholder
        charts["learning_styles"] = self._generate_placeholder_chart()
        
        return charts
    
    def _generate_radar_chart(self, dimension_scores):
        """
        Generates a radar chart for dimension scores.
        
        Args:
            dimension_scores (dict): Dictionary of dimension scores
            
        Returns:
            str: Base64 encoded image
        """
        # Set up the dimensions and scores
        dimensions = list(dimension_scores.keys())
        scores = list(dimension_scores.values())
        
        # Number of dimensions
        N = len(dimensions)
        
        # Create angle values for each dimension
        angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
        
        # Close the polygon by repeating the first value
        scores.append(scores[0])
        angles.append(angles[0])
        dimensions.append(dimensions[0])
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        
        # Plot the scores
        ax.plot(angles, scores, linewidth=2, linestyle='solid', color='#1f77b4')
        ax.fill(angles, scores, alpha=0.25, color='#1f77b4')
        
        # Set the labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([dim.replace('_', ' ').title() for dim in dimensions[:-1]])
        
        # Set y-axis limits
        ax.set_ylim(0, 100)
        
        # Add title
        ax.set_title("Learning Dimension Scores", size=15, color='#333333', y=1.1)
        
        # Save the chart to a BytesIO object
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        buffer.seek(0)
        
        # Encode the image as base64
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()
        
        return image_base64
    
    def _generate_placeholder_chart(self):
        """
        Generates a placeholder chart.
        
        Returns:
            str: Base64 encoded image
        """
        # Create a simple bar chart as a placeholder
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Sample data
        categories = ['Visual', 'Auditory', 'Kinesthetic', 'Logical', 'Social']
        values = [65, 45, 80, 55, 70]
        
        # Create the bar chart
        ax.bar(categories, values, color='#1f77b4')
        
        # Add labels and title
        ax.set_xlabel('Learning Styles')
        ax.set_ylabel('Score')
        ax.set_title('Learning Style Preferences')
        
        # Set y-axis limits
        ax.set_ylim(0, 100)
        
        # Add grid lines
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Save the chart to a BytesIO object
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight')
        buffer.seek(0)
        
        # Encode the image as base64
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()
        
        return image_base64
