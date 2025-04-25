"""
Learning Pathway Mapping Module
This module generates personalized learning pathways based on student profiles.
"""

class LearningPathwayMapper:
    """
    Creates personalized learning pathway recommendations based on student analysis results.
    """
    
    def __init__(self):
        """
        Initialize the learning pathway mapper with course data.
        """
        # Define course offerings by level and category
        self.courses = {
            "tech": {
                "entry": [
                    {
                        "id": "TECH101",
                        "title": "Introduction to Coding",
                        "description": "A beginner-friendly introduction to programming concepts using block-based coding.",
                        "benefits": "Builds logical thinking and introduces fundamental programming concepts.",
                        "duration": "8 weeks",
                        "age_range": "8-14"
                    },
                    {
                        "id": "TECH102",
                        "title": "Robotics Fundamentals",
                        "description": "Hands-on introduction to robotics using LEGO Mindstorms or similar platforms.",
                        "benefits": "Develops problem-solving skills and introduces engineering concepts.",
                        "duration": "10 weeks",
                        "age_range": "9-16"
                    }
                ],
                "intermediate": [
                    {
                        "id": "TECH201",
                        "title": "Python Programming",
                        "description": "Learn Python programming language fundamentals through practical projects.",
                        "benefits": "Builds real-world coding skills applicable to many technology fields.",
                        "duration": "12 weeks",
                        "age_range": "12-18"
                    },
                    {
                        "id": "TECH202",
                        "title": "Web Development Basics",
                        "description": "Introduction to HTML, CSS, and JavaScript for creating interactive websites.",
                        "benefits": "Develops creative and technical skills for the digital world.",
                        "duration": "10 weeks",
                        "age_range": "13-18"
                    }
                ],
                "advanced": [
                    {
                        "id": "TECH301",
                        "title": "AI & Machine Learning",
                        "description": "Introduction to artificial intelligence concepts and machine learning applications.",
                        "benefits": "Prepares students for cutting-edge technology careers.",
                        "duration": "14 weeks",
                        "age_range": "14-18"
                    },
                    {
                        "id": "TECH302",
                        "title": "Mobile App Development",
                        "description": "Design and build mobile applications for iOS and Android platforms.",
                        "benefits": "Creates portfolio-ready projects and introduces software development lifecycle.",
                        "duration": "16 weeks",
                        "age_range": "14-18"
                    }
                ]
            },
            "arts": {
                "entry": [
                    {
                        "id": "ARTS101",
                        "title": "Digital Art Fundamentals",
                        "description": "Introduction to digital art creation using tablets and beginner-friendly software.",
                        "benefits": "Develops creative expression and introduces digital tools.",
                        "duration": "8 weeks",
                        "age_range": "8-16"
                    },
                    {
                        "id": "ARTS102",
                        "title": "Animation Basics",
                        "description": "Learn the principles of animation through simple projects and exercises.",
                        "benefits": "Builds storytelling skills and introduces motion design concepts.",
                        "duration": "10 weeks",
                        "age_range": "9-16"
                    }
                ],
                "intermediate": [
                    {
                        "id": "ARTS201",
                        "title": "Graphic Design Principles",
                        "description": "Learn fundamental design principles and industry-standard software.",
                        "benefits": "Develops visual communication skills applicable to many creative fields.",
                        "duration": "12 weeks",
                        "age_range": "12-18"
                    },
                    {
                        "id": "ARTS202",
                        "title": "Digital Photography & Editing",
                        "description": "Master digital photography techniques and photo editing software.",
                        "benefits": "Creates portfolio-quality work and develops visual storytelling abilities.",
                        "duration": "10 weeks",
                        "age_range": "12-18"
                    }
                ],
                "advanced": [
                    {
                        "id": "ARTS301",
                        "title": "3D Modeling & Animation",
                        "description": "Create 3D models and animations using professional software.",
                        "benefits": "Prepares for careers in animation, game design, and visual effects.",
                        "duration": "14 weeks",
                        "age_range": "14-18"
                    },
                    {
                        "id": "ARTS302",
                        "title": "Digital Media Portfolio",
                        "description": "Create a professional portfolio of digital art and design projects.",
                        "benefits": "Prepares students for college applications or freelance opportunities.",
                        "duration": "16 weeks",
                        "age_range": "15-18"
                    }
                ]
            },
            "entrepreneurship": {
                "entry": [
                    {
                        "id": "BIZ101",
                        "title": "Young Entrepreneurs",
                        "description": "Introduction to business concepts through fun, hands-on projects.",
                        "benefits": "Develops creative thinking and introduces basic business principles.",
                        "duration": "8 weeks",
                        "age_range": "10-14"
                    },
                    {
                        "id": "BIZ102",
                        "title": "Design Thinking Workshop",
                        "description": "Learn the design thinking process to solve real-world problems.",
                        "benefits": "Builds problem-solving skills and introduces innovation methods.",
                        "duration": "6 weeks",
                        "age_range": "11-16"
                    }
                ],
                "intermediate": [
                    {
                        "id": "BIZ201",
                        "title": "Business Plan Development",
                        "description": "Create a comprehensive business plan for an original business idea.",
                        "benefits": "Develops strategic thinking and planning skills.",
                        "duration": "12 weeks",
                        "age_range": "13-18"
                    },
                    {
                        "id": "BIZ202",
                        "title": "Digital Marketing Essentials",
                        "description": "Learn effective digital marketing strategies for business growth.",
                        "benefits": "Builds practical skills for promoting products and services online.",
                        "duration": "10 weeks",
                        "age_range": "14-18"
                    }
                ],
                "advanced": [
                    {
                        "id": "BIZ301",
                        "title": "Startup Incubator",
                        "description": "Launch a real micro-business with mentorship and support.",
                        "benefits": "Provides real-world entrepreneurial experience and portfolio development.",
                        "duration": "16 weeks",
                        "age_range": "15-18"
                    },
                    {
                        "id": "BIZ302",
                        "title": "Leadership & Management",
                        "description": "Develop leadership skills and learn effective team management.",
                        "benefits": "Prepares for leadership roles in business and organizations.",
                        "duration": "12 weeks",
                        "age_range": "15-18"
                    }
                ]
            },
            "science": {
                "entry": [
                    {
                        "id": "SCI101",
                        "title": "Junior Scientists",
                        "description": "Hands-on science experiments and projects across various disciplines.",
                        "benefits": "Develops scientific thinking and curiosity about the natural world.",
                        "duration": "8 weeks",
                        "age_range": "8-12"
                    },
                    {
                        "id": "SCI102",
                        "title": "Environmental Science Explorers",
                        "description": "Investigate environmental systems through field work and experiments.",
                        "benefits": "Builds awareness of environmental issues and scientific methods.",
                        "duration": "10 weeks",
                        "age_range": "9-14"
                    }
                ],
                "intermediate": [
                    {
                        "id": "SCI201",
                        "title": "Applied Physics",
                        "description": "Learn physics principles through hands-on engineering challenges.",
                        "benefits": "Develops problem-solving skills and understanding of physical systems.",
                        "duration": "12 weeks",
                        "age_range": "12-16"
                    },
                    {
                        "id": "SCI202",
                        "title": "Biotechnology Basics",
                        "description": "Introduction to biotechnology concepts and laboratory techniques.",
                        "benefits": "Builds understanding of cutting-edge biological sciences.",
                        "duration": "12 weeks",
                        "age_range": "13-18"
                    }
                ],
                "advanced": [
                    {
                        "id": "SCI301",
                        "title": "Research Methods & Design",
                        "description": "Design and conduct original scientific research projects.",
                        "benefits": "Prepares for college-level research and science competitions.",
                        "duration": "16 weeks",
                        "age_range": "14-18"
                    },
                    {
                        "id": "SCI302",
                        "title": "Data Science & Analytics",
                        "description": "Learn to collect, analyze, and visualize data for scientific insights.",
                        "benefits": "Develops valuable skills for research and data-driven fields.",
                        "duration": "14 weeks",
                        "age_range": "15-18"
                    }
                ]
            },
            "language": {
                "entry": [
                    {
                        "id": "LANG101",
                        "title": "Creative Writing Workshop",
                        "description": "Develop creative writing skills through fun exercises and projects.",
                        "benefits": "Builds self-expression and communication skills.",
                        "duration": "8 weeks",
                        "age_range": "8-14"
                    },
                    {
                        "id": "LANG102",
                        "title": "Public Speaking Fundamentals",
                        "description": "Learn the basics of effective public speaking in a supportive environment.",
                        "benefits": "Develops confidence and verbal communication skills.",
                        "duration": "8 weeks",
                        "age_range": "10-16"
                    }
                ],
                "intermediate": [
                    {
                        "id": "LANG201",
                        "title": "Digital Storytelling",
                        "description": "Create compelling stories using digital media and technology.",
                        "benefits": "Combines creative writing with digital media skills.",
                        "duration": "10 weeks",
                        "age_range": "12-18"
                    },
                    {
                        "id": "LANG202",
                        "title": "Debate & Argumentation",
                        "description": "Master the art of constructing and delivering persuasive arguments.",
                        "benefits": "Develops critical thinking and advanced communication skills.",
                        "duration": "12 weeks",
                        "age_range": "13-18"
                    }
                ],
                "advanced": [
                    {
                        "id": "LANG301",
                        "title": "Content Creation & Publishing",
                        "description": "Create, edit, and publish original content across various platforms.",
                        "benefits": "Prepares for careers in writing, publishing, and digital media.",
                        "duration": "14 weeks",
                        "age_range": "14-18"
                    },
                    {
                        "id": "LANG302",
                        "title": "Professional Communication",
                        "description": "Master business writing, presentations, and professional communication.",
                        "benefits": "Develops essential skills for college and career success.",
                        "duration": "12 weeks",
                        "age_range": "15-18"
                    }
                ]
            }
        }
        
        # Define learning style to course category mappings
        self.learning_style_mappings = {
            "visual": ["arts", "tech"],
            "auditory": ["language", "science"],
            "kinesthetic": ["tech", "science"],
            "logical": ["science", "tech"],
            "social": ["entrepreneurship", "language"],
            "independent": ["science", "arts"]
        }
        
        # Define trait to course category mappings
        self.trait_mappings = {
            "creative": ["arts", "language"],
            "analytical": ["science", "tech"],
            "persistent": ["tech", "science"],
            "leadership": ["entrepreneurship", "language"],
            "collaborative": ["entrepreneurship", "language"],
            "organized": ["science", "entrepreneurship"]
        }
    
    def generate_pathway(self, student_info, analysis_results):
        """
        Generates a personalized 3-step learning pathway based on student profile.
        
        Args:
            student_info (dict): Student information including age
            analysis_results (dict): Results from the learning style analysis
            
        Returns:
            dict: Personalized learning pathway with entry, intermediate, and advanced courses
        """
        # Extract key information from analysis results
        primary_learning_style = analysis_results["learning_styles"]["primary"]
        top_traits = analysis_results["traits"]["top_traits"]
        top_interests = analysis_results["interests"]["top_interests"]
        student_age = student_info["age"]
        
        # Determine primary course category based on interests and learning style
        primary_category = self._determine_primary_category(top_interests, primary_learning_style, top_traits)
        
        # Determine secondary course category for diversification
        secondary_category = self._determine_secondary_category(primary_category, top_interests, primary_learning_style, top_traits)
        
        # Select appropriate courses for each level
        entry_course = self._select_course(primary_category, "entry", student_age)
        intermediate_course = self._select_course(primary_category, "intermediate", student_age)
        advanced_course = self._select_course(primary_category, "advanced", student_age)
        
        # Select a complementary course from secondary category
        complementary_course = self._select_course(secondary_category, "entry", student_age)
        
        # Create the pathway
        pathway = {
            "primary_category": primary_category,
            "secondary_category": secondary_category,
            "step1": {
                "title": "Building Your Foundation",
                "description": "Start with these courses to build core skills in your areas of interest and strength.",
                "primary_course": entry_course,
                "complementary_course": complementary_course
            },
            "step2": {
                "title": "Expanding Your Skills",
                "description": "Once you've mastered the basics, these courses will help you develop more advanced abilities.",
                "course": intermediate_course
            },
            "step3": {
                "title": "Specializing Your Expertise",
                "description": "These advanced courses will prepare you for real-world applications and future opportunities.",
                "course": advanced_course
            }
        }
        
        return pathway
    
    def _determine_primary_category(self, interests, learning_style, traits):
        """
        Determines the primary course category based on student profile.
        
        Args:
            interests (list): Student's top interests
            learning_style (str): Student's primary learning style
            traits (list): Student's top traits
            
        Returns:
            str: Primary course category
        """
        # First priority: use the top interest if available
        if interests and interests[0] in self.courses:
            return interests[0]
        
        # Second priority: use learning style mapping
        if learning_style in self.learning_style_mappings:
            style_categories = self.learning_style_mappings[learning_style]
            # Check if any of these categories match secondary interests
            if len(interests) > 1:
                for interest in interests[1:]:
                    if interest in style_categories:
                        return interest
            # Otherwise return the first mapped category
            return style_categories[0]
        
        # Third priority: use trait mapping
        if traits and traits[0] in self.trait_mappings:
            return self.trait_mappings[traits[0]][0]
        
        # Default to tech as a fallback
        return "tech"
    
    def _determine_secondary_category(self, primary_category, interests, learning_style, traits):
        """
        Determines a secondary course category that complements the primary category.
        
        Args:
            primary_category (str): The primary course category
            interests (list): Student's top interests
            learning_style (str): Student's primary learning style
            traits (list): Student's top traits
            
        Returns:
            str: Secondary course category
        """
        # First try to use a different interest
        for interest in interests:
            if interest in self.courses and interest != primary_category:
                return interest
        
        # Try to use learning style mapping
        if learning_style in self.learning_style_mappings:
            for category in self.learning_style_mappings[learning_style]:
                if category != primary_category:
                    return category
        
        # Try to use trait mapping
        if traits and traits[0] in self.trait_mappings:
            for category in self.trait_mappings[traits[0]]:
                if category != primary_category:
                    return category
        
        # Find any category different from primary
        for category in self.courses:
            if category != primary_category:
                return category
        
        # Fallback (should never reach here unless there's only one category)
        return primary_category
    
    def _select_course(self, category, level, student_age):
        """
        Selects an appropriate course based on category, level, and student age.
        
        Args:
            category (str): Course category
            level (str): Course level (entry, intermediate, advanced)
            student_age (int): Student's age
            
        Returns:
            dict: Selected course information
        """
        # Get available courses for the category and level
        available_courses = self.courses.get(category, {}).get(level, [])
        
        if not available_courses:
            # Return a placeholder if no courses are available
            return {
                "id": "N/A",
                "title": "Course Not Available",
                "description": "No suitable course found for this category and level.",
                "benefits": "Please contact an advisor for alternatives.",
                "duration": "N/A",
                "age_range": "N/A"
            }
        
        # Filter courses by age appropriateness
        suitable_courses = []
        for course in available_courses:
            age_range = course.get("age_range", "")
            if "-" in age_range:
                min_age, max_age = map(int, age_range.split("-"))
                if min_age <= student_age <= max_age:
                    suitable_courses.append(course)
        
        # If no age-appropriate courses, use the first available course
        if not suitable_courses and available_courses:
            return available_courses[0]
        
        # Return the first suitable course or None if none are suitable
        return suitable_courses[0] if suitable_courses else None
