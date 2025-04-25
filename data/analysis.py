"""
Learning Style Analysis Algorithm
This module processes questionnaire responses to determine learning styles and traits.
"""

import numpy as np
from collections import Counter

# Learning style categories and their descriptions
LEARNING_STYLES = {
    "visual": {
        "name": "Visual Learner",
        "description": "Learns best through seeing information, including pictures, diagrams, and written instructions.",
        "strategies": [
            "Use visual aids like charts, maps, and diagrams",
            "Highlight important information in notes",
            "Watch educational videos and demonstrations",
            "Create mind maps to organize information"
        ],
        "ideal_environment": "Well-organized, visually stimulating spaces with minimal visual distractions."
    },
    "auditory": {
        "name": "Auditory Learner",
        "description": "Learns best through listening to information, including lectures, discussions, and verbal instructions.",
        "strategies": [
            "Record and listen to lectures or explanations",
            "Participate in group discussions",
            "Read information aloud",
            "Use mnemonic devices and rhymes"
        ],
        "ideal_environment": "Quiet spaces for concentration with opportunities for discussion and verbal processing."
    },
    "kinesthetic": {
        "name": "Kinesthetic Learner",
        "description": "Learns best through hands-on activities, physical movement, and practical experiences.",
        "strategies": [
            "Engage in hands-on experiments and activities",
            "Take frequent breaks to move around",
            "Use physical objects to represent concepts",
            "Apply learning to real-world situations"
        ],
        "ideal_environment": "Spaces that allow movement and hands-on activities with opportunities for experiential learning."
    },
    "logical": {
        "name": "Logical Learner",
        "description": "Learns best through reasoning, systems, and patterns, with a preference for structured information.",
        "strategies": [
            "Organize information into logical categories",
            "Look for patterns and relationships",
            "Break complex problems into steps",
            "Create systems and frameworks for understanding"
        ],
        "ideal_environment": "Structured environments with clear expectations and opportunities for analytical thinking."
    },
    "social": {
        "name": "Social Learner",
        "description": "Learns best through interaction with others, group work, and collaborative activities.",
        "strategies": [
            "Study with peers or in groups",
            "Discuss ideas and concepts with others",
            "Teach concepts to someone else",
            "Participate in collaborative projects"
        ],
        "ideal_environment": "Collaborative spaces that encourage interaction and group work."
    },
    "independent": {
        "name": "Independent Learner",
        "description": "Learns best through self-directed study, with a preference for working alone.",
        "strategies": [
            "Set personal learning goals",
            "Create individual study plans",
            "Seek resources for self-directed learning",
            "Reflect on personal progress"
        ],
        "ideal_environment": "Quiet, personal spaces with minimal distractions and opportunities for self-directed work."
    }
}

# Trait categories and their descriptions
TRAITS = {
    "creative": {
        "name": "Creative Thinker",
        "description": "Shows originality and imagination in approaching problems and tasks.",
        "strengths": [
            "Generating unique ideas and solutions",
            "Thinking outside conventional boundaries",
            "Making unexpected connections between concepts",
            "Expressing ideas in innovative ways"
        ]
    },
    "analytical": {
        "name": "Analytical Thinker",
        "description": "Excels at breaking down complex information and identifying patterns and relationships.",
        "strengths": [
            "Solving complex problems systematically",
            "Identifying logical patterns and inconsistencies",
            "Evaluating information critically",
            "Making decisions based on careful analysis"
        ]
    },
    "persistent": {
        "name": "Persistent Worker",
        "description": "Shows determination and resilience when facing challenges or setbacks.",
        "strengths": [
            "Maintaining focus on long-term goals",
            "Overcoming obstacles through sustained effort",
            "Continuing to try different approaches when initial attempts fail",
            "Showing patience with difficult tasks"
        ]
    },
    "leadership": {
        "name": "Natural Leader",
        "description": "Takes initiative in group settings and helps guide others toward goals.",
        "strengths": [
            "Organizing and directing group activities",
            "Motivating others to participate",
            "Taking responsibility for outcomes",
            "Communicating vision and goals effectively"
        ]
    },
    "collaborative": {
        "name": "Team Collaborator",
        "description": "Works effectively with others and contributes positively to group efforts.",
        "strengths": [
            "Sharing ideas and resources with others",
            "Listening to and incorporating different perspectives",
            "Supporting team members and building consensus",
            "Adapting to group dynamics"
        ]
    },
    "organized": {
        "name": "Organized Planner",
        "description": "Excels at planning, organizing, and managing time and resources effectively.",
        "strengths": [
            "Creating and following structured plans",
            "Managing time efficiently",
            "Keeping track of details and requirements",
            "Prioritizing tasks appropriately"
        ]
    }
}

