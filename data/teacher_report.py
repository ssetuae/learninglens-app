"""
Teacher Mirror Report Module
This module generates specialized reports for teachers with deeper academic insights.
"""

import os
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

class TeacherReportGenerator:
    """
    Generates specialized reports for teachers with deeper academic insights.
    """
    
    def __init__(self, templates_dir):
        """
        Initialize the teacher report generator.
        
        Args:
            templates_dir (str): Directory containing report templates
        """
        self.templates_dir = templates_dir
        self.env = Environment(loader=FileSystemLoader(templates_dir))
    
    def generate_teacher_report(self, student_info, analysis_results, parent_comparison, output_dir):
        """
        Generates a specialized teacher report with deeper academic insights.
        
        Args:
            student_info (dict): Student information
            analysis_results (dict): Results from learning style analysis
            parent_comparison (dict): Results from parent-student comparison
            output_dir (str): Directory to save the generated report
            
        Returns:
            str: Path to the generated HTML report
        """
        # Create template data with enhanced academic insights
        template_data = self._prepare_template_data(student_info, analysis_results, parent_comparison)
        
        # Render the template
        template = self.env.get_template('teacher_report.html')
        rendered_html = template.render(**template_data)
        
        # Save the rendered HTML
        os.makedirs(output_dir, exist_ok=True)
        report_filename = f"teacher_report_{student_info['id']}.html"
        report_path = os.path.join(output_dir, report_filename)
        
        with open(report_path, 'w') as f:
            f.write(rendered_html)
        
        return report_path
    
    def _prepare_template_data(self, student_info, analysis_results, parent_comparison):
        """
        Prepares template data with enhanced academic insights for teachers.
        
        Args:
            student_info (dict): Student information
            analysis_results (dict): Results from learning style analysis
            parent_comparison (dict): Results from parent-student comparison
            
        Returns:
            dict: Template data for the teacher report
        """
        # Extract basic information from analysis results
        learning_styles = analysis_results.get("learning_styles", {})
        traits = analysis_results.get("traits", {})
        interests = analysis_results.get("interests", {})
        
        # Generate academic insights specific for teachers
        academic_insights = self._generate_academic_insights(
            student_info,
            learning_styles,
            traits,
            interests
        )
        
        # Generate classroom strategies based on learning profile
        classroom_strategies = self._generate_classroom_strategies(
            learning_styles,
            traits
        )
        
        # Generate potential challenges and solutions
        challenges_solutions = self._generate_challenges_solutions(
            learning_styles,
            traits
        )
        
        # Generate academic strengths and growth areas
        strengths_growth = self._generate_strengths_growth_areas(
            learning_styles,
            traits,
            interests
        )
        
        # Generate parent alignment insights
        parent_alignment = self._generate_parent_alignment_insights(
            parent_comparison
        )
        
        # Generate mathematical aptitude assessment
        math_aptitude = self._generate_math_aptitude_assessment(
            analysis_results
        )
        
        # Generate examination readiness assessment
        exam_readiness = self._generate_exam_readiness(
            student_info,
            analysis_results
        )
        
        # Compile all data for the template
        template_data = {
            "student": student_info,
            "date": datetime.now().strftime("%B %d, %Y"),
            "report_id": f"TSSR-{datetime.now().strftime('%Y%m%d')}-{student_info['id']}",
            "learning_styles": learning_styles,
            "traits": traits,
            "interests": interests,
            "academic_insights": academic_insights,
            "classroom_strategies": classroom_strategies,
            "challenges_solutions": challenges_solutions,
            "strengths_growth": strengths_growth,
            "parent_alignment": parent_alignment,
            "math_aptitude": math_aptitude,
            "exam_readiness": exam_readiness
        }
        
        return template_data
    
    def _generate_academic_insights(self, student_info, learning_styles, traits, interests):
        """
        Generates academic insights specific for teachers.
        
        Args:
            student_info (dict): Student information
            learning_styles (dict): Learning style analysis results
            traits (dict): Personality traits analysis results
            interests (dict): Interest areas analysis results
            
        Returns:
            dict: Academic insights for teachers
        """
        # Extract primary learning style and traits
        primary_style = learning_styles.get("primary", "")
        secondary_styles = learning_styles.get("secondary", [])
        top_traits = traits.get("top_traits", [])
        
        # Generate general academic approach
        academic_approach = self._get_academic_approach(primary_style, top_traits)
        
        # Generate subject affinities based on learning style and interests
        subject_affinities = self._get_subject_affinities(
            primary_style,
            secondary_styles,
            interests.get("top_interests", [])
        )
        
        # Generate learning pace and depth insights
        learning_pace = self._get_learning_pace(primary_style, top_traits)
        
        # Generate attention span and focus insights
        attention_focus = self._get_attention_focus(primary_style, top_traits)
        
        # Generate group work dynamics
        group_dynamics = self._get_group_dynamics(primary_style, top_traits)
        
        # Generate assessment preferences
        assessment_preferences = self._get_assessment_preferences(primary_style, top_traits)
        
        # Compile academic insights
        academic_insights = {
            "academic_approach": academic_approach,
            "subject_affinities": subject_affinities,
            "learning_pace": learning_pace,
            "attention_focus": attention_focus,
            "group_dynamics": group_dynamics,
            "assessment_preferences": assessment_preferences
        }
        
        return academic_insights
    
    def _get_academic_approach(self, primary_style, top_traits):
        """
        Determines the student's general academic approach.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            str: Description of academic approach
        """
        approaches = {
            "visual": "Tends to understand and remember concepts through visual representations. " +
                     "Responds well to diagrams, charts, and written instructions.",
            "auditory": "Processes information effectively through listening and discussion. " +
                       "Benefits from verbal explanations and group discussions.",
            "kinesthetic": "Learns best through hands-on activities and physical engagement. " +
                          "May struggle with long periods of sitting still.",
            "logical": "Excels in systematic and logical problem-solving. " +
                      "Appreciates clear structures and sequential learning.",
            "social": "Thrives in collaborative learning environments. " +
                     "Benefits from group projects and peer teaching opportunities.",
            "independent": "Works well independently and is self-directed. " +
                          "May need less direct supervision but benefits from clear expectations."
        }
        
        # Get base approach from primary learning style
        approach = approaches.get(primary_style, "Shows a balanced approach to learning.")
        
        # Modify based on top traits
        if "analytical" in top_traits:
            approach += " Shows strong analytical thinking and attention to detail."
        if "creative" in top_traits:
            approach += " Demonstrates creative thinking and novel approaches to problems."
        if "persistent" in top_traits:
            approach += " Exhibits persistence when facing challenging material."
        if "organized" in top_traits:
            approach += " Maintains good organization of materials and assignments."
        
        return approach
    
    def _get_subject_affinities(self, primary_style, secondary_styles, interests):
        """
        Determines subject affinities based on learning style and interests.
        
        Args:
            primary_style (str): Primary learning style
            secondary_styles (list): Secondary learning styles
            interests (list): Top interest areas
            
        Returns:
            dict: Subject affinities with strengths and potential challenges
        """
        # Define subject affinities by learning style
        style_affinities = {
            "visual": {
                "strengths": ["Art", "Geography", "Geometry", "Biology (diagrams)"],
                "challenges": ["Abstract concepts without visual aids", "Purely auditory lectures"]
            },
            "auditory": {
                "strengths": ["Languages", "Music", "History", "Literature"],
                "challenges": ["Complex visual diagrams", "Silent reading comprehension"]
            },
            "kinesthetic": {
                "strengths": ["Physical Education", "Chemistry (labs)", "Engineering", "Drama"],
                "challenges": ["Long lectures", "Extended writing assignments"]
            },
            "logical": {
                "strengths": ["Mathematics", "Physics", "Computer Science", "Chess"],
                "challenges": ["Creative writing", "Abstract art interpretation"]
            },
            "social": {
                "strengths": ["Group projects", "Debate", "Team sports", "Social studies"],
                "challenges": ["Independent research", "Individual assessments"]
            },
            "independent": {
                "strengths": ["Research projects", "Creative writing", "Self-paced subjects"],
                "challenges": ["Group presentations", "Team-based assessments"]
            }
        }
        
        # Get primary style affinities
        affinities = {
            "strengths": style_affinities.get(primary_style, {}).get("strengths", []),
            "challenges": style_affinities.get(primary_style, {}).get("challenges", [])
        }
        
        # Add secondary style strengths (but not challenges)
        for style in secondary_styles:
            if style in style_affinities:
                affinities["strengths"].extend(style_affinities[style].get("strengths", [])[:2])
        
        # Add interest-based subjects
        interest_subjects = {
            "technology": ["Computer Science", "Digital Media", "Robotics"],
            "arts": ["Visual Arts", "Music", "Drama", "Creative Writing"],
            "entrepreneurship": ["Business Studies", "Economics", "Public Speaking"],
            "science": ["Biology", "Chemistry", "Physics", "Environmental Science"],
            "language": ["Literature", "Foreign Languages", "Journalism"],
            "mathematics": ["Algebra", "Geometry", "Calculus", "Statistics"]
        }
        
        for interest in interests:
            if interest in interest_subjects:
                affinities["strengths"].extend(interest_subjects[interest][:2])
        
        # Remove duplicates
        affinities["strengths"] = list(dict.fromkeys(affinities["strengths"]))
        affinities["challenges"] = list(dict.fromkeys(affinities["challenges"]))
        
        return affinities
    
    def _get_learning_pace(self, primary_style, top_traits):
        """
        Determines the student's learning pace and depth preferences.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            dict: Learning pace insights
        """
        # Base pace by learning style
        pace_by_style = {
            "visual": "Moderate; needs time to process visual information thoroughly",
            "auditory": "Variable; can process verbal information quickly but may need time for reflection",
            "kinesthetic": "Hands-on pace; learns quickly through direct experience",
            "logical": "Methodical; prefers to understand concepts deeply before moving on",
            "social": "Adaptive; pace often influenced by group dynamics",
            "independent": "Self-regulated; may move quickly through familiar material and slower through challenging concepts"
        }
        
        # Depth preferences by traits
        depth_by_traits = {
            "analytical": "Prefers deep exploration of topics with attention to details and connections",
            "creative": "Enjoys exploring novel aspects and unconventional applications of concepts",
            "persistent": "Will work through difficult material thoroughly; doesn't give up easily",
            "leadership": "May focus more on broad understanding than details; sees big picture",
            "collaborative": "Benefits from discussing concepts in depth with peers",
            "organized": "Systematic in approaching new material; builds comprehensive understanding"
        }
        
        # Get base pace
        pace = pace_by_style.get(primary_style, "Moderate and balanced learning pace")
        
        # Get depth preference based on top trait
        depth = "Shows balanced interest in both breadth and depth of material"
        if top_traits and top_traits[0] in depth_by_traits:
            depth = depth_by_traits[top_traits[0]]
        
        return {
            "pace": pace,
            "depth": depth
        }
    
    def _get_attention_focus(self, primary_style, top_traits):
        """
        Determines the student's attention span and focus characteristics.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            dict: Attention and focus insights
        """
        # Attention characteristics by learning style
        attention_by_style = {
            "visual": "Strong visual focus; may lose attention during long verbal explanations",
            "auditory": "Good auditory attention; may struggle with focus in noisy environments",
            "kinesthetic": "May fidget during passive learning; excellent focus during hands-on activities",
            "logical": "Strong focus for logical problems; may disengage from unstructured activities",
            "social": "Attention enhanced in social learning contexts; may be distracted in isolated work",
            "independent": "Generally good self-directed focus; may tune out during group activities"
        }
        
        # Focus duration by traits
        focus_by_traits = {
            "analytical": "Can maintain extended focus on complex problems",
            "creative": "May have variable focus; intense concentration on interesting topics",
            "persistent": "Strong sustained focus, especially when challenged",
            "leadership": "Good focus when leading or engaged; may disengage when passive",
            "collaborative": "Focus enhanced in collaborative settings",
            "organized": "Methodical focus; good at managing attention across multiple tasks"
        }
        
        # Get attention characteristics
        attention = attention_by_style.get(primary_style, "Shows typical attention patterns for age")
        
        # Get focus duration based on top trait
        focus = "Shows age-appropriate focus duration"
        if top_traits and top_traits[0] in focus_by_traits:
            focus = focus_by_traits[top_traits[0]]
        
        # Compile strategies
        strategies = [
            "Break complex tasks into smaller segments",
            "Provide clear transitions between activities",
            "Use learning style-aligned engagement techniques",
            "Offer periodic movement breaks"
        ]
        
        return {
            "characteristics": attention,
            "duration": focus,
            "strategies": strategies
        }
    
    def _get_group_dynamics(self, primary_style, top_traits):
        """
        Determines the student's group work dynamics.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            dict: Group dynamics insights
        """
        # Role preferences by learning style
        role_by_style = {
            "visual": "May excel at creating visual representations for the group",
            "auditory": "Often effective at verbal presentations and discussions",
            "kinesthetic": "Prefers active roles in group activities",
            "logical": "Naturally takes on problem-solving and planning roles",
            "social": "Thrives in collaborative settings; often helps maintain group cohesion",
            "independent": "May prefer defined individual contributions within group projects"
        }
        
        # Collaboration style by traits
        collab_by_traits = {
            "analytical": "Contributes through careful analysis and attention to detail",
            "creative": "Offers innovative ideas and unconventional approaches",
            "persistent": "Helps keep the group on task and working through challenges",
            "leadership": "Naturally assumes leadership or coordination roles",
            "collaborative": "Excels at fostering cooperation and inclusive participation",
            "organized": "Often manages project organization and timeline adherence"
        }
        
        # Get role preference
        role = role_by_style.get(primary_style, "Adapts to various roles in group settings")
        
        # Get collaboration style based on top trait
        collab = "Shows balanced collaboration style"
        if top_traits and top_traits[0] in collab_by_traits:
            collab = collab_by_traits[top_traits[0]]
        
        # Determine optimal group size and composition
        if primary_style in ["social", "auditory"]:
            group_size = "Thrives in medium to large groups (4-6 students)"
        elif primary_style in ["independent", "logical"]:
            group_size = "Works best in smaller groups (2-3 students)"
        else:
            group_size = "Adapts well to various group sizes"
        
        if "leadership" in top_traits:
            composition = "Benefits from groups where leadership opportunities exist"
        elif "collaborative" in top_traits:
            composition = "Thrives in groups with cooperative dynamics"
        elif "analytical" in top_traits or "organized" in top_traits:
            composition = "Works well in groups with clear role definitions"
        else:
            composition = "Adapts to various group compositions"
        
        return {
            "role_preference": role,
            "collaboration_style": collab,
            "optimal_group_size": group_size,
            "optimal_composition": composition
        }
    
    def _get_assessment_preferences(self, primary_style, top_traits):
        """
        Determines the student's assessment preferences.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            dict: Assessment preferences insights
        """
        # Preferred assessment types by learning style
        assessment_by_style = {
            "visual": ["Visual projects", "Diagram creation", "Written exams with visual components"],
            "auditory": ["Oral presentations", "Debates", "Audio/video projects"],
            "kinesthetic": ["Hands-on demonstrations", "Role-playing", "Model building"],
            "logical": ["Problem-solving tasks", "Logical reasoning tests", "Structured projects"],
            "social": ["Group presentations", "Collaborative projects", "Peer teaching"],
            "independent": ["Research papers", "Individual projects", "Self-assessments"]
        }
        
        # Assessment approach by traits
        approach_by_traits = {
            "analytical": "Methodical and detail-oriented approach to assessments",
            "creative": "Brings creative elements to assessments; may excel with open-ended formats",
            "persistent": "Thorough in preparation; perseveres through challenging assessments",
            "leadership": "Confident in presentation-based assessments; may rush through details",
            "collaborative": "Performs well in group assessments; may need encouragement for individual work",
            "organized": "Well-prepared and structured approach to assessments"
        }
        
        # Get preferred assessment types
        preferred = assessment_by_style.get(primary_style, ["Mixed assessment types"])
        
        # Get challenging assessment types (opposite of preferred)
        challenging_map = {
            "visual": ["Pure auditory assessments", "Extended essays without visual aids"],
            "auditory": ["Silent reading comprehension", "Complex visual analysis"],
            "kinesthetic": ["Extended written exams", "Passive listening assessments"],
            "logical": ["Unstructured creative tasks", "Subjective assessments"],
            "social": ["Individual timed tests", "Isolated research projects"],
            "independent": ["Group performance assessments", "Team-based evaluations"]
        }
        
        challenging = challenging_map.get(primary_style, ["Varies based on content"])
        
        # Get assessment approach based on top trait
        approach = "Balanced approach to assessments"
        if top_traits and top_traits[0] in approach_by_traits:
            approach = approach_by_traits[top_traits[0]]
        
        # Compile recommendations
        recommendations = [
            "Offer assessment options aligned with learning style when possible",
            "Provide clear rubrics and expectations",
            "Allow adequate preparation time",
            "Balance assessment types throughout the term"
        ]
        
        return {
            "preferred_types": preferred,
            "challenging_types": challenging,
            "approach": approach,
            "recommendations": recommendations
        }
    
    def _generate_classroom_strategies(self, learning_styles, traits):
        """
        Generates classroom strategies based on learning profile.
        
        Args:
            learning_styles (dict): Learning style analysis results
            traits (dict): Personality traits analysis results
            
        Returns:
            dict: Classroom strategies
        """
        primary_style = learning_styles.get("primary", "")
        top_traits = traits.get("top_traits", [])
        
        # Engagement strategies by learning style
        engagement_by_style = {
            "visual": [
                "Use visual aids, diagrams, and charts",
                "Provide written instructions alongside verbal ones",
                "Incorporate color-coding for organization",
                "Use graphic organizers for note-taking"
            ],
            "auditory": [
                "Incorporate discussions and verbal explanations",
                "Use audio recordings or read-alouds",
                "Encourage verbal summarization of concepts",
                "Implement think-pair-share activities"
            ],
            "kinesthetic": [
                "Incorporate hands-on activities and manipulatives",
                "Allow movement during learning when possible",
                "Use role-play and physical demonstrations",
                "Implement lab-style activities across subjects"
            ],
            "logical": [
                "Provide clear, sequential instructions",
                "Use problem-solving activities and puzzles",
                "Explain the reasoning behind concepts",
                "Incorporate pattern recognition activities"
            ],
            "social": [
                "Implement collaborative learning activities",
                "Use group discussions and projects",
                "Incorporate peer teaching opportunities",
                "Create interactive classroom experiences"
            ],
            "independent": [
                "Provide self-directed learning opportunities",
                "Allow for independent research projects",
                "Offer choice in assignments when possible",
                "Provide clear expectations for independent work"
            ]
        }
        
        # Motivation strategies by traits
        motivation_by_traits = {
            "analytical": [
                "Provide complex problems to analyze",
                "Offer opportunities to dive deep into topics",
                "Recognize attention to detail and thoroughness"
            ],
            "creative": [
                "Allow creative expression in assignments",
                "Provide open-ended project options",
                "Recognize and value unique approaches"
            ],
            "persistent": [
                "Acknowledge effort and perseverance",
                "Provide appropriately challenging material",
                "Celebrate progress and improvement"
            ],
            "leadership": [
                "Offer opportunities to lead small groups",
                "Provide classroom responsibilities",
                "Recognize positive influence on peers"
            ],
            "collaborative": [
                "Create meaningful collaborative experiences",
                "Recognize contributions to group success",
                "Provide opportunities to help peers"
            ],
            "organized": [
                "Recognize effective organization and planning",
                "Provide tools for organization (templates, planners)",
                "Acknowledge thorough and structured work"
            ]
        }
        
        # Get engagement strategies
        engagement = engagement_by_style.get(primary_style, [
            "Use varied instructional approaches",
            "Combine visual, auditory, and kinesthetic elements",
            "Provide both structured and open-ended activities",
            "Balance individual and group work"
        ])
        
        # Get motivation strategies based on top traits
        motivation = []
        for trait in top_traits[:2]:  # Use top two traits
            if trait in motivation_by_traits:
                motivation.extend(motivation_by_traits[trait])
        
        if not motivation:
            motivation = [
                "Provide specific, meaningful feedback",
                "Connect learning to real-world applications",
                "Celebrate achievements and progress"
            ]
        
        # Compile differentiation strategies
        differentiation = [
            "Adjust complexity of assignments based on readiness",
            "Provide extension activities for deeper exploration",
            "Offer multiple ways to demonstrate understanding",
            "Vary grouping strategies based on learning objectives"
        ]
        
        return {
            "engagement": engagement,
            "motivation": motivation,
            "differentiation": differentiation
        }
    
    def _generate_challenges_solutions(self, learning_styles, traits):
        """
        Generates potential challenges and solutions.
        
        Args:
            learning_styles (dict): Learning style analysis results
            traits (dict): Personality traits analysis results
            
        Returns:
            list: Challenges and solutions
        """
        primary_style = learning_styles.get("primary", "")
        top_traits = traits.get("top_traits", [])
        
        # Potential challenges by learning style
        challenges_by_style = {
            "visual": [
                {
                    "challenge": "May struggle with purely auditory instruction",
                    "solutions": [
                        "Provide visual supplements to verbal instruction",
                        "Allow time to create visual notes or diagrams",
                        "Use visual cues for important information"
                    ]
                },
                {
                    "challenge": "May miss details in verbal directions",
                    "solutions": [
                        "Provide written instructions for complex tasks",
                        "Check for understanding through visual confirmation",
                        "Use visual checklists for multi-step processes"
                    ]
                }
            ],
            "auditory": [
                {
                    "challenge": "May be distracted in noisy environments",
                    "solutions": [
                        "Provide quiet work spaces when possible",
                        "Use noise-cancelling headphones for independent work",
                        "Position away from high-traffic classroom areas"
                    ]
                },
                {
                    "challenge": "May struggle with complex visual information",
                    "solutions": [
                        "Provide verbal explanations of visual materials",
                        "Allow verbal processing of visual information",
                        "Break down visual information into smaller components"
                    ]
                }
            ],
            "kinesthetic": [
                {
                    "challenge": "May appear fidgety or restless during passive learning",
                    "solutions": [
                        "Incorporate movement breaks",
                        "Provide fidget tools when appropriate",
                        "Allow standing or alternative seating options"
                    ]
                },
                {
                    "challenge": "May rush through written work",
                    "solutions": [
                        "Break writing tasks into smaller segments",
                        "Incorporate physical elements into writing tasks",
                        "Provide clear structures for written assignments"
                    ]
                }
            ],
            "logical": [
                {
                    "challenge": "May question instructions or methods frequently",
                    "solutions": [
                        "Explain reasoning behind instructional decisions",
                        "Provide logical frameworks for activities",
                        "Allow time for questions and clarification"
                    ]
                },
                {
                    "challenge": "May struggle with creative or subjective tasks",
                    "solutions": [
                        "Provide clear criteria even for creative assignments",
                        "Break down creative processes into logical steps",
                        "Connect creative tasks to logical frameworks"
                    ]
                }
            ],
            "social": [
                {
                    "challenge": "May be chatty or distracted during independent work",
                    "solutions": [
                        "Provide clear expectations for quiet work time",
                        "Use visual timers for independent work periods",
                        "Balance independent work with collaborative opportunities"
                    ]
                },
                {
                    "challenge": "May rely too heavily on peers in group work",
                    "solutions": [
                        "Assign specific roles in group activities",
                        "Require individual accountability within group projects",
                        "Balance group work with individual assessments"
                    ]
                }
            ],
            "independent": [
                {
                    "challenge": "May resist group work or collaboration",
                    "solutions": [
                        "Provide clear individual roles within group projects",
                        "Start with pair work before larger groups",
                        "Explain the value of collaborative skills"
                    ]
                },
                {
                    "challenge": "May work too independently without seeking help",
                    "solutions": [
                        "Check in regularly during independent work",
                        "Teach explicit help-seeking strategies",
                        "Create safe opportunities to ask questions"
                    ]
                }
            ]
        }
        
        # Trait-based challenges
        challenges_by_traits = {
            "analytical": {
                "challenge": "May get caught in details and miss big picture",
                "solutions": [
                    "Help connect details to overarching concepts",
                    "Provide opportunities to synthesize information",
                    "Use graphic organizers to show relationships between concepts"
                ]
            },
            "creative": {
                "challenge": "May pursue tangential ideas during lessons",
                "solutions": [
                    "Provide creative outlets within structured activities",
                    "Allow time for creative exploration after core content",
                    "Help connect creative ideas back to learning objectives"
                ]
            },
            "persistent": {
                "challenge": "May become frustrated when not immediately successful",
                "solutions": [
                    "Normalize struggle as part of learning",
                    "Break challenging tasks into manageable steps",
                    "Recognize effort and perseverance, not just results"
                ]
            },
            "leadership": {
                "challenge": "May dominate group activities",
                "solutions": [
                    "Assign specific roles in group work",
                    "Teach collaborative leadership skills",
                    "Provide leadership opportunities in appropriate contexts"
                ]
            },
            "collaborative": {
                "challenge": "May prioritize social harmony over academic rigor",
                "solutions": [
                    "Set clear academic expectations for group work",
                    "Teach constructive academic discourse",
                    "Model how to respectfully challenge ideas"
                ]
            },
            "organized": {
                "challenge": "May become anxious when routines are disrupted",
                "solutions": [
                    "Provide advance notice of schedule changes",
                    "Teach flexibility strategies",
                    "Help develop adaptable organizational systems"
                ]
            }
        }
        
        # Get style-based challenges
        challenges = challenges_by_style.get(primary_style, [
            {
                "challenge": "May need varied instructional approaches",
                "solutions": [
                    "Use multi-modal instruction",
                    "Provide options for demonstrating understanding",
                    "Check for understanding in different ways"
                ]
            }
        ])
        
        # Add trait-based challenge if relevant
        if top_traits and top_traits[0] in challenges_by_traits:
            challenges.append(challenges_by_traits[top_traits[0]])
        
        return challenges
    
    def _generate_strengths_growth_areas(self, learning_styles, traits, interests):
        """
        Generates academic strengths and growth areas.
        
        Args:
            learning_styles (dict): Learning style analysis results
            traits (dict): Personality traits analysis results
            interests (dict): Interest areas analysis results
            
        Returns:
            dict: Strengths and growth areas
        """
        primary_style = learning_styles.get("primary", "")
        top_traits = traits.get("top_traits", [])
        top_interests = interests.get("top_interests", [])
        
        # Academic strengths by learning style
        strengths_by_style = {
            "visual": [
                "Processing and remembering visual information",
                "Creating visual representations of concepts",
                "Understanding spatial relationships",
                "Noticing visual patterns and details"
            ],
            "auditory": [
                "Processing verbal instructions",
                "Participating in discussions",
                "Remembering spoken information",
                "Verbal explanation of concepts"
            ],
            "kinesthetic": [
                "Hands-on learning activities",
                "Physical demonstrations of concepts",
                "Learning through movement and touch",
                "Applied and practical learning"
            ],
            "logical": [
                "Systematic problem-solving",
                "Recognizing patterns and relationships",
                "Sequential and organized thinking",
                "Abstract reasoning and analysis"
            ],
            "social": [
                "Collaborative learning",
                "Group discussions and projects",
                "Peer teaching and learning",
                "Communication and interpersonal skills"
            ],
            "independent": [
                "Self-directed learning",
                "Independent research and projects",
                "Setting and pursuing learning goals",
                "Focused individual work"
            ]
        }
        
        # Growth areas by learning style
        growth_by_style = {
            "visual": [
                "Processing information without visual aids",
                "Taking notes from verbal lectures",
                "Expressing ideas verbally",
                "Following multi-step verbal directions"
            ],
            "auditory": [
                "Processing complex visual information",
                "Creating visual representations",
                "Working for extended periods in silence",
                "Organizing information spatially"
            ],
            "kinesthetic": [
                "Sitting still for extended periods",
                "Abstract conceptual learning",
                "Traditional test-taking",
                "Detailed written work"
            ],
            "logical": [
                "Creative and open-ended tasks",
                "Subjective or ambiguous content",
                "Emotional or social aspects of learning",
                "Flexibility when approaches need to change"
            ],
            "social": [
                "Extended independent work",
                "Self-directed learning",
                "Focusing in social environments",
                "Individual assessment"
            ],
            "independent": [
                "Collaborative projects",
                "Group discussions and activities",
                "Seeking help when needed",
                "Sharing ideas in group settings"
            ]
        }
        
        # Get strengths based on learning style
        strengths = strengths_by_style.get(primary_style, [
            "Adaptable learning approach",
            "Processing information in multiple ways",
            "Balancing independent and collaborative work"
        ])
        
        # Add trait-based strengths
        trait_strengths = {
            "analytical": "Detailed analysis and critical thinking",
            "creative": "Creative problem-solving and innovative thinking",
            "persistent": "Perseverance through challenging material",
            "leadership": "Taking initiative and guiding peers",
            "collaborative": "Working effectively with others",
            "organized": "Systematic approach to learning and tasks"
        }
        
        for trait in top_traits[:2]:
            if trait in trait_strengths:
                strengths.append(trait_strengths[trait])
        
        # Get growth areas based on learning style
        growth_areas = growth_by_style.get(primary_style, [
            "Adapting to various instructional approaches",
            "Balancing different learning modalities",
            "Developing versatility in learning strategies"
        ])
        
        # Add interest-based recommendations
        recommendations = []
        
        interest_recommendations = {
            "technology": [
                "Incorporate technology tools for organization and learning",
                "Connect academic concepts to technological applications",
                "Explore coding or digital creation to reinforce concepts"
            ],
            "arts": [
                "Use artistic expression to demonstrate understanding",
                "Connect academic concepts to creative applications",
                "Incorporate visual or performing arts into projects"
            ],
            "entrepreneurship": [
                "Connect learning to real-world applications",
                "Develop project management and planning skills",
                "Practice presenting and communicating ideas"
            ],
            "science": [
                "Emphasize scientific method across subject areas",
                "Connect concepts to scientific principles",
                "Incorporate inquiry-based approaches to learning"
            ],
            "language": [
                "Strengthen vocabulary development across subjects",
                "Practice clear written and verbal communication",
                "Use storytelling to reinforce concepts"
            ],
            "mathematics": [
                "Strengthen mathematical reasoning across subjects",
                "Practice logical thinking and problem-solving",
                "Connect abstract concepts to concrete applications"
            ]
        }
        
        for interest in top_interests[:2]:
            if interest in interest_recommendations:
                recommendations.extend(interest_recommendations[interest][:2])
        
        if not recommendations:
            recommendations = [
                "Provide balanced learning experiences across modalities",
                "Connect learning to personal interests when possible",
                "Develop metacognitive awareness of learning process"
            ]
        
        return {
            "strengths": strengths,
            "growth_areas": growth_areas,
            "recommendations": recommendations
        }
    
    def _generate_parent_alignment_insights(self, parent_comparison):
        """
        Generates insights on parent-student alignment.
        
        Args:
            parent_comparison (dict): Results from parent-student comparison
            
        Returns:
            dict: Parent alignment insights
        """
        if not parent_comparison:
            return {
                "alignment_areas": ["No parent comparison data available"],
                "difference_areas": ["No parent comparison data available"],
                "communication_strategies": [
                    "Discuss learning preferences with both student and parents",
                    "Share specific observations about learning style",
                    "Provide concrete examples of effective strategies"
                ]
            }
        
        # Extract alignment and difference areas
        alignment_areas = parent_comparison.get("alignment_areas", [])
        difference_areas = parent_comparison.get("difference_areas", [])
        
        # Generate communication strategies based on differences
        communication_strategies = [
            "Share specific observations about learning patterns",
            "Provide concrete examples of classroom successes",
            "Focus on strengths while addressing growth areas"
        ]
        
        if difference_areas:
            communication_strategies.extend([
                "Discuss different perspectives without judgment",
                "Use student work samples to illustrate learning style",
                "Suggest home activities aligned with learning preferences"
            ])
        
        return {
            "alignment_areas": alignment_areas or ["Limited alignment data available"],
            "difference_areas": difference_areas or ["Limited difference data available"],
            "communication_strategies": communication_strategies
        }
    
    def _generate_math_aptitude_assessment(self, analysis_results):
        """
        Generates mathematical aptitude assessment.
        
        Args:
            analysis_results (dict): Results from learning style analysis
            
        Returns:
            dict: Mathematical aptitude assessment
        """
        # Extract relevant information
        learning_styles = analysis_results.get("learning_styles", {})
        traits = analysis_results.get("traits", {})
        interests = analysis_results.get("interests", {})
        
        primary_style = learning_styles.get("primary", "")
        top_traits = traits.get("top_traits", [])
        top_interests = interests.get("top_interests", [])
        
        # Assess math learning style
        math_learning_style = self._assess_math_learning_style(primary_style, top_traits)
        
        # Assess potential for Abacus & Vedic Math
        abacus_vedic_potential = self._assess_abacus_vedic_potential(
            primary_style,
            top_traits,
            top_interests
        )
        
        # Generate math strengths
        math_strengths = self._generate_math_strengths(primary_style, top_traits)
        
        # Generate math challenges
        math_challenges = self._generate_math_challenges(primary_style, top_traits)
        
        # Generate teaching strategies
        teaching_strategies = self._generate_math_teaching_strategies(
            primary_style,
            top_traits
        )
        
        return {
            "math_learning_style": math_learning_style,
            "abacus_vedic_potential": abacus_vedic_potential,
            "strengths": math_strengths,
            "challenges": math_challenges,
            "teaching_strategies": teaching_strategies
        }
    
    def _assess_math_learning_style(self, primary_style, top_traits):
        """
        Assesses the student's mathematical learning style.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            str: Description of mathematical learning style
        """
        math_styles = {
            "visual": "Visual-spatial mathematical learner who benefits from diagrams, graphs, and visual representations of mathematical concepts. Likely to understand geometric concepts readily and may visualize number relationships.",
            "auditory": "Verbal-mathematical learner who benefits from talking through problems and hearing explanations. May prefer word problems and verbal reasoning over abstract symbolic manipulation.",
            "kinesthetic": "Tactile-mathematical learner who benefits from manipulatives and physical representations. Learns mathematical concepts best through hands-on activities and real-world applications.",
            "logical": "Abstract-logical mathematical learner who naturally connects with mathematical patterns and relationships. Likely to enjoy the systematic nature of mathematics and abstract reasoning.",
            "social": "Collaborative mathematical learner who benefits from discussing problems and working with others. May understand concepts better when explaining them to peers or working through problems in groups.",
            "independent": "Reflective mathematical learner who benefits from time to process concepts independently. Likely to prefer working through problems at their own pace with time for deep thinking."
        }
        
        # Get base math learning style
        style = math_styles.get(primary_style, "Balanced mathematical learner who can adapt to various approaches to mathematical concepts.")
        
        # Modify based on traits
        if "analytical" in top_traits:
            style += " Shows strong analytical thinking and attention to mathematical detail and precision."
        if "creative" in top_traits:
            style += " Demonstrates creative approaches to problem-solving and may find multiple solution paths."
        if "persistent" in top_traits:
            style += " Exhibits persistence when facing challenging mathematical problems."
        
        return style
    
    def _assess_abacus_vedic_potential(self, primary_style, top_traits, top_interests):
        """
        Assesses potential for Abacus & Vedic Math.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            top_interests (list): Top interest areas
            
        Returns:
            dict: Assessment of potential for Abacus & Vedic Math
        """
        # Base potential by learning style
        abacus_potential = {
            "visual": "High",
            "kinesthetic": "High",
            "logical": "Medium-High",
            "independent": "Medium",
            "auditory": "Medium-Low",
            "social": "Medium-Low"
        }.get(primary_style, "Medium")
        
        vedic_potential = {
            "logical": "High",
            "visual": "Medium-High",
            "independent": "Medium-High",
            "auditory": "Medium",
            "kinesthetic": "Medium-Low",
            "social": "Medium-Low"
        }.get(primary_style, "Medium")
        
        # Adjust based on traits
        trait_adjustments = {
            "analytical": {"abacus": 1, "vedic": 1},
            "persistent": {"abacus": 1, "vedic": 1},
            "organized": {"abacus": 1, "vedic": 1},
            "creative": {"abacus": 0, "vedic": 1},
            "leadership": {"abacus": 0, "vedic": 0},
            "collaborative": {"abacus": -1, "vedic": -1}
        }
        
        # Apply trait adjustments
        for trait in top_traits[:2]:
            if trait in trait_adjustments:
                # Adjust abacus potential
                if trait_adjustments[trait]["abacus"] == 1:
                    if abacus_potential == "Medium-Low":
                        abacus_potential = "Medium"
                    elif abacus_potential == "Medium":
                        abacus_potential = "Medium-High"
                    elif abacus_potential == "Medium-High":
                        abacus_potential = "High"
                elif trait_adjustments[trait]["abacus"] == -1:
                    if abacus_potential == "High":
                        abacus_potential = "Medium-High"
                    elif abacus_potential == "Medium-High":
                        abacus_potential = "Medium"
                    elif abacus_potential == "Medium":
                        abacus_potential = "Medium-Low"
                
                # Adjust vedic potential
                if trait_adjustments[trait]["vedic"] == 1:
                    if vedic_potential == "Medium-Low":
                        vedic_potential = "Medium"
                    elif vedic_potential == "Medium":
                        vedic_potential = "Medium-High"
                    elif vedic_potential == "Medium-High":
                        vedic_potential = "High"
                elif trait_adjustments[trait]["vedic"] == -1:
                    if vedic_potential == "High":
                        vedic_potential = "Medium-High"
                    elif vedic_potential == "Medium-High":
                        vedic_potential = "Medium"
                    elif vedic_potential == "Medium":
                        vedic_potential = "Medium-Low"
        
        # Further adjust if mathematics is a top interest
        if "mathematics" in top_interests:
            if abacus_potential == "Medium-Low":
                abacus_potential = "Medium"
            elif abacus_potential == "Medium":
                abacus_potential = "Medium-High"
            elif abacus_potential == "Medium-High":
                abacus_potential = "High"
            
            if vedic_potential == "Medium-Low":
                vedic_potential = "Medium"
            elif vedic_potential == "Medium":
                vedic_potential = "Medium-High"
            elif vedic_potential == "Medium-High":
                vedic_potential = "High"
        
        # Generate recommendations
        abacus_recommendations = []
        vedic_recommendations = []
        
        if abacus_potential in ["High", "Medium-High"]:
            abacus_recommendations = [
                "Consider introducing Abacus training to develop visual-spatial calculation skills",
                "Start with basic Abacus concepts and progress based on interest and aptitude",
                "Use Abacus training to strengthen mental math abilities"
            ]
        else:
            abacus_recommendations = [
                "Introduce Abacus concepts gradually if interest develops",
                "Use physical manipulatives to build number sense before formal Abacus training",
                "Consider alternative approaches to mental math development"
            ]
        
        if vedic_potential in ["High", "Medium-High"]:
            vedic_recommendations = [
                "Consider introducing Vedic Math techniques to enhance calculation speed",
                "Start with basic Vedic Math sutras and applications",
                "Use Vedic Math to develop pattern recognition and mathematical intuition"
            ]
        else:
            vedic_recommendations = [
                "Focus on building strong foundational math skills before introducing Vedic techniques",
                "Introduce Vedic Math concepts gradually as supplements to traditional methods",
                "Consider alternative approaches to developing mathematical fluency"
            ]
        
        return {
            "abacus": {
                "potential": abacus_potential,
                "recommendations": abacus_recommendations
            },
            "vedic": {
                "potential": vedic_potential,
                "recommendations": vedic_recommendations
            }
        }
    
    def _generate_math_strengths(self, primary_style, top_traits):
        """
        Generates mathematical strengths based on learning style and traits.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            list: Mathematical strengths
        """
        # Strengths by learning style
        strengths_by_style = {
            "visual": [
                "Geometric reasoning and spatial relationships",
                "Understanding visual patterns in mathematics",
                "Interpreting graphs and visual data",
                "Visualizing mathematical concepts"
            ],
            "auditory": [
                "Verbal reasoning in mathematics",
                "Following verbal explanations of mathematical concepts",
                "Discussing mathematical ideas",
                "Word problems and mathematical language"
            ],
            "kinesthetic": [
                "Hands-on mathematical activities",
                "Applied and practical mathematics",
                "Using manipulatives effectively",
                "Real-world mathematical applications"
            ],
            "logical": [
                "Abstract mathematical reasoning",
                "Recognizing patterns and relationships",
                "Systematic problem-solving",
                "Logical proofs and deductions"
            ],
            "social": [
                "Collaborative problem-solving",
                "Explaining mathematical concepts to others",
                "Learning from mathematical discussions",
                "Group mathematical projects"
            ],
            "independent": [
                "Self-directed mathematical exploration",
                "Focused individual problem-solving",
                "Developing personal mathematical strategies",
                "Independent mathematical research"
            ]
        }
        
        # Get base strengths from learning style
        strengths = strengths_by_style.get(primary_style, [
            "Adaptable approach to mathematical concepts",
            "Balancing different mathematical thinking styles",
            "Applying various strategies to problem-solving"
        ])
        
        # Add trait-based strengths
        trait_strengths = {
            "analytical": "Detailed mathematical analysis and precision",
            "creative": "Creative approaches to mathematical problem-solving",
            "persistent": "Perseverance through challenging mathematical problems",
            "leadership": "Taking initiative in mathematical discussions and group work",
            "collaborative": "Working effectively with others on mathematical tasks",
            "organized": "Systematic approach to mathematical procedures and problem-solving"
        }
        
        for trait in top_traits[:2]:
            if trait in trait_strengths:
                strengths.append(trait_strengths[trait])
        
        return strengths
    
    def _generate_math_challenges(self, primary_style, top_traits):
        """
        Generates mathematical challenges based on learning style and traits.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            list: Mathematical challenges
        """
        # Challenges by learning style
        challenges_by_style = {
            "visual": [
                "Abstract mathematical concepts without visual representation",
                "Showing work in a step-by-step manner",
                "Verbal mathematical explanations",
                "Mental math without visual aids"
            ],
            "auditory": [
                "Complex visual or spatial mathematics",
                "Silent, independent mathematical work",
                "Geometric reasoning",
                "Visual pattern recognition"
            ],
            "kinesthetic": [
                "Abstract mathematical theory",
                "Extended periods of seated mathematical work",
                "Multi-step problems without concrete application",
                "Showing detailed written work"
            ],
            "logical": [
                "Creative or open-ended mathematical problems",
                "Mathematical concepts without clear patterns",
                "Showing work when solution paths seem obvious",
                "Collaborative mathematical tasks"
            ],
            "social": [
                "Independent mathematical practice",
                "Silent, focused mathematical work",
                "Abstract mathematical reasoning",
                "Detailed individual problem-solving"
            ],
            "independent": [
                "Collaborative mathematical projects",
                "Explaining mathematical thinking to others",
                "Group problem-solving activities",
                "Seeking help with mathematical challenges"
            ]
        }
        
        # Get base challenges from learning style
        challenges = challenges_by_style.get(primary_style, [
            "Adapting to various mathematical teaching approaches",
            "Balancing conceptual and procedural understanding",
            "Connecting abstract and applied mathematics"
        ])
        
        # Add trait-based challenges
        trait_challenges = {
            "analytical": "May get caught in mathematical details and miss broader concepts",
            "creative": "May use unconventional approaches that are difficult to assess",
            "persistent": "May become frustrated when mathematical solutions aren't readily apparent",
            "leadership": "May dominate group mathematical activities",
            "collaborative": "May rely too heavily on others during mathematical problem-solving",
            "organized": "May struggle with open-ended or creative mathematical tasks"
        }
        
        for trait in top_traits[:2]:
            if trait in trait_challenges:
                challenges.append(trait_challenges[trait])
        
        return challenges
    
    def _generate_math_teaching_strategies(self, primary_style, top_traits):
        """
        Generates mathematical teaching strategies based on learning style and traits.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            list: Mathematical teaching strategies
        """
        # Strategies by learning style
        strategies_by_style = {
            "visual": [
                "Use visual models, diagrams, and graphs",
                "Incorporate color-coding for mathematical processes",
                "Provide visual step-by-step procedures",
                "Use graphic organizers for mathematical concepts"
            ],
            "auditory": [
                "Explain mathematical concepts verbally",
                "Encourage mathematical discussions and think-alouds",
                "Use rhythmic patterns for mathematical memorization",
                "Incorporate mathematical vocabulary development"
            ],
            "kinesthetic": [
                "Use manipulatives and hands-on activities",
                "Incorporate movement into mathematical learning",
                "Connect mathematics to real-world applications",
                "Use physical models for abstract concepts"
            ],
            "logical": [
                "Emphasize patterns and relationships in mathematics",
                "Provide logical sequences and clear procedures",
                "Encourage analytical thinking and reasoning",
                "Connect new concepts to previously learned material"
            ],
            "social": [
                "Incorporate collaborative problem-solving",
                "Use mathematical discussions and peer teaching",
                "Implement group projects with mathematical components",
                "Create opportunities for mathematical communication"
            ],
            "independent": [
                "Provide self-directed mathematical exploration opportunities",
                "Allow time for independent problem-solving",
                "Offer choice in mathematical practice activities",
                "Provide clear expectations for independent work"
            ]
        }
        
        # Get base strategies from learning style
        strategies = strategies_by_style.get(primary_style, [
            "Use multi-modal approaches to mathematical instruction",
            "Balance conceptual understanding with procedural fluency",
            "Provide both independent and collaborative mathematical experiences",
            "Connect abstract concepts to concrete applications"
        ])
        
        # Add trait-based strategies
        trait_strategies = {
            "analytical": [
                "Provide opportunities for detailed mathematical analysis",
                "Encourage precision and attention to mathematical detail"
            ],
            "creative": [
                "Allow for multiple solution paths",
                "Incorporate open-ended mathematical problems"
            ],
            "persistent": [
                "Provide appropriately challenging mathematical tasks",
                "Recognize effort and perseverance in mathematics"
            ],
            "leadership": [
                "Provide opportunities to lead mathematical discussions",
                "Encourage positive mathematical leadership"
            ],
            "collaborative": [
                "Create meaningful collaborative mathematical experiences",
                "Teach effective mathematical communication"
            ],
            "organized": [
                "Provide organizational tools for mathematical work",
                "Recognize systematic approaches to problem-solving"
            ]
        }
        
        for trait in top_traits[:2]:
            if trait in trait_strategies:
                strategies.extend(trait_strategies[trait])
        
        # Add Abacus and Vedic Math specific strategies
        strategies.extend([
            "Consider introducing Abacus for visual-spatial calculation development",
            "Explore Vedic Mathematics for mental math and calculation speed",
            "Balance traditional and alternative mathematical approaches"
        ])
        
        return strategies
    
    def _generate_exam_readiness(self, student_info, analysis_results):
        """
        Generates examination readiness assessment.
        
        Args:
            student_info (dict): Student information
            analysis_results (dict): Results from learning style analysis
            
        Returns:
            dict: Examination readiness assessment
        """
        # Extract relevant information
        age = student_info.get("age", 10)
        grade = student_info.get("grade", age - 5)  # Estimate grade if not provided
        
        learning_styles = analysis_results.get("learning_styles", {})
        traits = analysis_results.get("traits", {})
        
        primary_style = learning_styles.get("primary", "")
        top_traits = traits.get("top_traits", [])
        
        # Determine age-appropriate global examinations
        global_exams = self._get_age_appropriate_exams(age, grade)
        
        # Assess exam-taking strengths
        exam_strengths = self._assess_exam_strengths(primary_style, top_traits)
        
        # Assess exam-taking challenges
        exam_challenges = self._assess_exam_challenges(primary_style, top_traits)
        
        # Generate exam preparation strategies
        preparation_strategies = self._generate_exam_preparation_strategies(
            primary_style,
            top_traits
        )
        
        return {
            "global_exams": global_exams,
            "exam_strengths": exam_strengths,
            "exam_challenges": exam_challenges,
            "preparation_strategies": preparation_strategies
        }
    
    def _get_age_appropriate_exams(self, age, grade):
        """
        Determines age-appropriate global examinations.
        
        Args:
            age (int): Student's age
            grade (int): Student's grade level
            
        Returns:
            list: Age-appropriate global examinations
        """
        # Elementary school exams (ages 5-10, grades K-5)
        elementary_exams = [
            {
                "name": "International Mathematics Olympiad (IMO)",
                "description": "Elementary level mathematics competition for young students",
                "age_range": "Grades 1-5",
                "benefits": "Develops problem-solving skills and mathematical thinking",
                "preparation": "Regular practice with mathematical puzzles and problems"
            },
            {
                "name": "International English Olympiad (IEO)",
                "description": "English language and comprehension competition for elementary students",
                "age_range": "Grades 1-5",
                "benefits": "Enhances vocabulary, grammar, and reading comprehension",
                "preparation": "Regular reading practice and language exercises"
            },
            {
                "name": "National Science Olympiad (NSO)",
                "description": "Science competition covering age-appropriate scientific concepts",
                "age_range": "Grades 1-5",
                "benefits": "Develops scientific thinking and knowledge",
                "preparation": "Exploring scientific concepts through experiments and reading"
            },
            {
                "name": "ASSET (Assessment of Scholastic Skills through Educational Testing)",
                "description": "Diagnostic test assessing conceptual understanding across subjects",
                "age_range": "Grades 3-5",
                "benefits": "Provides detailed feedback on conceptual understanding",
                "preparation": "Focus on understanding concepts rather than memorization"
            }
        ]
        
        # Middle school exams (ages 11-13, grades 6-8)
        middle_exams = [
            {
                "name": "International Mathematics Olympiad (IMO)",
                "description": "Challenging mathematics competition for middle school students",
                "age_range": "Grades 6-8",
                "benefits": "Develops advanced problem-solving and mathematical reasoning",
                "preparation": "Regular practice with challenging math problems"
            },
            {
                "name": "International Science Olympiad (ISO)",
                "description": "Science competition covering physics, chemistry, and biology",
                "age_range": "Grades 6-8",
                "benefits": "Enhances scientific knowledge and analytical thinking",
                "preparation": "In-depth study of scientific concepts and principles"
            },
            {
                "name": "ASSET (Assessment of Scholastic Skills through Educational Testing)",
                "description": "Diagnostic test assessing conceptual understanding across subjects",
                "age_range": "Grades 6-8",
                "benefits": "Provides detailed feedback on conceptual understanding",
                "preparation": "Focus on understanding concepts rather than memorization"
            },
            {
                "name": "International English Olympiad (IEO)",
                "description": "English language competition for middle school students",
                "age_range": "Grades 6-8",
                "benefits": "Enhances language skills and critical reading",
                "preparation": "Regular reading, writing practice, and vocabulary development"
            },
            {
                "name": "American Mathematics Competition 8 (AMC 8)",
                "description": "Mathematics competition for middle school students",
                "age_range": "Grades 6-8",
                "benefits": "Develops problem-solving skills and mathematical thinking",
                "preparation": "Regular practice with challenging math problems"
            }
        ]
        
        # High school exams (ages 14-18, grades 9-12)
        high_exams = [
            {
                "name": "PSAT/NMSQT (Preliminary SAT/National Merit Scholarship Qualifying Test)",
                "description": "Preliminary version of the SAT, used for National Merit Scholarships",
                "age_range": "Grades 10-11",
                "benefits": "Prepares for SAT and qualifies for scholarships",
                "preparation": "Practice tests and targeted study in critical reading, math, and writing"
            },
            {
                "name": "SAT (Scholastic Assessment Test)",
                "description": "College admission test measuring reading, writing, and math skills",
                "age_range": "Grades 11-12",
                "benefits": "Required for many college applications",
                "preparation": "Regular practice tests and subject-specific study"
            },
            {
                "name": "ACT (American College Testing)",
                "description": "College admission test covering English, math, reading, and science",
                "age_range": "Grades 11-12",
                "benefits": "Alternative to SAT for college applications",
                "preparation": "Practice tests and subject-specific study"
            },
            {
                "name": "AP (Advanced Placement) Exams",
                "description": "College-level exams in specific subject areas",
                "age_range": "Grades 10-12",
                "benefits": "Can earn college credit and demonstrate subject mastery",
                "preparation": "AP courses and intensive subject study"
            },
            {
                "name": "International Baccalaureate (IB) Exams",
                "description": "Rigorous international education program exams",
                "age_range": "Grades 11-12",
                "benefits": "Internationally recognized qualification",
                "preparation": "IB Diploma Programme coursework"
            },
            {
                "name": "American Mathematics Competition (AMC 10/12)",
                "description": "Mathematics competition for high school students",
                "age_range": "Grades 9-12",
                "benefits": "Develops advanced mathematical problem-solving",
                "preparation": "Regular practice with challenging math problems"
            },
            {
                "name": "Science Olympiads (Physics, Chemistry, Biology)",
                "description": "Subject-specific science competitions",
                "age_range": "Grades 9-12",
                "benefits": "Develops deep subject knowledge and problem-solving",
                "preparation": "In-depth study and laboratory practice"
            }
        ]
        
        # Aptitude tests for all age groups
        aptitude_tests = [
            {
                "name": "Cognitive Abilities Test (CogAT)",
                "description": "Measures reasoning abilities in verbal, quantitative, and nonverbal areas",
                "age_range": "K-12",
                "benefits": "Identifies cognitive strengths and learning styles",
                "preparation": "Exposure to diverse problem-solving activities"
            },
            {
                "name": "Naglieri Nonverbal Ability Test (NNAT)",
                "description": "Nonverbal test of general ability using geometric shapes and patterns",
                "age_range": "K-12",
                "benefits": "Assesses ability independent of language and cultural background",
                "preparation": "Practice with pattern recognition and spatial reasoning"
            },
            {
                "name": "Otis-Lennon School Ability Test (OLSAT)",
                "description": "Measures abstract thinking and reasoning ability",
                "age_range": "K-12",
                "benefits": "Assesses aptitude for learning",
                "preparation": "Practice with verbal and nonverbal reasoning problems"
            }
        ]
        
        # Select age-appropriate exams
        if age <= 10:  # Elementary school
            appropriate_exams = elementary_exams
            appropriate_aptitude = aptitude_tests
        elif age <= 13:  # Middle school
            appropriate_exams = middle_exams
            appropriate_aptitude = aptitude_tests
        else:  # High school
            appropriate_exams = high_exams
            appropriate_aptitude = aptitude_tests
        
        # Combine and return
        return {
            "academic_exams": appropriate_exams,
            "aptitude_tests": appropriate_aptitude
        }
    
    def _assess_exam_strengths(self, primary_style, top_traits):
        """
        Assesses exam-taking strengths based on learning style and traits.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            list: Exam-taking strengths
        """
        # Strengths by learning style
        strengths_by_style = {
            "visual": [
                "Processing visual information in exams",
                "Interpreting graphs, charts, and diagrams",
                "Remembering information presented visually",
                "Spatial reasoning questions"
            ],
            "auditory": [
                "Recalling information from discussions",
                "Processing verbal instructions in exams",
                "Language-based questions",
                "Verbal reasoning sections"
            ],
            "kinesthetic": [
                "Practical or lab-based assessments",
                "Exams with manipulative components",
                "Applied problem-solving questions",
                "Performance-based assessments"
            ],
            "logical": [
                "Logical reasoning questions",
                "Mathematical problem-solving",
                "Sequential thinking tasks",
                "Pattern recognition questions"
            ],
            "social": [
                "Group assessment components",
                "Discussion-based evaluations",
                "Collaborative problem-solving tasks",
                "Interpersonal scenario questions"
            ],
            "independent": [
                "Self-paced exam sections",
                "Independent problem-solving questions",
                "Extended response questions",
                "Research-based assessments"
            ]
        }
        
        # Get base strengths from learning style
        strengths = strengths_by_style.get(primary_style, [
            "Adapting to various question formats",
            "Balancing different cognitive approaches",
            "Processing information in multiple formats"
        ])
        
        # Add trait-based strengths
        trait_strengths = {
            "analytical": "Detailed analysis of complex questions",
            "creative": "Novel approaches to problem-solving questions",
            "persistent": "Maintaining focus throughout lengthy exams",
            "leadership": "Confidence in assessment situations",
            "collaborative": "Effective performance in group assessment components",
            "organized": "Systematic approach to exam questions and time management"
        }
        
        for trait in top_traits[:2]:
            if trait in trait_strengths:
                strengths.append(trait_strengths[trait])
        
        return strengths
    
    def _assess_exam_challenges(self, primary_style, top_traits):
        """
        Assesses exam-taking challenges based on learning style and traits.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            list: Exam-taking challenges
        """
        # Challenges by learning style
        challenges_by_style = {
            "visual": [
                "Extended reading without visual supports",
                "Purely auditory instructions or content",
                "Remembering verbal information without visual cues",
                "Writing extensive text responses"
            ],
            "auditory": [
                "Complex visual information without verbal explanation",
                "Silent reading comprehension under time pressure",
                "Interpreting detailed graphs or diagrams",
                "Spatial reasoning questions"
            ],
            "kinesthetic": [
                "Sitting still for extended exam periods",
                "Abstract theoretical questions",
                "Limited physical interaction with materials",
                "Extended writing tasks"
            ],
            "logical": [
                "Ambiguous or open-ended questions",
                "Subjective assessment criteria",
                "Creative writing or expression tasks",
                "Questions without clear logical structure"
            ],
            "social": [
                "Extended individual work without interaction",
                "Competitive assessment environments",
                "Limited verbal processing opportunities",
                "Isolated problem-solving under pressure"
            ],
            "independent": [
                "Group assessment components",
                "Time pressure that limits reflection",
                "Collaborative problem-solving requirements",
                "Verbal presentation components"
            ]
        }
        
        # Get base challenges from learning style
        challenges = challenges_by_style.get(primary_style, [
            "Adapting to unfamiliar question formats",
            "Managing time across different question types",
            "Balancing speed and accuracy"
        ])
        
        # Add trait-based challenges
        trait_challenges = {
            "analytical": "May spend too much time on detailed analysis of questions",
            "creative": "May use unconventional approaches that don't match scoring criteria",
            "persistent": "May perseverate on difficult questions instead of moving on",
            "leadership": "May rush through individual assessment components",
            "collaborative": "May struggle with competitive assessment environments",
            "organized": "May become anxious if exam structure differs from expectations"
        }
        
        for trait in top_traits[:2]:
            if trait in trait_challenges:
                challenges.append(trait_challenges[trait])
        
        return challenges
    
    def _generate_exam_preparation_strategies(self, primary_style, top_traits):
        """
        Generates exam preparation strategies based on learning style and traits.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            list: Exam preparation strategies
        """
        # Strategies by learning style
        strategies_by_style = {
            "visual": [
                "Use visual study aids like mind maps and diagrams",
                "Convert notes into visual formats",
                "Practice with visual practice questions",
                "Use color-coding for organizing information"
            ],
            "auditory": [
                "Record and listen to study materials",
                "Discuss concepts verbally",
                "Use mnemonic devices and verbal repetition",
                "Participate in study groups with discussion"
            ],
            "kinesthetic": [
                "Use movement while studying",
                "Create physical models or manipulatives",
                "Take breaks for physical activity",
                "Practice with hands-on simulations when possible"
            ],
            "logical": [
                "Organize study materials in logical sequences",
                "Create systematic study plans",
                "Practice with problem-solving questions",
                "Look for patterns and connections between concepts"
            ],
            "social": [
                "Form study groups",
                "Teach concepts to others",
                "Discuss practice questions with peers",
                "Use collaborative study techniques"
            ],
            "independent": [
                "Create personalized study schedules",
                "Find quiet, focused study environments",
                "Set individual study goals",
                "Self-test regularly"
            ]
        }
        
        # Get base strategies from learning style
        strategies = strategies_by_style.get(primary_style, [
            "Use multi-modal study techniques",
            "Balance individual and group study",
            "Practice with various question formats",
            "Develop personalized study routines"
        ])
        
        # Add trait-based strategies
        trait_strategies = {
            "analytical": [
                "Practice analyzing complex questions",
                "Develop systematic approaches to different question types"
            ],
            "creative": [
                "Balance creative thinking with standard approaches",
                "Practice identifying what scoring criteria require"
            ],
            "persistent": [
                "Set time limits for practice questions",
                "Develop strategies for knowing when to move on"
            ],
            "leadership": [
                "Practice careful reading of all instructions",
                "Develop patience with detailed individual work"
            ],
            "collaborative": [
                "Balance collaborative study with independent practice",
                "Simulate test conditions during some practice sessions"
            ],
            "organized": [
                "Create detailed study plans",
                "Practice with unfamiliar formats to build flexibility"
            ]
        }
        
        for trait in top_traits[:2]:
            if trait in trait_strategies:
                strategies.extend(trait_strategies[trait])
        
        # Add general exam strategies
        general_strategies = [
            "Practice with timed conditions",
            "Develop effective test-taking strategies",
            "Learn relaxation techniques for test anxiety",
            "Ensure physical readiness (sleep, nutrition, etc.)"
        ]
        
        strategies.extend(general_strategies)
        
        return strategies
