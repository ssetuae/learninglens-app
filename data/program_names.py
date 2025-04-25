"""
Program Name Options with Taglines
This module provides unique name options with taglines for the AI-driven diagnostic program.
"""

class ProgramNameGenerator:
    """
    Generates unique name options with taglines for the AI-driven diagnostic program.
    """
    
    def __init__(self):
        """
        Initialize the program name generator with options and taglines.
        """
        self.program_names = [
            {
                "name": "LearningLens",
                "tagline": "Illuminating pathways to personalized educational excellence through AI-driven insights",
                "description": "LearningLens focuses on the diagnostic aspect of the program, suggesting how it provides clear vision into a student's learning profile. The name is memorable, easy to pronounce, and has positive connotations of clarity and focus."
            },
            {
                "name": "CognitiveCraft",
                "tagline": "Artfully mapping minds, masterfully shaping educational journeys",
                "description": "CognitiveCraft emphasizes the artistry and science behind understanding cognitive patterns. It suggests both the analytical aspect of the program and the creative, personalized approach to crafting learning pathways."
            },
            {
                "name": "EduGenesis",
                "tagline": "Where potential meets pathway: The beginning of personalized learning transformation",
                "description": "EduGenesis conveys the idea of a new beginning or origin point for educational journeys. It suggests that the diagnostic process is the starting point for a transformative educational experience tailored to each student's unique profile."
            },
            {
                "name": "MindSphere",
                "tagline": "Encompassing every dimension of learning potential to create 360° student success",
                "description": "MindSphere suggests a comprehensive, holistic approach to understanding the student's mind. The spherical imagery implies completeness, with no aspect of learning style or cognitive strength left unexplored."
            }
        ]
        
        self.additional_taglines = [
            "Decoding learning DNA for educational excellence",
            "Mapping minds, illuminating futures",
            "Where AI meets education to unlock human potential",
            "Personalized pathways to academic brilliance",
            "Transforming education through cognitive intelligence",
            "Beyond assessment: The future of personalized learning",
            "Revealing the unique blueprint of every learner"
        ]
    
    def get_program_names(self):
        """
        Returns the program name options with taglines.
        
        Returns:
            list: Program name options with taglines
        """
        return self.program_names
    
    def get_additional_taglines(self):
        """
        Returns additional tagline options.
        
        Returns:
            list: Additional tagline options
        """
        return self.additional_taglines
    
    def get_recommended_name(self):
        """
        Returns the recommended program name with tagline.
        
        Returns:
            dict: Recommended program name with tagline
        """
        # LearningLens is the recommended option
        return self.program_names[0]