# Interest areas and their descriptions
INTERESTS = {
    "tech": {
        "name": "Technology & Computing",
        "description": "Shows interest in computers, programming, robotics, and digital technologies.",
        "related_careers": [
            "Software Developer",
            "Robotics Engineer",
            "Data Scientist",
            "AI Specialist",
            "Game Designer"
        ],
        "shining_star_tracks": ["Coding Path", "Robotics Program", "AI & Machine Learning"]
    },
    "arts": {
        "name": "Creative Arts",
        "description": "Shows interest in visual arts, music, design, and creative expression.",
        "related_careers": [
            "Graphic Designer",
            "Digital Artist",
            "Multimedia Producer",
            "UX/UI Designer",
            "Creative Director"
        ],
        "shining_star_tracks": ["Digital Arts Program", "Creative Design Track", "Multimedia Production"]
    },
    "entrepreneurship": {
        "name": "Entrepreneurship & Business",
        "description": "Shows interest in business concepts, innovation, and entrepreneurial ventures.",
        "related_careers": [
            "Entrepreneur",
            "Business Consultant",
            "Marketing Specialist",
            "Product Manager",
            "Innovation Strategist"
        ],
        "shining_star_tracks": ["Young Entrepreneurs Program", "Business Innovation Track", "Leadership Academy"]
    },
    "science": {
        "name": "Scientific Research",
        "description": "Shows interest in scientific inquiry, experimentation, and discovery.",
        "related_careers": [
            "Research Scientist",
            "Environmental Specialist",
            "Biomedical Researcher",
            "Laboratory Technician",
            "Science Educator"
        ],
        "shining_star_tracks": ["Science Exploration Program", "Research Methods Track", "STEM Academy"]
    },
    "language": {
        "name": "Communication & Language",
        "description": "Shows interest in reading, writing, languages, and communication.",
        "related_careers": [
            "Content Creator",
            "Journalist",
            "Technical Writer",
            "Communications Specialist",
            "Digital Marketing Manager"
        ],
        "shining_star_tracks": ["Creative Writing Program", "Digital Communication Track", "Public Speaking Academy"]
    }
}

