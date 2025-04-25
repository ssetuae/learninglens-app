"""
Career Affinity Module
This module suggests potential future careers based on student profiles.
"""

class CareerAffinityAdvisor:
    """
    Suggests potential future careers and college paths based on student analysis results.
    """
    
    def __init__(self):
        """
        Initialize the career affinity advisor with career data.
        """
        # Define career paths by category with descriptions and education paths
        self.career_paths = {
            "tech": {
                "title": "Technology & Computing",
                "description": "Careers focused on developing, implementing, and maintaining technology systems and software.",
                "careers": [
                    {
                        "title": "Software Developer",
                        "description": "Creates applications and systems that run on computers and other devices.",
                        "education_path": "Computer Science or Software Engineering degree, coding bootcamps, or self-taught with strong portfolio.",
                        "skills_needed": ["Programming", "Problem-solving", "Logical thinking", "Attention to detail"],
                        "growth_outlook": "Excellent growth prospects with increasing demand across industries."
                    },
                    {
                        "title": "AI & Machine Learning Specialist",
                        "description": "Develops systems that can learn from and make decisions based on data.",
                        "education_path": "Computer Science degree with specialization in AI/ML, often requires advanced degrees.",
                        "skills_needed": ["Programming", "Mathematics", "Data analysis", "Research skills"],
                        "growth_outlook": "One of the fastest-growing tech fields with applications expanding rapidly."
                    },
                    {
                        "title": "Robotics Engineer",
                        "description": "Designs, builds, and programs robots for various applications.",
                        "education_path": "Robotics, Mechanical Engineering, or Computer Science degree.",
                        "skills_needed": ["Programming", "Mechanical design", "Electronics", "Problem-solving"],
                        "growth_outlook": "Growing field with applications in manufacturing, healthcare, and consumer products."
                    },
                    {
                        "title": "Game Developer",
                        "description": "Creates video games for computers, consoles, and mobile devices.",
                        "education_path": "Game Development, Computer Science degree, or specialized training programs.",
                        "skills_needed": ["Programming", "Creativity", "Visual design", "Storytelling"],
                        "growth_outlook": "Steady growth in a competitive industry with opportunities in various game types."
                    },
                    {
                        "title": "Cybersecurity Specialist",
                        "description": "Protects computer systems and networks from threats and attacks.",
                        "education_path": "Cybersecurity or Computer Science degree, often with specialized certifications.",
                        "skills_needed": ["Security protocols", "Problem-solving", "Attention to detail", "Ethical hacking"],
                        "growth_outlook": "Critical and rapidly growing field with high demand across all sectors."
                    }
                ]
            },
            "arts": {
                "title": "Creative Arts & Design",
                "description": "Careers focused on visual communication, digital media, and artistic expression.",
                "careers": [
                    {
                        "title": "UX/UI Designer",
                        "description": "Designs user interfaces and experiences for websites, apps, and digital products.",
                        "education_path": "Design degree, UX certification programs, or self-taught with strong portfolio.",
                        "skills_needed": ["Visual design", "User empathy", "Prototyping", "Research skills"],
                        "growth_outlook": "Strong demand as digital products continue to prioritize user experience."
                    },
                    {
                        "title": "Digital Artist",
                        "description": "Creates visual art using digital tools and technologies.",
                        "education_path": "Fine Arts or Digital Arts degree, or self-taught with strong portfolio.",
                        "skills_needed": ["Creativity", "Visual composition", "Technical software skills", "Artistic vision"],
                        "growth_outlook": "Growing opportunities in entertainment, advertising, and digital media."
                    },
                    {
                        "title": "3D Animator",
                        "description": "Creates animated characters, environments, and effects for films, games, and media.",
                        "education_path": "Animation, Digital Arts degree, or specialized training programs.",
                        "skills_needed": ["3D modeling", "Animation principles", "Storytelling", "Technical software skills"],
                        "growth_outlook": "Continued growth in film, gaming, and emerging AR/VR applications."
                    },
                    {
                        "title": "Graphic Designer",
                        "description": "Creates visual concepts to communicate ideas through print and digital media.",
                        "education_path": "Graphic Design degree or certificate programs with portfolio development.",
                        "skills_needed": ["Visual design", "Typography", "Color theory", "Communication"],
                        "growth_outlook": "Steady demand across industries for both in-house and freelance designers."
                    },
                    {
                        "title": "Art Director",
                        "description": "Oversees visual style and creative elements of projects in various media.",
                        "education_path": "Design or Fine Arts degree, typically with several years of industry experience.",
                        "skills_needed": ["Leadership", "Visual design", "Project management", "Creative vision"],
                        "growth_outlook": "Senior-level position with opportunities in advertising, publishing, and entertainment."
                    }
                ]
            },
            "entrepreneurship": {
                "title": "Business & Entrepreneurship",
                "description": "Careers focused on creating, managing, and growing business ventures and organizations.",
                "careers": [
                    {
                        "title": "Entrepreneur/Startup Founder",
                        "description": "Creates and builds new businesses, products, or services.",
                        "education_path": "Business degree helpful but not required; many successful entrepreneurs come from diverse backgrounds.",
                        "skills_needed": ["Innovation", "Risk management", "Leadership", "Adaptability"],
                        "growth_outlook": "Always opportunities for innovative new ventures, though success rates vary widely."
                    },
                    {
                        "title": "Product Manager",
                        "description": "Oversees product development from conception to launch and beyond.",
                        "education_path": "Business, Engineering, or related degree, often with MBA for senior positions.",
                        "skills_needed": ["Strategic thinking", "User empathy", "Communication", "Data analysis"],
                        "growth_outlook": "High demand role, especially in technology and consumer product companies."
                    },
                    {
                        "title": "Marketing Specialist",
                        "description": "Develops and implements strategies to promote products and services.",
                        "education_path": "Marketing, Business, or Communications degree, often with specialized certifications.",
                        "skills_needed": ["Communication", "Creativity", "Data analysis", "Strategic thinking"],
                        "growth_outlook": "Evolving field with growing emphasis on digital marketing skills."
                    },
                    {
                        "title": "Business Consultant",
                        "description": "Advises businesses on improving performance, operations, and strategy.",
                        "education_path": "Business degree, often with MBA or specialized expertise in particular industries.",
                        "skills_needed": ["Problem-solving", "Analysis", "Communication", "Industry knowledge"],
                        "growth_outlook": "Consistent demand, especially for consultants with specialized expertise."
                    },
                    {
                        "title": "Innovation Strategist",
                        "description": "Develops strategies for organizations to innovate and stay competitive.",
                        "education_path": "Business, Design, or Engineering background, often with interdisciplinary experience.",
                        "skills_needed": ["Creative thinking", "Strategic planning", "Research", "Change management"],
                        "growth_outlook": "Growing field as companies increasingly prioritize innovation."
                    }
                ]
            },
            "science": {
                "title": "Scientific Research & Development",
                "description": "Careers focused on scientific inquiry, discovery, and application of knowledge.",
                "careers": [
                    {
                        "title": "Data Scientist",
                        "description": "Analyzes complex data to help organizations make better decisions.",
                        "education_path": "Statistics, Computer Science, or related field, often with advanced degrees.",
                        "skills_needed": ["Programming", "Statistics", "Machine learning", "Data visualization"],
                        "growth_outlook": "Rapidly growing field with applications across virtually all industries."
                    },
                    {
                        "title": "Research Scientist",
                        "description": "Conducts experiments and investigations to expand scientific knowledge.",
                        "education_path": "PhD in specific scientific field (Biology, Chemistry, Physics, etc.).",
                        "skills_needed": ["Research methods", "Critical thinking", "Technical writing", "Specialized knowledge"],
                        "growth_outlook": "Varies by field, with strongest growth in interdisciplinary and emerging areas."
                    },
                    {
                        "title": "Biomedical Engineer",
                        "description": "Develops devices and procedures that solve medical and health-related problems.",
                        "education_path": "Biomedical Engineering or related engineering degree.",
                        "skills_needed": ["Engineering principles", "Biology", "Problem-solving", "Design thinking"],
                        "growth_outlook": "Strong growth with aging population and advances in medical technology."
                    },
                    {
                        "title": "Environmental Scientist",
                        "description": "Studies environmental conditions and develops solutions to environmental problems.",
                        "education_path": "Environmental Science, Ecology, or related degree.",
                        "skills_needed": ["Research methods", "Data analysis", "Field work", "Communication"],
                        "growth_outlook": "Growing field as environmental concerns become increasingly important."
                    },
                    {
                        "title": "Biotechnologist",
                        "description": "Applies biological processes to develop new products and technologies.",
                        "education_path": "Biotechnology, Biology, or related degree, often with advanced degrees.",
                        "skills_needed": ["Laboratory techniques", "Research", "Problem-solving", "Innovation"],
                        "growth_outlook": "Expanding field with applications in medicine, agriculture, and industry."
                    }
                ]
            },
            "language": {
                "title": "Communication & Media",
                "description": "Careers focused on creating, managing, and sharing information and stories.",
                "careers": [
                    {
                        "title": "Content Creator",
                        "description": "Develops written, visual, or multimedia content for various platforms.",
                        "education_path": "Communications, Journalism, or related field, or self-taught with strong portfolio.",
                        "skills_needed": ["Writing", "Creativity", "Digital media", "Audience engagement"],
                        "growth_outlook": "Expanding opportunities with growth of digital platforms and content marketing."
                    },
                    {
                        "title": "Technical Writer",
                        "description": "Creates documentation that explains complex information in accessible ways.",
                        "education_path": "English, Communications, or technical field with strong writing skills.",
                        "skills_needed": ["Clear writing", "Research", "Information organization", "Subject knowledge"],
                        "growth_outlook": "Steady demand, especially in technology, healthcare, and engineering."
                    },
                    {
                        "title": "Digital Marketing Manager",
                        "description": "Oversees online marketing strategies and campaigns.",
                        "education_path": "Marketing, Communications, or Business degree, often with specialized certifications.",
                        "skills_needed": ["Digital platforms", "Analytics", "Content strategy", "Campaign management"],
                        "growth_outlook": "Strong growth as marketing continues to shift toward digital channels."
                    },
                    {
                        "title": "Public Relations Specialist",
                        "description": "Manages communication between organizations and the public.",
                        "education_path": "Public Relations, Communications, or Journalism degree.",
                        "skills_needed": ["Communication", "Media relations", "Writing", "Strategic thinking"],
                        "growth_outlook": "Steady demand with evolving focus on digital and social media skills."
                    },
                    {
                        "title": "UX Writer",
                        "description": "Creates the text that appears throughout digital interfaces.",
                        "education_path": "English, Communications, or Design background with specialized training.",
                        "skills_needed": ["Concise writing", "User empathy", "Information architecture", "Collaboration"],
                        "growth_outlook": "Growing specialty within UX design as companies focus on user experience."
                    }
                ]
            }
        }
        
        # Define college/education paths by interest area
        self.education_paths = {
            "tech": {
                "college_majors": [
                    "Computer Science",
                    "Software Engineering",
                    "Information Technology",
                    "Computer Engineering",
                    "Data Science"
                ],
                "alternative_paths": [
                    "Coding bootcamps",
                    "Technical certification programs",
                    "Self-directed learning with portfolio development",
                    "Apprenticeships in tech companies"
                ]
            },
            "arts": {
                "college_majors": [
                    "Graphic Design",
                    "Digital Media",
                    "Animation",
                    "Game Design",
                    "Interactive Media"
                ],
                "alternative_paths": [
                    "Design bootcamps",
                    "Portfolio development programs",
                    "Apprenticeships with established artists",
                    "Self-directed learning with online courses"
                ]
            },
            "entrepreneurship": {
                "college_majors": [
                    "Business Administration",
                    "Entrepreneurship",
                    "Marketing",
                    "Finance",
                    "International Business"
                ],
                "alternative_paths": [
                    "Startup incubators and accelerators",
                    "Business certificate programs",
                    "Mentorship with established entrepreneurs",
                    "Direct experience launching small ventures"
                ]
            },
            "science": {
                "college_majors": [
                    "Biology",
                    "Chemistry",
                    "Physics",
                    "Environmental Science",
                    "Biomedical Engineering"
                ],
                "alternative_paths": [
                    "Laboratory technician certification",
                    "Research assistant positions",
                    "Field research programs",
                    "Science communication programs"
                ]
            },
            "language": {
                "college_majors": [
                    "Communications",
                    "Journalism",
                    "English",
                    "Media Studies",
                    "Public Relations"
                ],
                "alternative_paths": [
                    "Content creation portfolios",
                    "Digital marketing certifications",
                    "Publishing internships",
                    "Self-publishing and platform building"
                ]
            }
        }
    
    def generate_career_affinities(self, analysis_results):
        """
        Generates career affinity suggestions based on student profile.
        
        Args:
            analysis_results (dict): Results from the learning style analysis
            
        Returns:
            dict: Career affinity suggestions
        """
        # Extract key information from analysis results
        primary_learning_style = analysis_results["learning_styles"]["primary"]
        top_traits = analysis_results["traits"]["top_traits"]
        top_interests = analysis_results["interests"]["top_interests"]
        
        # Determine primary and secondary career categories
        primary_category = self._determine_primary_category(top_interests, primary_learning_style, top_traits)
        secondary_categories = self._determine_secondary_categories(primary_category, top_interests, primary_learning_style, top_traits)
        
        # Select careers from primary category
        primary_careers = self._select_careers(primary_category, 3)
        
        # Select careers from secondary categories
        secondary_careers = []
        for category in secondary_categories[:2]:  # Limit to top 2 secondary categories
            secondary_careers.extend(self._select_careers(category, 1))
        
        # Get education paths
        education_paths = self._get_education_paths(primary_category, secondary_categories[0] if secondary_categories else None)
        
        # Create the career affinity suggestions
        affinities = {
            "primary_field": self.career_paths[primary_category]["title"],
            "primary_field_description": self.career_paths[primary_category]["description"],
            "primary_careers": primary_careers,
            "secondary_careers": secondary_careers,
            "education_paths": education_paths,
            "disclaimer": "These suggestions are based on your current interests and strengths. Your path may change as you grow and explore new areas. This is meant to inspire, not limit your options."
        }
        
        return affinities
    
    def _determine_primary_category(self, interests, learning_style, traits):
        """
        Determines the primary career category based on student profile.
        
        Args:
            interests (list): Student's top interests
            learning_style (str): Student's primary learning style
            traits (list): Student's top traits
            
        Returns:
            str: Primary career category
        """
        # First priority: use the top interest if available
        if interests and interests[0] in self.career_paths:
            return interests[0]
        
        # Second priority: use learning style mapping
        learning_style_mappings = {
            "visual": ["arts", "tech"],
            "auditory": ["language", "science"],
            "kinesthetic": ["tech", "science"],
            "logical": ["science", "tech"],
            "social": ["entrepreneurship", "language"],
            "independent": ["science", "arts"]
        }
        
        if learning_style in learning_style_mappings:
            style_categories = learning_style_mappings[learning_style]
            # Check if any of these categories match secondary interests
            if len(interests) > 1:
                for interest in interests[1:]:
                    if interest in style_categories:
                        return interest
            # Otherwise return the first mapped category
            return style_categories[0]
        
        # Third priority: use trait mapping
        trait_mappings = {
            "creative": ["arts", "language"],
            "analytical": ["science", "tech"],
            "persistent": ["tech", "science"],
            "leadership": ["entrepreneurship", "language"],
            "collaborative": ["entrepreneurship", "language"],
            "organized": ["science", "entrepreneurship"]
        }
        
        if traits and traits[0] in trait_mappings:
            return trait_mappings[traits[0]][0]
        
        # Default to tech as a fallback
        return "tech"
    
    def _determine_secondary_categories(self, primary_category, interests, learning_style, traits):
        """
        Determines secondary career categories that complement the primary category.
        
        Args:
            primary_category (str): The primary career category
            interests (list): Student's top interests
            learning_style (str): Student's primary learning style
            traits (list): Student's top traits
            
        Returns:
            list: Secondary career categories
        """
        secondary_categories = []
        
        # Add interests that aren't the primary category
        for interest in interests:
            if interest in self.career_paths and interest != primary_category and interest not in secondary_categories:
                secondary_categories.append(interest)
        
        # Add categories based on learning style
        learning_style_mappings = {
            "visual": ["arts", "tech"],
            "auditory": ["language", "science"],
            "kinesthetic": ["tech", "science"],
            "logical": ["science", "tech"],
            "social": ["entrepreneurship", "language"],
            "independent": ["science", "arts"]
        }
        
        if learning_style in learning_style_mappings:
            for category in learning_style_mappings[learning_style]:
                if category != primary_category and category not in secondary_categories:
                    secondary_categories.append(category)
        
        # Add categories based on traits
        trait_mappings = {
            "creative": ["arts", "language"],
            "analytical": ["science", "tech"],
            "persistent": ["tech", "science"],
            "leadership": ["entrepreneurship", "language"],
            "collaborative": ["entrepreneurship", "language"],
            "organized": ["science", "entrepreneurship"]
        }
        
        if traits:
            for trait in traits:
                if trait in trait_mappings:
                    for category in trait_mappings[trait]:
                        if category != primary_category and category not in secondary_categories:
                            secondary_categories.append(category)
        
        # Ensure we have at least one secondary category
        if not secondary_categories:
            for category in self.career_paths:
                if category != primary_category:
                    secondary_categories.append(category)
                    break
        
        return secondary_categories
    
    def _select_careers(self, category, count):
        """
        Selects a specified number of careers from a category.
        
        Args:
            category (str): Career category
            count (int): Number of careers to select
            
        Returns:
            list: Selected careers
        """
        if category not in self.career_paths:
            return []
            
        careers = self.career_paths[category]["careers"]
        return careers[:min(count, len(careers))]
    
    def _get_education_paths(self, primary_category, secondary_category=None):
        """
        Gets education path suggestions based on career categories.
        
        Args:
            primary_category (str): Primary career category
            secondary_category (str, optional): Secondary career category
            
        Returns:
            dict: Education path suggestions
        """
        education_paths = {
            "college_majors": [],
            "alternative_paths": [],
            "note": "Education paths are just one way to prepare for these careers. Many successful professionals combine formal education with practical experience and self-directed learning."
        }
        
        # Add paths from primary category
        if primary_category in self.education_paths:
            education_paths["college_majors"].extend(self.education_paths[primary_category]["college_majors"][:3])
            education_paths["alternative_paths"].extend(self.education_paths[primary_category]["alternative_paths"][:2])
        
        # Add paths from secondary category
        if secondary_category and secondary_category in self.education_paths:
            education_paths["college_majors"].extend(self.education_paths[secondary_category]["college_majors"][:2])
            education_paths["alternative_paths"].extend(self.education_paths[secondary_category]["alternative_paths"][:1])
        
        return education_paths
