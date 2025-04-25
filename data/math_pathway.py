"""
Mathematics Learning Pathway Module
This module implements mathematics learning pathways with focus on Abacus & Vedic Math.
"""

import os
import json
from datetime import datetime

class MathematicsPathwayGenerator:
    """
    Generates mathematics learning pathways with focus on Abacus & Vedic Math.
    """
    
    def __init__(self):
        """
        Initialize the mathematics pathway generator.
        """
        # Define mathematics pathway options
        self.math_pathways = {
            "abacus": {
                "title": "Abacus Mathematics",
                "description": "A visual and kinesthetic approach to mathematics using the abacus tool to develop mental calculation abilities and number sense.",
                "benefits": [
                    "Enhances visual-spatial processing",
                    "Develops strong mental calculation abilities",
                    "Improves concentration and focus",
                    "Builds number sense and place value understanding",
                    "Strengthens working memory"
                ],
                "levels": [
                    {
                        "level": "Beginner",
                        "title": "Abacus Foundations",
                        "description": "Introduction to the abacus tool and basic operations",
                        "skills": [
                            "Understanding abacus structure and value placement",
                            "Basic addition and subtraction on the abacus",
                            "Number representation from 1-100",
                            "Simple mental calculations"
                        ],
                        "duration": "8-12 weeks",
                        "age_range": "6-9 years",
                        "prerequisites": "Basic number recognition and counting"
                    },
                    {
                        "level": "Intermediate",
                        "title": "Abacus Calculation Mastery",
                        "description": "Advanced operations and mental calculation techniques",
                        "skills": [
                            "Multi-digit addition and subtraction",
                            "Beginning multiplication on the abacus",
                            "Mental visualization techniques",
                            "Speed and accuracy development"
                        ],
                        "duration": "12-16 weeks",
                        "age_range": "7-11 years",
                        "prerequisites": "Completion of Abacus Foundations or equivalent"
                    },
                    {
                        "level": "Advanced",
                        "title": "Mental Abacus Mastery",
                        "description": "Advanced mental calculation without physical abacus",
                        "skills": [
                            "Complex calculations using mental abacus",
                            "Multiplication and division operations",
                            "Decimal operations",
                            "Speed calculation techniques"
                        ],
                        "duration": "16-20 weeks",
                        "age_range": "8-14 years",
                        "prerequisites": "Completion of Abacus Calculation Mastery or equivalent"
                    },
                    {
                        "level": "Expert",
                        "title": "Competitive Abacus Mathematics",
                        "description": "Preparation for abacus competitions and advanced applications",
                        "skills": [
                            "Lightning calculation techniques",
                            "Complex problem-solving with mental abacus",
                            "Competition strategies and techniques",
                            "Application to advanced mathematics"
                        ],
                        "duration": "20-24 weeks",
                        "age_range": "9-16 years",
                        "prerequisites": "Completion of Mental Abacus Mastery or equivalent"
                    }
                ],
                "certification": {
                    "name": "International Abacus Mathematics Certification",
                    "levels": ["Basic", "Intermediate", "Advanced", "Master"],
                    "benefits": "Internationally recognized certification of abacus calculation proficiency"
                },
                "competitions": [
                    {
                        "name": "International Abacus Mental Arithmetic Competition",
                        "frequency": "Annual",
                        "eligibility": "Students of all ages with abacus training",
                        "description": "International competition testing speed and accuracy in mental calculations"
                    },
                    {
                        "name": "National Abacus Championship",
                        "frequency": "Annual",
                        "eligibility": "Students aged 6-18 with abacus training",
                        "description": "National-level competition with various age categories and difficulty levels"
                    }
                ],
                "career_connections": [
                    "Accounting and finance",
                    "Data analysis",
                    "Engineering",
                    "Computer science",
                    "Mathematics education"
                ]
            },
            "vedic": {
                "title": "Vedic Mathematics",
                "description": "An ancient Indian system of mathematics based on 16 sutras (formulas) that provide efficient methods for calculation and problem-solving.",
                "benefits": [
                    "Dramatically increases calculation speed",
                    "Develops mathematical intuition and insight",
                    "Reduces calculation errors",
                    "Builds pattern recognition abilities",
                    "Enhances mathematical confidence"
                ],
                "levels": [
                    {
                        "level": "Beginner",
                        "title": "Vedic Mathematics Foundations",
                        "description": "Introduction to basic Vedic mathematics principles and sutras",
                        "skills": [
                            "Understanding key Vedic sutras",
                            "Basic Vedic addition and subtraction techniques",
                            "Simple multiplication shortcuts",
                            "Checking answers using Vedic methods"
                        ],
                        "duration": "8-12 weeks",
                        "age_range": "8-11 years",
                        "prerequisites": "Basic arithmetic operations understanding"
                    },
                    {
                        "level": "Intermediate",
                        "title": "Vedic Calculation Techniques",
                        "description": "Advanced calculation methods and application of multiple sutras",
                        "skills": [
                            "Advanced multiplication techniques",
                            "Division using Vedic methods",
                            "Square and cube calculations",
                            "Decimal operations using Vedic mathematics"
                        ],
                        "duration": "12-16 weeks",
                        "age_range": "9-13 years",
                        "prerequisites": "Completion of Vedic Mathematics Foundations or equivalent"
                    },
                    {
                        "level": "Advanced",
                        "title": "Advanced Vedic Problem Solving",
                        "description": "Application of Vedic techniques to complex mathematical problems",
                        "skills": [
                            "Algebraic applications of Vedic sutras",
                            "Solving equations using Vedic methods",
                            "Advanced pattern recognition",
                            "Mental calculation of complex operations"
                        ],
                        "duration": "16-20 weeks",
                        "age_range": "10-16 years",
                        "prerequisites": "Completion of Vedic Calculation Techniques or equivalent"
                    },
                    {
                        "level": "Expert",
                        "title": "Vedic Mathematics Mastery",
                        "description": "Comprehensive mastery of all Vedic sutras and their applications",
                        "skills": [
                            "All 16 sutras and their applications",
                            "Complex problem-solving using multiple sutras",
                            "Application to competitive mathematics",
                            "Teaching and explaining Vedic techniques"
                        ],
                        "duration": "20-24 weeks",
                        "age_range": "12-18 years",
                        "prerequisites": "Completion of Advanced Vedic Problem Solving or equivalent"
                    }
                ],
                "certification": {
                    "name": "Vedic Mathematics Proficiency Certification",
                    "levels": ["Foundation", "Intermediate", "Advanced", "Master"],
                    "benefits": "Recognition of Vedic mathematics knowledge and calculation abilities"
                },
                "competitions": [
                    {
                        "name": "International Vedic Mathematics Olympiad",
                        "frequency": "Annual",
                        "eligibility": "Students aged 8-18 with Vedic mathematics knowledge",
                        "description": "International competition testing Vedic mathematics problem-solving"
                    },
                    {
                        "name": "Speed Calculation Championship",
                        "frequency": "Biannual",
                        "eligibility": "Students of all ages with mental calculation training",
                        "description": "Competition focusing on calculation speed using various methods including Vedic"
                    }
                ],
                "career_connections": [
                    "Mathematics research",
                    "Computer science and programming",
                    "Engineering",
                    "Financial analysis",
                    "Data science"
                ]
            },
            "integrated": {
                "title": "Integrated Mathematical Thinking",
                "description": "A comprehensive approach combining traditional mathematics with Abacus and Vedic techniques to develop well-rounded mathematical abilities.",
                "benefits": [
                    "Develops multiple approaches to mathematical problems",
                    "Combines visual, logical, and intuitive mathematical thinking",
                    "Builds strong calculation abilities alongside conceptual understanding",
                    "Prepares students for both academic and competitive mathematics",
                    "Enhances overall mathematical confidence and flexibility"
                ],
                "levels": [
                    {
                        "level": "Beginner",
                        "title": "Mathematical Thinking Foundations",
                        "description": "Introduction to multiple mathematical approaches and tools",
                        "skills": [
                            "Traditional arithmetic operations",
                            "Basic abacus techniques",
                            "Introduction to Vedic calculation principles",
                            "Number sense and pattern recognition"
                        ],
                        "duration": "12-16 weeks",
                        "age_range": "7-10 years",
                        "prerequisites": "Basic number understanding"
                    },
                    {
                        "level": "Intermediate",
                        "title": "Multi-Method Calculation",
                        "description": "Development of calculation skills using multiple methods",
                        "skills": [
                            "Mental abacus visualization",
                            "Vedic calculation shortcuts",
                            "Traditional algorithm mastery",
                            "Method selection for different problem types"
                        ],
                        "duration": "16-20 weeks",
                        "age_range": "8-12 years",
                        "prerequisites": "Completion of Mathematical Thinking Foundations or equivalent"
                    },
                    {
                        "level": "Advanced",
                        "title": "Comprehensive Problem Solving",
                        "description": "Application of multiple methods to complex mathematical problems",
                        "skills": [
                            "Advanced mental calculation techniques",
                            "Algebraic problem-solving using multiple approaches",
                            "Pattern recognition and generalization",
                            "Mathematical modeling and application"
                        ],
                        "duration": "20-24 weeks",
                        "age_range": "10-14 years",
                        "prerequisites": "Completion of Multi-Method Calculation or equivalent"
                    },
                    {
                        "level": "Expert",
                        "title": "Mathematical Excellence Program",
                        "description": "Preparation for mathematical competitions and advanced studies",
                        "skills": [
                            "Competition-level problem-solving",
                            "Advanced calculation mastery",
                            "Mathematical proof and reasoning",
                            "Creative mathematical thinking"
                        ],
                        "duration": "24-30 weeks",
                        "age_range": "12-18 years",
                        "prerequisites": "Completion of Comprehensive Problem Solving or equivalent"
                    }
                ],
                "certification": {
                    "name": "Comprehensive Mathematical Excellence Certification",
                    "levels": ["Foundation", "Intermediate", "Advanced", "Excellence"],
                    "benefits": "Recognition of well-rounded mathematical abilities across multiple approaches"
                },
                "competitions": [
                    {
                        "name": "International Mathematical Olympiad (IMO)",
                        "frequency": "Annual",
                        "eligibility": "Top mathematics students selected through national competitions",
                        "description": "Prestigious international competition for high school students"
                    },
                    {
                        "name": "American Mathematics Competition (AMC)",
                        "frequency": "Annual",
                        "eligibility": "Students in grades 8-12",
                        "description": "Series of competitions leading to the International Mathematical Olympiad"
                    },
                    {
                        "name": "Mathematics Kangaroo",
                        "frequency": "Annual",
                        "eligibility": "Students aged 5-18",
                        "description": "International competition with multiple age categories"
                    }
                ],
                "career_connections": [
                    "Pure and applied mathematics",
                    "Scientific research",
                    "Engineering and technology",
                    "Data science and analytics",
                    "Quantitative finance",
                    "Computer science and artificial intelligence"
                ]
            }
        }
        
        # Define mathematics courses
        self.math_courses = {
            "elementary": [
                {
                    "id": "MATH101",
                    "title": "Abacus Adventures: Level 1",
                    "description": "A fun introduction to the abacus for young learners, building number sense and basic calculation skills.",
                    "pathway": "abacus",
                    "level": "Beginner",
                    "age_range": "6-8",
                    "duration": "8 weeks",
                    "key_skills": [
                        "Abacus structure and operation",
                        "Numbers 1-100 on the abacus",
                        "Basic addition and subtraction",
                        "Beginning mental visualization"
                    ],
                    "next_course": "MATH102"
                },
                {
                    "id": "MATH102",
                    "title": "Abacus Adventures: Level 2",
                    "description": "Building on basic abacus skills to develop stronger calculation abilities and mental math.",
                    "pathway": "abacus",
                    "level": "Beginner-Intermediate",
                    "age_range": "7-9",
                    "duration": "8 weeks",
                    "key_skills": [
                        "Two-digit addition and subtraction",
                        "Beginning multiplication concepts",
                        "Enhanced mental visualization",
                        "Speed and accuracy development"
                    ],
                    "next_course": "MATH201"
                },
                {
                    "id": "MATH103",
                    "title": "Vedic Math for Kids",
                    "description": "An engaging introduction to Vedic mathematics principles through games and activities.",
                    "pathway": "vedic",
                    "level": "Beginner",
                    "age_range": "8-10",
                    "duration": "8 weeks",
                    "key_skills": [
                        "Basic Vedic sutras",
                        "Simple calculation shortcuts",
                        "Pattern recognition",
                        "Mental math foundations"
                    ],
                    "next_course": "MATH203"
                },
                {
                    "id": "MATH104",
                    "title": "Math Explorers: Multiple Methods",
                    "description": "Exploration of different mathematical approaches including traditional, abacus, and Vedic techniques.",
                    "pathway": "integrated",
                    "level": "Beginner",
                    "age_range": "7-10",
                    "duration": "10 weeks",
                    "key_skills": [
                        "Multiple calculation methods",
                        "Number sense development",
                        "Basic abacus and Vedic techniques",
                        "Mathematical flexibility"
                    ],
                    "next_course": "MATH204"
                }
            ],
            "middle": [
                {
                    "id": "MATH201",
                    "title": "Mental Abacus Mastery",
                    "description": "Advancing from physical abacus to mental calculation using abacus visualization.",
                    "pathway": "abacus",
                    "level": "Intermediate",
                    "age_range": "8-12",
                    "duration": "12 weeks",
                    "key_skills": [
                        "Mental abacus visualization",
                        "Multi-digit operations",
                        "Speed calculation techniques",
                        "Application to school mathematics"
                    ],
                    "next_course": "MATH301"
                },
                {
                    "id": "MATH202",
                    "title": "Abacus Competition Preparation",
                    "description": "Specialized training for students interested in abacus competitions.",
                    "pathway": "abacus",
                    "level": "Intermediate-Advanced",
                    "age_range": "9-13",
                    "duration": "12 weeks",
                    "key_skills": [
                        "Competition techniques",
                        "Speed and accuracy drills",
                        "Complex calculation patterns",
                        "Competition strategies"
                    ],
                    "next_course": "MATH301"
                },
                {
                    "id": "MATH203",
                    "title": "Vedic Mathematics: Calculation Mastery",
                    "description": "Comprehensive study of Vedic calculation techniques for enhanced mathematical performance.",
                    "pathway": "vedic",
                    "level": "Intermediate",
                    "age_range": "10-14",
                    "duration": "12 weeks",
                    "key_skills": [
                        "Advanced Vedic sutras",
                        "Multiplication and division shortcuts",
                        "Square and cube calculations",
                        "Decimal operations"
                    ],
                    "next_course": "MATH303"
                },
                {
                    "id": "MATH204",
                    "title": "Integrated Mathematical Problem Solving",
                    "description": "Development of problem-solving skills using multiple mathematical approaches.",
                    "pathway": "integrated",
                    "level": "Intermediate",
                    "age_range": "10-13",
                    "duration": "14 weeks",
                    "key_skills": [
                        "Problem-solving strategies",
                        "Method selection for efficiency",
                        "Pattern recognition",
                        "Mathematical reasoning"
                    ],
                    "next_course": "MATH304"
                }
            ],
            "high": [
                {
                    "id": "MATH301",
                    "title": "Advanced Abacus and Mental Arithmetic",
                    "description": "Mastery-level abacus techniques and lightning-fast mental calculation abilities.",
                    "pathway": "abacus",
                    "level": "Advanced",
                    "age_range": "11-16",
                    "duration": "16 weeks",
                    "key_skills": [
                        "Complex mental calculations",
                        "Advanced abacus techniques",
                        "Application to advanced mathematics",
                        "Teaching and demonstration skills"
                    ],
                    "next_course": None
                },
                {
                    "id": "MATH302",
                    "title": "Abacus Teacher Training",
                    "description": "Preparation for students who wish to become abacus instructors.",
                    "pathway": "abacus",
                    "level": "Expert",
                    "age_range": "14-18",
                    "duration": "20 weeks",
                    "key_skills": [
                        "Advanced abacus mastery",
                        "Teaching methodology",
                        "Student assessment techniques",
                        "Curriculum development"
                    ],
                    "next_course": None
                },
                {
                    "id": "MATH303",
                    "title": "Advanced Vedic Mathematics",
                    "description": "Comprehensive study of all 16 Vedic sutras and their applications to complex mathematics.",
                    "pathway": "vedic",
                    "level": "Advanced",
                    "age_range": "13-18",
                    "duration": "16 weeks",
                    "key_skills": [
                        "All 16 Vedic sutras",
                        "Application to algebra and calculus",
                        "Complex problem-solving",
                        "Competitive mathematics preparation"
                    ],
                    "next_course": None
                },
                {
                    "id": "MATH304",
                    "title": "Mathematical Excellence Program",
                    "description": "Elite program for mathematically gifted students preparing for competitions and advanced studies.",
                    "pathway": "integrated",
                    "level": "Advanced-Expert",
                    "age_range": "14-18",
                    "duration": "24 weeks",
                    "key_skills": [
                        "Olympiad-level problem-solving",
                        "Advanced calculation mastery",
                        "Mathematical proof techniques",
                        "Research and exploration"
                    ],
                    "next_course": None
                }
            ]
        }
    
    def generate_math_pathway(self, student_info, analysis_results):
        """
        Generates a mathematics learning pathway based on student profile.
        
        Args:
            student_info (dict): Student information
            analysis_results (dict): Results from learning style analysis
            
        Returns:
            dict: Mathematics learning pathway
        """
        # Extract relevant information
        age = student_info.get("age", 10)
        learning_styles = analysis_results.get("learning_styles", {})
        traits = analysis_results.get("traits", {})
        interests = analysis_results.get("interests", {})
        
        primary_style = learning_styles.get("primary", "")
        secondary_styles = learning_styles.get("secondary", [])
        top_traits = traits.get("top_traits", [])
        top_interests = interests.get("top_interests", [])
        
        # Determine the most suitable math pathway
        pathway_type = self._determine_math_pathway_type(
            primary_style,
            secondary_styles,
            top_traits
        )
        
        # Get the pathway details
        pathway_details = self.math_pathways.get(pathway_type, self.math_pathways["integrated"])
        
        # Determine appropriate level based on age
        level_index = self._determine_level_index(age)
        
        # Get appropriate courses based on age group and pathway
        recommended_courses = self._get_recommended_courses(
            age,
            pathway_type,
            level_index
        )
        
        # Generate personalized pathway description
        personalized_description = self._generate_personalized_pathway_description(
            pathway_type,
            primary_style,
            top_traits,
            top_interests
        )
        
        # Generate learning journey steps
        journey_steps = self._generate_journey_steps(
            pathway_type,
            level_index,
            recommended_courses
        )
        
        # Generate examination recommendations
        exam_recommendations = self._generate_exam_recommendations(
            pathway_type,
            age
        )
        
        # Compile the complete pathway
        math_pathway = {
            "type": pathway_type,
            "title": pathway_details["title"],
            "description": pathway_details["description"],
            "personalized_description": personalized_description,
            "benefits": pathway_details["benefits"],
            "journey_steps": journey_steps,
            "recommended_courses": recommended_courses,
            "certification": pathway_details["certification"],
            "competitions": pathway_details["competitions"][:2],  # Limit to top 2
            "exam_recommendations": exam_recommendations,
            "career_connections": pathway_details["career_connections"][:5]  # Limit to top 5
        }
        
        return math_pathway
    
    def _determine_math_pathway_type(self, primary_style, secondary_styles, top_traits):
        """
        Determines the most suitable math pathway type based on learning style and traits.
        
        Args:
            primary_style (str): Primary learning style
            secondary_styles (list): Secondary learning styles
            top_traits (list): Top personality traits
            
        Returns:
            str: Math pathway type ("abacus", "vedic", or "integrated")
        """
        # Score each pathway based on learning style and traits
        pathway_scores = {
            "abacus": 0,
            "vedic": 0,
            "integrated": 0
        }
        
        # Score based on primary learning style
        style_scores = {
            "visual": {"abacus": 3, "vedic": 1, "integrated": 2},
            "kinesthetic": {"abacus": 3, "vedic": 1, "integrated": 2},
            "logical": {"abacus": 1, "vedic": 3, "integrated": 2},
            "independent": {"abacus": 2, "vedic": 2, "integrated": 2},
            "auditory": {"abacus": 0, "vedic": 2, "integrated": 2},
            "social": {"abacus": 1, "vedic": 1, "integrated": 3}
        }
        
        if primary_style in style_scores:
            for pathway, score in style_scores[primary_style].items():
                pathway_scores[pathway] += score
        
        # Score based on secondary learning styles
        for style in secondary_styles:
            if style in style_scores:
                for pathway, score in style_scores[style].items():
                    pathway_scores[pathway] += score / 2  # Half weight for secondary styles
        
        # Score based on traits
        trait_scores = {
            "analytical": {"abacus": 2, "vedic": 3, "integrated": 2},
            "creative": {"abacus": 1, "vedic": 2, "integrated": 3},
            "persistent": {"abacus": 3, "vedic": 2, "integrated": 2},
            "leadership": {"abacus": 1, "vedic": 1, "integrated": 3},
            "collaborative": {"abacus": 1, "vedic": 1, "integrated": 3},
            "organized": {"abacus": 3, "vedic": 2, "integrated": 2}
        }
        
        for i, trait in enumerate(top_traits[:3]):  # Consider top 3 traits
            if trait in trait_scores:
                weight = 1.0 if i == 0 else 0.7 if i == 1 else 0.4  # Decreasing weights
                for pathway, score in trait_scores[trait].items():
                    pathway_scores[pathway] += score * weight
        
        # Find the pathway with the highest score
        max_score = 0
        best_pathway = "integrated"  # Default
        
        for pathway, score in pathway_scores.items():
            if score > max_score:
                max_score = score
                best_pathway = pathway
        
        return best_pathway
    
    def _determine_level_index(self, age):
        """
        Determines the appropriate level index based on age.
        
        Args:
            age (int): Student's age
            
        Returns:
            int: Level index (0-3)
        """
        if age <= 8:
            return 0  # Beginner
        elif age <= 11:
            return 1  # Intermediate
        elif age <= 14:
            return 2  # Advanced
        else:
            return 3  # Expert
    
    def _get_recommended_courses(self, age, pathway_type, level_index):
        """
        Gets recommended courses based on age, pathway type, and level.
        
        Args:
            age (int): Student's age
            pathway_type (str): Math pathway type
            level_index (int): Level index
            
        Returns:
            list: Recommended courses
        """
        # Determine age group
        if age <= 10:
            age_group = "elementary"
        elif age <= 13:
            age_group = "middle"
        else:
            age_group = "high"
        
        # Get courses for the age group
        age_group_courses = self.math_courses.get(age_group, [])
        
        # Filter courses by pathway and level appropriateness
        recommended = []
        
        for course in age_group_courses:
            # Check if course is in the recommended pathway
            if course["pathway"] == pathway_type:
                # Check if course level is appropriate
                course_level = course["level"].lower()
                
                if level_index == 0 and "beginner" in course_level:
                    recommended.append(course)
                elif level_index == 1 and "intermediate" in course_level:
                    recommended.append(course)
                elif level_index == 2 and "advanced" in course_level:
                    recommended.append(course)
                elif level_index == 3 and "expert" in course_level:
                    recommended.append(course)
        
        # If no courses match exactly, include courses from the integrated pathway
        if not recommended and pathway_type != "integrated":
            for course in age_group_courses:
                if course["pathway"] == "integrated":
                    recommended.append(course)
        
        # If still no courses, include any course appropriate for the age
        if not recommended:
            for course in age_group_courses:
                age_range = course.get("age_range", "")
                if "-" in age_range:
                    min_age, max_age = map(int, age_range.split("-"))
                    if min_age <= age <= max_age:
                        recommended.append(course)
        
        # Limit to top 3 courses
        return recommended[:3]
    
    def _generate_personalized_pathway_description(self, pathway_type, primary_style, top_traits, top_interests):
        """
        Generates a personalized pathway description.
        
        Args:
            pathway_type (str): Math pathway type
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            top_interests (list): Top interest areas
            
        Returns:
            str: Personalized pathway description
        """
        # Base descriptions by pathway type
        base_descriptions = {
            "abacus": "The Abacus Mathematics pathway offers a visual and hands-on approach to developing calculation skills and number sense.",
            "vedic": "The Vedic Mathematics pathway provides efficient calculation techniques and mathematical shortcuts based on ancient Indian mathematical principles.",
            "integrated": "The Integrated Mathematical Thinking pathway combines traditional, Abacus, and Vedic approaches for comprehensive mathematical development."
        }
        
        # Get base description
        description = base_descriptions.get(pathway_type, base_descriptions["integrated"])
        
        # Add learning style component
        style_components = {
            "visual": "This pathway aligns well with your visual learning style, using spatial arrangements and visual patterns to enhance mathematical understanding.",
            "kinesthetic": "This pathway complements your hands-on learning style, providing tactile experiences that make mathematical concepts concrete and accessible.",
            "logical": "This pathway resonates with your logical learning style, offering systematic approaches to mathematical problem-solving.",
            "independent": "This pathway supports your independent learning style, providing techniques you can practice and master at your own pace.",
            "auditory": "While working through this pathway, you'll benefit from verbalizing the steps and discussing concepts to engage your auditory learning style.",
            "social": "This pathway can be enhanced through collaborative learning, allowing you to leverage your social learning preferences."
        }
        
        if primary_style in style_components:
            description += " " + style_components[primary_style]
        
        # Add trait component
        trait_components = {
            "analytical": "Your analytical nature will help you excel in breaking down mathematical processes into logical steps.",
            "creative": "Your creative thinking will allow you to find unique applications and connections within mathematical concepts.",
            "persistent": "Your persistence will be valuable as you develop increasingly advanced calculation skills.",
            "leadership": "Your leadership qualities can be channeled into helping peers understand these mathematical techniques.",
            "collaborative": "Your collaborative nature will enhance group learning experiences in mathematics.",
            "organized": "Your organizational skills will help you systematically master each level of mathematical development."
        }
        
        if top_traits and top_traits[0] in trait_components:
            description += " " + trait_components[top_traits[0]]
        
        # Add interest component if mathematics is a top interest
        if "mathematics" in top_interests:
            description += " Your interest in mathematics will provide intrinsic motivation as you explore these powerful calculation techniques."
        
        return description
    
    def _generate_journey_steps(self, pathway_type, level_index, recommended_courses):
        """
        Generates learning journey steps.
        
        Args:
            pathway_type (str): Math pathway type
            level_index (int): Level index
            recommended_courses (list): Recommended courses
            
        Returns:
            list: Learning journey steps
        """
        # Get pathway levels
        pathway_levels = self.math_pathways.get(pathway_type, {}).get("levels", [])
        
        # Start from the appropriate level based on level_index
        relevant_levels = pathway_levels[level_index:level_index + 3]
        
        # Ensure we have at least 3 steps
        while len(relevant_levels) < 3:
            if pathway_type != "integrated":
                # Add levels from integrated pathway if needed
                integrated_levels = self.math_pathways["integrated"]["levels"]
                for level in integrated_levels:
                    if level["level"] not in [l["level"] for l in relevant_levels]:
                        relevant_levels.append(level)
                        if len(relevant_levels) >= 3:
                            break
            else:
                # If already on integrated pathway, duplicate the last level with modifications
                if relevant_levels:
                    last_level = relevant_levels[-1].copy()
                    last_level["title"] += " (Advanced)"
                    last_level["description"] = "Further advancement in mathematical excellence and problem-solving."
                    relevant_levels.append(last_level)
        
        # Limit to 3 steps
        journey_steps = relevant_levels[:3]
        
        # Match courses to steps where possible
        for i, step in enumerate(journey_steps):
            step_with_course = step.copy()
            
            # Try to find a matching course
            matching_course = None
            for course in recommended_courses:
                if course["level"].lower() in step["level"].lower():
                    matching_course = course
                    break
            
            if matching_course:
                step_with_course["course"] = matching_course
            elif recommended_courses and i < len(recommended_courses):
                # If no exact match, assign a course anyway
                step_with_course["course"] = recommended_courses[i]
            
            journey_steps[i] = step_with_course
        
        return journey_steps
    
    def _generate_exam_recommendations(self, pathway_type, age):
        """
        Generates examination recommendations.
        
        Args:
            pathway_type (str): Math pathway type
            age (int): Student's age
            
        Returns:
            list: Examination recommendations
        """
        # Define age-appropriate math competitions
        elementary_competitions = [
            {
                "name": "Math Kangaroo",
                "description": "International mathematical competition with age-appropriate problems",
                "age_range": "Grades 1-12",
                "website": "https://www.mathkangaroo.org/",
                "preparation": "Regular practice with mathematical puzzles and problems"
            },
            {
                "name": "International Mathematics Olympiad (IMO) - Elementary Level",
                "description": "Mathematics competition for elementary students",
                "age_range": "Grades 1-5",
                "website": "https://www.imo-official.org/",
                "preparation": "Practice with challenging math problems beyond grade level"
            },
            {
                "name": "Abacus & Mental Arithmetic Competition",
                "description": "Competition testing abacus and mental calculation skills",
                "age_range": "Ages 4-12",
                "website": "Various regional organizations",
                "preparation": "Regular abacus practice and speed calculation drills"
            }
        ]
        
        middle_competitions = [
            {
                "name": "American Mathematics Competition 8 (AMC 8)",
                "description": "25-question multiple choice contest for middle school students",
                "age_range": "Grades 6-8",
                "website": "https://www.maa.org/math-competitions/amc-8",
                "preparation": "Practice with previous AMC 8 problems and middle school competition math"
            },
            {
                "name": "Math Counts",
                "description": "National middle school coaching and competition program",
                "age_range": "Grades 6-8",
                "website": "https://www.mathcounts.org/",
                "preparation": "Regular practice with competition-style problems and team strategies"
            },
            {
                "name": "International Vedic Mathematics Olympiad",
                "description": "Competition testing Vedic mathematics knowledge and application",
                "age_range": "Ages 8-14",
                "website": "Various organizations",
                "preparation": "Practice with Vedic mathematics techniques and speed calculations"
            },
            {
                "name": "International Junior Math Olympiad (IJMO)",
                "description": "International competition for middle school students",
                "age_range": "Grades 6-8",
                "website": "https://www.ijmo.org/",
                "preparation": "Practice with olympiad-style problems and proof techniques"
            }
        ]
        
        high_competitions = [
            {
                "name": "American Mathematics Competition 10/12 (AMC 10/12)",
                "description": "First in a series of competitions leading to the International Mathematical Olympiad",
                "age_range": "Grades 9-12",
                "website": "https://www.maa.org/math-competitions",
                "preparation": "Regular practice with AMC problems and advanced mathematical concepts"
            },
            {
                "name": "American Invitational Mathematics Examination (AIME)",
                "description": "Qualification round after AMC 10/12 for top-scoring students",
                "age_range": "Grades 9-12",
                "website": "https://www.maa.org/math-competitions",
                "preparation": "Intensive practice with previous AIME problems and proof techniques"
            },
            {
                "name": "International Mathematical Olympiad (IMO)",
                "description": "Prestigious international competition for high school students",
                "age_range": "Under 20 years old",
                "website": "https://www.imo-official.org/",
                "preparation": "Extensive training in advanced mathematical problem-solving and proof techniques"
            },
            {
                "name": "Harvard-MIT Mathematics Tournament (HMMT)",
                "description": "Prestigious competition hosted by Harvard and MIT",
                "age_range": "High school students",
                "website": "https://www.hmmt.org/",
                "preparation": "Team and individual practice with advanced competition mathematics"
            }
        ]
        
        # Select age-appropriate competitions
        if age <= 10:
            competitions = elementary_competitions
        elif age <= 13:
            competitions = middle_competitions
        else:
            competitions = high_competitions
        
        # Add pathway-specific competitions
        pathway_competitions = self.math_pathways.get(pathway_type, {}).get("competitions", [])
        
        # Filter pathway competitions by age
        age_appropriate_pathway_competitions = []
        for comp in pathway_competitions:
            eligibility = comp.get("eligibility", "")
            if "all ages" in eligibility.lower() or str(age) in eligibility:
                age_appropriate_pathway_competitions.append({
                    "name": comp["name"],
                    "description": comp["description"],
                    "age_range": comp["eligibility"],
                    "website": "Contact Shining Star Education for details",
                    "preparation": "Specialized training through our pathway programs"
                })
        
        # Combine and prioritize
        recommendations = age_appropriate_pathway_competitions + competitions
        
        # Limit to top 5
        return recommendations[:5]