class LearningStyleAnalyzer:
    """
    Analyzes questionnaire responses to determine learning styles, traits, and interests.
    """
    
    def __init__(self):
        self.learning_styles = LEARNING_STYLES
        self.traits = TRAITS
        self.interests = INTERESTS
        
    def analyze_responses(self, responses, age):
        """
        Analyzes student responses to determine learning profile.
        
        Args:
            responses (dict): Dictionary of question IDs and selected answers
            age (int): Age of the student
            
        Returns:
            dict: Analysis results including learning styles, traits, and interests
        """
        # Initialize counters for different categories
        learning_style_counts = Counter()
        trait_counts = Counter()
        interest_counts = Counter()
        
        # Process each response
        for question_id, answer_index in responses.items():
            # Find the question in the questionnaire
            question = self._find_question(question_id, age)
            
            if not question:
                continue
                
            # Process based on question category and type
            if question["category"] == "learning_style" and "learning_style_mapping" in question:
                learning_style = question["learning_style_mapping"][answer_index]
                learning_style_counts[learning_style] += 1
                
            elif "trait_mapping" in question:
                if isinstance(question["trait_mapping"], list) and len(question["trait_mapping"]) > answer_index:
                    trait = question["trait_mapping"][answer_index]
                    trait_counts[trait] += 1
                elif isinstance(question["trait_mapping"], str):
                    # For questions with a single trait mapping
                    trait_counts[question["trait_mapping"]] += 1
                    
            elif "interest_mapping" in question and len(question["interest_mapping"]) > answer_index:
                interest = question["interest_mapping"][answer_index]
                interest_counts[interest] += 1
        
        # Determine primary and secondary learning styles
        primary_learning_style = learning_style_counts.most_common(1)[0][0] if learning_style_counts else "visual"
        secondary_learning_styles = [style for style, _ in learning_style_counts.most_common(3)[1:3]] if len(learning_style_counts) > 1 else []
        
        # Determine top traits
        top_traits = [trait for trait, _ in trait_counts.most_common(3)]
        
        # Determine top interests
        top_interests = [interest for interest, _ in interest_counts.most_common(3)]
        
        # Calculate scores for different dimensions (normalized to 0-100)
        total_questions = len(responses)
        
        # Calculate dimension scores
        dimension_scores = {
            "logical_thinking": self._calculate_dimension_score(responses, ["ps_1", "mid_2", "high_2"], total_questions),
            "creativity": self._calculate_dimension_score(responses, ["cr_1", "elem_3", "mid_3", "high_3"], total_questions),
            "social_skills": self._calculate_dimension_score(responses, ["ls_3", "mid_6", "high_6"], total_questions),
            "self_direction": self._calculate_dimension_score(responses, ["bh_1", "tm_1", "high_4"], total_questions)
        }
        
        # Prepare the analysis results
        results = {
            "learning_styles": {
                "primary": primary_learning_style,
                "secondary": secondary_learning_styles,
                "description": self.learning_styles[primary_learning_style]["description"],
                "strategies": self.learning_styles[primary_learning_style]["strategies"],
                "ideal_environment": self.learning_styles[primary_learning_style]["ideal_environment"]
            },
            "traits": {
                "top_traits": top_traits,
                "descriptions": [self.traits[trait]["description"] if trait in self.traits else "" for trait in top_traits],
                "strengths": [self.traits[trait]["strengths"] if trait in self.traits else [] for trait in top_traits]
            },
            "interests": {
                "top_interests": top_interests,
                "descriptions": [self.interests[interest]["description"] if interest in self.interests else "" for interest in top_interests],
                "related_careers": [self.interests[interest]["related_careers"] if interest in self.interests else [] for interest in top_interests],
                "shining_star_tracks": [self.interests[interest]["shining_star_tracks"] if interest in self.interests else [] for interest in top_interests]
            },
            "dimension_scores": dimension_scores
        }
        
        return results
    
    def compare_parent_responses(self, parent_responses, student_results):
        """
        Compares parent responses with student results to identify alignments and differences.
        
        Args:
            parent_responses (dict): Dictionary of parent question IDs and selected answers
            student_results (dict): Student analysis results
            
        Returns:
            dict: Comparison results highlighting alignments and differences
        """
        # Initialize comparison results
        comparison = {
            "alignments": [],
            "differences": [],
            "insights": []
        }
        
        # Extract parent perceptions
        parent_learning_style = None
        parent_traits = []
        parent_interests = []
        
        for question_id, answer_index in parent_responses.items():
            # Find the parent question
            question = self._find_parent_question(question_id)
            
            if not question:
                continue
                
            if question["category"] == "learning_style" and "learning_style_mapping" in question:
                parent_learning_style = question["learning_style_mapping"][answer_index]
                
            elif "trait_mapping" in question:
                parent_traits.append(question["trait_mapping"][answer_index])
                
            elif "interest_mapping" in question:
                parent_interests.append(question["interest_mapping"][answer_index])
        
        # Compare learning styles
        student_learning_style = student_results["learning_styles"]["primary"]
        if parent_learning_style == student_learning_style:
            comparison["alignments"].append(f"You both identified a preference for {self.learning_styles[student_learning_style]['name']} learning.")
        else:
            comparison["differences"].append(
                f"You identified your child as a {self.learning_styles[parent_learning_style]['name'] if parent_learning_style in self.learning_styles else 'different type of learner'}, "
                f"but their responses indicate they are a {self.learning_styles[student_learning_style]['name']}."
            )
            comparison["insights"].append(
                f"Consider providing more opportunities for {self.learning_styles[student_learning_style]['name'].lower()} learning experiences."
            )
        
        # Compare traits
        student_traits = student_results["traits"]["top_traits"]
        for trait in parent_traits:
            if trait in student_traits:
                comparison["alignments"].append(f"You both recognized the {self.traits[trait]['name'].lower() if trait in self.traits else trait} trait.")
            else:
                comparison["differences"].append(
                    f"You identified your child as a {self.traits[trait]['name'].lower() if trait in self.traits else trait}, "
                    f"but this wasn't among their top traits in the assessment."
                )
        
        # Compare interests
        student_interests = student_results["interests"]["top_interests"]
        for interest in parent_interests:
            if interest in student_interests:
                comparison["alignments"].append(f"You both identified an interest in {self.interests[interest]['name'].lower() if interest in self.interests else interest}.")
            else:
                comparison["differences"].append(
                    f"You identified an interest in {self.interests[interest]['name'].lower() if interest in self.interests else interest}, "
                    f"but this wasn't among their top interests in the assessment."
                )
                comparison["insights"].append(
                    f"Your child may benefit from exploring their expressed interests in {', '.join([self.interests[i]['name'].lower() if i in self.interests else i for i in student_interests[:2]])}."
                )
        
        return comparison
    
    def _find_question(self, question_id, age):
        """
        Finds a question by ID in the appropriate age group.
        
        Args:
            question_id (str): Question ID
            age (int): Student age
            
        Returns:
            dict: Question dictionary or None if not found
        """
        from data.questionnaire import get_questions_for_age
        
        questions = get_questions_for_age(age)
        for question in questions:
            if question["id"] == question_id:
                return question
        
        return None
    
    def _find_parent_question(self, question_id):
        """
        Finds a parent question by ID.
        
        Args:
            question_id (str): Question ID
            
        Returns:
            dict: Question dictionary or None if not found
        """
        from data.questionnaire import get_parent_questions
        
        questions = get_parent_questions()
        for question in questions:
            if question["id"] == question_id:
                return question
        
        return None
    
    def _calculate_dimension_score(self, responses, relevant_question_ids, total_questions):
        """
        Calculates a normalized score for a specific dimension.
        
        Args:
            responses (dict): Dictionary of question IDs and selected answers
            relevant_question_ids (list): List of question IDs relevant to this dimension
            total_questions (int): Total number of questions answered
            
        Returns:
            int: Normalized score (0-100)
        """
        # Count positive responses for this dimension
        positive_count = 0
        max_possible = 0
        
        for q_id in relevant_question_ids:
            if q_id in responses:
                answer_index = responses[q_id]
                # For simplicity, consider first two options as lower scores, last two as higher scores
                if answer_index >= 2:  # Third or fourth option selected
                    positive_count += 1
                max_possible += 1
        
        # Normalize to 0-100 scale
        if max_possible == 0:
            return 50  # Default middle value if no relevant questions were answered
            
        return int((positive_count / max_possible) * 100)

