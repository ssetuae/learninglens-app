"""
Course Recommendation System
This module recommends courses based on student learning profiles.
"""

class CourseRecommender:
    """
    Recommends Shining Star courses based on student analysis results.
    """
    
    def __init__(self):
        """
        Initialize the course recommender with course data.
        """
        # Define course catalog with detailed information
        self.courses = {
            "tech": [
                {
                    "id": "TECH101",
                    "title": "Introduction to Coding",
                    "description": "A beginner-friendly introduction to programming concepts using block-based coding.",
                    "benefits": "Builds logical thinking and introduces fundamental programming concepts.",
                    "duration": "8 weeks",
                    "age_range": "8-14",
                    "learning_styles": ["visual", "logical", "kinesthetic"],
                    "traits": ["analytical", "persistent", "creative"],
                    "discount_eligible": True,
                    "next_start_date": "June 5, 2025",
                    "popularity": 95
                },
                {
                    "id": "TECH102",
                    "title": "Robotics Fundamentals",
                    "description": "Hands-on introduction to robotics using LEGO Mindstorms or similar platforms.",
                    "benefits": "Develops problem-solving skills and introduces engineering concepts.",
                    "duration": "10 weeks",
                    "age_range": "9-16",
                    "learning_styles": ["kinesthetic", "logical", "visual"],
                    "traits": ["analytical", "persistent", "creative"],
                    "discount_eligible": True,
                    "next_start_date": "May 15, 2025",
                    "popularity": 90
                },
                {
                    "id": "TECH201",
                    "title": "Python Programming",
                    "description": "Learn Python programming language fundamentals through practical projects.",
                    "benefits": "Builds real-world coding skills applicable to many technology fields.",
                    "duration": "12 weeks",
                    "age_range": "12-18",
                    "learning_styles": ["logical", "visual", "independent"],
                    "traits": ["analytical", "persistent", "organized"],
                    "discount_eligible": True,
                    "next_start_date": "June 10, 2025",
                    "popularity": 88
                },
                {
                    "id": "TECH202",
                    "title": "Web Development Basics",
                    "description": "Introduction to HTML, CSS, and JavaScript for creating interactive websites.",
                    "benefits": "Develops creative and technical skills for the digital world.",
                    "duration": "10 weeks",
                    "age_range": "13-18",
                    "learning_styles": ["visual", "logical", "independent"],
                    "traits": ["creative", "analytical", "organized"],
                    "discount_eligible": True,
                    "next_start_date": "May 20, 2025",
                    "popularity": 85
                },
                {
                    "id": "TECH301",
                    "title": "AI & Machine Learning",
                    "description": "Introduction to artificial intelligence concepts and machine learning applications.",
                    "benefits": "Prepares students for cutting-edge technology careers.",
                    "duration": "14 weeks",
                    "age_range": "14-18",
                    "learning_styles": ["logical", "visual", "independent"],
                    "traits": ["analytical", "persistent", "organized"],
                    "discount_eligible": False,
                    "next_start_date": "July 1, 2025",
                    "popularity": 92
                }
            ],
            "arts": [
                {
                    "id": "ARTS101",
                    "title": "Digital Art Fundamentals",
                    "description": "Introduction to digital art creation using tablets and beginner-friendly software.",
                    "benefits": "Develops creative expression and introduces digital tools.",
                    "duration": "8 weeks",
                    "age_range": "8-16",
                    "learning_styles": ["visual", "kinesthetic", "independent"],
                    "traits": ["creative", "persistent", "organized"],
                    "discount_eligible": True,
                    "next_start_date": "May 12, 2025",
                    "popularity": 88
                },
                {
                    "id": "ARTS102",
                    "title": "Animation Basics",
                    "description": "Learn the principles of animation through simple projects and exercises.",
                    "benefits": "Builds storytelling skills and introduces motion design concepts.",
                    "duration": "10 weeks",
                    "age_range": "9-16",
                    "learning_styles": ["visual", "kinesthetic", "creative"],
                    "traits": ["creative", "persistent", "organized"],
                    "discount_eligible": True,
                    "next_start_date": "June 8, 2025",
                    "popularity": 85
                },
                {
                    "id": "ARTS201",
                    "title": "Graphic Design Principles",
                    "description": "Learn fundamental design principles and industry-standard software.",
                    "benefits": "Develops visual communication skills applicable to many creative fields.",
                    "duration": "12 weeks",
                    "age_range": "12-18",
                    "learning_styles": ["visual", "logical", "independent"],
                    "traits": ["creative", "analytical", "organized"],
                    "discount_eligible": True,
                    "next_start_date": "May 25, 2025",
                    "popularity": 82
                },
                {
                    "id": "ARTS301",
                    "title": "3D Modeling & Animation",
                    "description": "Create 3D models and animations using professional software.",
                    "benefits": "Prepares for careers in animation, game design, and visual effects.",
                    "duration": "14 weeks",
                    "age_range": "14-18",
                    "learning_styles": ["visual", "logical", "kinesthetic"],
                    "traits": ["creative", "analytical", "persistent"],
                    "discount_eligible": False,
                    "next_start_date": "July 5, 2025",
                    "popularity": 80
                }
            ],
            "entrepreneurship": [
                {
                    "id": "BIZ101",
                    "title": "Young Entrepreneurs",
                    "description": "Introduction to business concepts through fun, hands-on projects.",
                    "benefits": "Develops creative thinking and introduces basic business principles.",
                    "duration": "8 weeks",
                    "age_range": "10-14",
                    "learning_styles": ["social", "kinesthetic", "auditory"],
                    "traits": ["leadership", "creative", "collaborative"],
                    "discount_eligible": True,
                    "next_start_date": "June 1, 2025",
                    "popularity": 85
                },
                {
                    "id": "BIZ102",
                    "title": "Design Thinking Workshop",
                    "description": "Learn the design thinking process to solve real-world problems.",
                    "benefits": "Builds problem-solving skills and introduces innovation methods.",
                    "duration": "6 weeks",
                    "age_range": "11-16",
                    "learning_styles": ["visual", "kinesthetic", "social"],
                    "traits": ["creative", "analytical", "collaborative"],
                    "discount_eligible": True,
                    "next_start_date": "May 18, 2025",
                    "popularity": 80
                },
                {
                    "id": "BIZ201",
                    "title": "Business Plan Development",
                    "description": "Create a comprehensive business plan for an original business idea.",
                    "benefits": "Develops strategic thinking and planning skills.",
                    "duration": "12 weeks",
                    "age_range": "13-18",
                    "learning_styles": ["logical", "social", "independent"],
                    "traits": ["leadership", "analytical", "organized"],
                    "discount_eligible": True,
                    "next_start_date": "June 15, 2025",
                    "popularity": 78
                },
                {
                    "id": "BIZ301",
                    "title": "Startup Incubator",
                    "description": "Launch a real micro-business with mentorship and support.",
                    "benefits": "Provides real-world entrepreneurial experience and portfolio development.",
                    "duration": "16 weeks",
                    "age_range": "15-18",
                    "learning_styles": ["social", "logical", "independent"],
                    "traits": ["leadership", "persistent", "creative"],
                    "discount_eligible": False,
                    "next_start_date": "July 10, 2025",
                    "popularity": 88
                }
            ],
            "science": [
                {
                    "id": "SCI101",
                    "title": "Junior Scientists",
                    "description": "Hands-on science experiments and projects across various disciplines.",
                    "benefits": "Develops scientific thinking and curiosity about the natural world.",
                    "duration": "8 weeks",
                    "age_range": "8-12",
                    "learning_styles": ["kinesthetic", "logical", "visual"],
                    "traits": ["analytical", "persistent", "creative"],
                    "discount_eligible": True,
                    "next_start_date": "May 22, 2025",
                    "popularity": 86
                },
                {
                    "id": "SCI102",
                    "title": "Environmental Science Explorers",
                    "description": "Investigate environmental systems through field work and experiments.",
                    "benefits": "Builds awareness of environmental issues and scientific methods.",
                    "duration": "10 weeks",
                    "age_range": "9-14",
                    "learning_styles": ["kinesthetic", "visual", "social"],
                    "traits": ["analytical", "persistent", "collaborative"],
                    "discount_eligible": True,
                    "next_start_date": "June 5, 2025",
                    "popularity": 82
                },
                {
                    "id": "SCI201",
                    "title": "Applied Physics",
                    "description": "Learn physics principles through hands-on engineering challenges.",
                    "benefits": "Develops problem-solving skills and understanding of physical systems.",
                    "duration": "12 weeks",
                    "age_range": "12-16",
                    "learning_styles": ["kinesthetic", "logical", "visual"],
                    "traits": ["analytical", "persistent", "creative"],
                    "discount_eligible": True,
                    "next_start_date": "May 28, 2025",
                    "popularity": 78
                },
                {
                    "id": "SCI301",
                    "title": "Research Methods & Design",
                    "description": "Design and conduct original scientific research projects.",
                    "benefits": "Prepares for college-level research and science competitions.",
                    "duration": "16 weeks",
                    "age_range": "14-18",
                    "learning_styles": ["logical", "independent", "visual"],
                    "traits": ["analytical", "persistent", "organized"],
                    "discount_eligible": False,
                    "next_start_date": "July 8, 2025",
                    "popularity": 75
                }
            ],
            "language": [
                {
                    "id": "LANG101",
                    "title": "Creative Writing Workshop",
                    "description": "Develop creative writing skills through fun exercises and projects.",
                    "benefits": "Builds self-expression and communication skills.",
                    "duration": "8 weeks",
                    "age_range": "8-14",
                    "learning_styles": ["auditory", "visual", "independent"],
                    "traits": ["creative", "organized", "persistent"],
                    "discount_eligible": True,
                    "next_start_date": "May 15, 2025",
                    "popularity": 84
                },
                {
                    "id": "LANG102",
                    "title": "Public Speaking Fundamentals",
                    "description": "Learn the basics of effective public speaking in a supportive environment.",
                    "benefits": "Develops confidence and verbal communication skills.",
                    "duration": "8 weeks",
                    "age_range": "10-16",
                    "learning_styles": ["auditory", "social", "kinesthetic"],
                    "traits": ["leadership", "collaborative", "persistent"],
                    "discount_eligible": True,
                    "next_start_date": "June 10, 2025",
                    "popularity": 80
                },
                {
                    "id": "LANG201",
                    "title": "Digital Storytelling",
                    "description": "Create compelling stories using digital media and technology.",
                    "benefits": "Combines creative writing with digital media skills.",
                    "duration": "10 weeks",
                    "age_range": "12-18",
                    "learning_styles": ["visual", "auditory", "independent"],
                    "traits": ["creative", "analytical", "organized"],
                    "discount_eligible": True,
                    "next_start_date": "May 25, 2025",
                    "popularity": 82
                },
                {
                    "id": "LANG301",
                    "title": "Content Creation & Publishing",
                    "description": "Create, edit, and publish original content across various platforms.",
                    "benefits": "Prepares for careers in writing, publishing, and digital media.",
                    "duration": "14 weeks",
                    "age_range": "14-18",
                    "learning_styles": ["visual", "independent", "auditory"],
                    "traits": ["creative", "organized", "persistent"],
                    "discount_eligible": False,
                    "next_start_date": "July 1, 2025",
                    "popularity": 78
                }
            ]
        }
    
    def recommend_courses(self, student_info, analysis_results, pathway_results, count=3):
        """
        Recommends courses based on student profile and analysis results.
        
        Args:
            student_info (dict): Student information including age
            analysis_results (dict): Results from the learning style analysis
            pathway_results (dict): Results from the learning pathway mapping
            count (int): Number of courses to recommend
            
        Returns:
            list: Recommended courses
        """
        # Extract key information from analysis results
        primary_learning_style = analysis_results["learning_styles"]["primary"]
        secondary_learning_styles = analysis_results["learning_styles"]["secondary"]
        top_traits = analysis_results["traits"]["top_traits"]
        top_interests = analysis_results["interests"]["top_interests"]
        student_age = student_info["age"]
        
        # Get primary and secondary categories from pathway results
        primary_category = pathway_results["primary_category"]
        secondary_category = pathway_results["secondary_category"]
        
        # Collect all potential courses
        potential_courses = []
        
        # Add courses from primary category
        if primary_category in self.courses:
            potential_courses.extend(self.courses[primary_category])
        
        # Add courses from secondary category
        if secondary_category in self.courses and secondary_category != primary_category:
            potential_courses.extend(self.courses[secondary_category])
        
        # Add courses from other categories based on interests
        for interest in top_interests:
            if interest in self.courses and interest != primary_category and interest != secondary_category:
                potential_courses.extend(self.courses[interest])
        
        # Filter courses by age appropriateness
        age_appropriate_courses = []
        for course in potential_courses:
            age_range = course.get("age_range", "")
            if "-" in age_range:
                min_age, max_age = map(int, age_range.split("-"))
                if min_age <= student_age <= max_age:
                    age_appropriate_courses.append(course)
        
        # If no age-appropriate courses, use all potential courses
        if not age_appropriate_courses:
            age_appropriate_courses = potential_courses
        
        # Score each course based on fit with student profile
        scored_courses = []
        for course in age_appropriate_courses:
            score = self._calculate_course_fit_score(
                course, 
                primary_learning_style, 
                secondary_learning_styles, 
                top_traits, 
                top_interests
            )
            scored_courses.append((course, score))
        
        # Sort courses by score (descending)
        scored_courses.sort(key=lambda x: x[1], reverse=True)
        
        # Get top courses
        top_courses = [course for course, _ in scored_courses[:count]]
        
        # Ensure we have enough recommendations
        if len(top_courses) < count:
            # Add courses from any category based on popularity
            all_courses = []
            for category in self.courses:
                all_courses.extend(self.courses[category])
            
            # Filter by age and exclude already recommended courses
            additional_courses = []
            for course in all_courses:
                if course not in top_courses:
                    age_range = course.get("age_range", "")
                    if "-" in age_range:
                        min_age, max_age = map(int, age_range.split("-"))
                        if min_age <= student_age <= max_age:
                            additional_courses.append(course)
            
            # Sort by popularity
            additional_courses.sort(key=lambda x: x.get("popularity", 0), reverse=True)
            
            # Add enough to reach the requested count
            top_courses.extend(additional_courses[:count - len(top_courses)])
        
        # Add personalized benefit statements
        for course in top_courses:
            course["personalized_benefit"] = self._generate_personalized_benefit(
                course, 
                primary_learning_style, 
                top_traits, 
                top_interests
            )
        
        return top_courses
    
    def _calculate_course_fit_score(self, course, primary_style, secondary_styles, traits, interests):
        """
        Calculates a fit score for a course based on student profile.
        
        Args:
            course (dict): Course information
            primary_style (str): Student's primary learning style
            secondary_styles (list): Student's secondary learning styles
            traits (list): Student's top traits
            interests (list): Student's top interests
            
        Returns:
            float: Fit score (0-100)
        """
        score = 0
        
        # Score based on learning style match (max 40 points)
        course_styles = course.get("learning_styles", [])
        if primary_style in course_styles:
            score += 30  # Primary style match
        
        for style in secondary_styles:
            if style in course_styles:
                score += 5  # Secondary style match (max 10 points)
        
        # Score based on trait match (max 30 points)
        course_traits = course.get("traits", [])
        for i, trait in enumerate(traits[:3]):
            if trait in course_traits:
                score += 10 - (i * 3)  # 10 points for first trait, 7 for second, 4 for third
        
        # Score based on category/interest match (max 20 points)
        course_id = course.get("id", "")
        course_category = None
        for category in self.courses:
            if any(c.get("id") == course_id for c in self.courses[category]):
                course_category = category
                break
        
        if course_category in interests[:1]:
            score += 20  # Top interest match
        elif course_category in interests[1:2]:
            score += 15  # Second interest match
        elif course_category in interests[2:]:
            score += 10  # Other interest match
        
        # Score based on popularity (max 10 points)
        popularity = course.get("popularity", 0)
        score += (popularity / 10)
        
        return score
    
    def _generate_personalized_benefit(self, course, learning_style, traits, interests):
        """
        Generates a personalized benefit statement for a course.
        
        Args:
            course (dict): Course information
            learning_style (str): Student's primary learning style
            traits (list): Student's top traits
            interests (list): Student's top interests
            
        Returns:
            str: Personalized benefit statement
        """
        # Base benefit from course
        base_benefit = course.get("benefits", "")
        
        # Learning style specific benefit
        style_benefits = {
            "visual": "The visual elements and demonstrations in this course align perfectly with your visual learning style.",
            "auditory": "This course includes discussions and verbal explanations that match your auditory learning preference.",
            "kinesthetic": "You'll enjoy the hands-on activities in this course that suit your kinesthetic learning style.",
            "logical": "The structured approach of this course complements your logical learning style.",
            "social": "The collaborative aspects of this course are ideal for your social learning preference.",
            "independent": "This course offers opportunities for self-directed learning that match your independent style."
        }
        
        style_benefit = style_benefits.get(learning_style, "")
        
        # Trait specific benefit
        trait_benefits = {
            "creative": "Your creative thinking will be an asset in the innovative projects included in this course.",
            "analytical": "Your analytical abilities will help you excel in the problem-solving aspects of this course.",
            "persistent": "Your persistence will be valuable when tackling the challenging components of this course.",
            "leadership": "Your leadership qualities will shine in the group activities included in this course.",
            "collaborative": "Your collaborative nature will be beneficial in the team projects within this course.",
            "organized": "Your organizational skills will help you manage the various components of this course effectively."
        }
        
        trait_benefit = ""
        if traits and traits[0] in trait_benefits:
            trait_benefit = trait_benefits[traits[0]]
        
        # Combine benefits
        personalized_benefit = f"{base_benefit} {style_benefit}"
        
        if trait_benefit:
            personalized_benefit += f" {trait_benefit}"
        
        return personalized_benefit