def generate_learning_badges(results):
    """
    Generates gamified badges based on learning profile results.
    
    Args:
        results (dict): Analysis results
        
    Returns:
        dict: Badge information including title, description, and icon
    """
    # Determine primary badge based on combination of learning style and top traits/interests
    primary_style = results["learning_styles"]["primary"]
    top_traits = results["traits"]["top_traits"]
    top_interests = results["interests"]["top_interests"]
    
    badges = {
        # Learning style based badges
        "visual": {
            "title": "Visual Virtuoso",
            "description": "You excel at processing visual information and thinking in pictures.",
            "icon": "👁️"
        },
        "auditory": {
            "title": "Sound Sage",
            "description": "You have a gift for processing and remembering what you hear.",
            "icon": "👂"
        },
        "kinesthetic": {
            "title": "Hands-On Hero",
            "description": "You learn best through physical activity and practical experience.",
            "icon": "✋"
        },
        "logical": {
            "title": "Logic Legend",
            "description": "You excel at systematic thinking and solving complex problems.",
            "icon": "🔢"
        },
        "social": {
            "title": "Team Tactician",
            "description": "You thrive in collaborative environments and group learning.",
            "icon": "👥"
        },
        "independent": {
            "title": "Solo Scholar",
            "description": "You excel at self-directed learning and independent study.",
            "icon": "🧠"
        },
        
        # Trait based badges
        "creative": {
            "title": "Creative Genius",
            "description": "Your imagination and innovative thinking set you apart.",
            "icon": "💡"
        },
        "analytical": {
            "title": "Analytical Ace",
            "description": "Your ability to break down complex problems is exceptional.",
            "icon": "🔍"
        },
        "persistent": {
            "title": "Persistence Pro",
            "description": "Your determination helps you overcome challenges.",
            "icon": "🏆"
        },
        "leadership": {
            "title": "Born Leader",
            "description": "You naturally take charge and inspire others.",
            "icon": "👑"
        },
        
        # Interest based badges
        "tech": {
            "title": "Tech Wizard",
            "description": "Your affinity for technology and computing shines through.",
            "icon": "💻"
        },
        "arts": {
            "title": "Creative Visionary",
            "description": "Your artistic talents and creative expression are remarkable.",
            "icon": "🎨"
        },
        "entrepreneurship": {
            "title": "Future Founder",
            "description": "Your business sense and innovative ideas show entrepreneurial promise.",
            "icon": "💼"
        },
        "science": {
            "title": "Science Explorer",
            "description": "Your curiosity and analytical approach make you a natural scientist.",
            "icon": "🔬"
        },
        "language": {
            "title": "Word Weaver",
            "description": "Your communication skills and language abilities are outstanding.",
            "icon": "📚"
        }
    }
    
    # Select primary badge based on learning style
    primary_badge = badges[primary_style]
    
    # Select secondary badges based on top traits and interests
    secondary_badges = []
    
    # Add trait badge if available
    if top_traits and top_traits[0] in badges:
        secondary_badges.append(badges[top_traits[0]])
    
    # Add interest badge if available
    if top_interests and top_interests[0] in badges:
        secondary_badges.append(badges[top_interests[0]])
    
    # Create special combination badges for certain profiles
    combination_badges = []
    
    # Check for special combinations
    if primary_style == "logical" and "tech" in top_interests:
        combination_badges.append({
            "title": "Code Commander",
            "description": "Your logical thinking and tech interests make you a natural programmer.",
            "icon": "⌨️"
        })
    
    if primary_style == "visual" and "arts" in top_interests:
        combination_badges.append({
            "title": "Design Dynamo",
            "description": "Your visual learning style and artistic interests make you a natural designer.",
            "icon": "🎭"
        })
    
    if "leadership" in top_traits and "entrepreneurship" in top_interests:
        combination_badges.append({
            "title": "Future CEO",
            "description": "Your leadership skills and business interests show executive potential.",
            "icon": "🚀"
        })
    
    if "creative" in top_traits and "tech" in top_interests:
        combination_badges.append({
            "title": "Innovation Architect",
            "description": "Your creativity and tech interests make you a natural innovator.",
            "icon": "🔮"
        })
    
    return {
        "primary_badge": primary_badge,
        "secondary_badges": secondary_badges,
        "combination_badges": combination_badges
    }
