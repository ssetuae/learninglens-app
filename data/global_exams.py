"""
Global Examination Recommendations Module
This module provides recommendations for globally available examinations and aptitude tests.
"""

import os
import json
from datetime import datetime

class GlobalExamRecommender:
    """
    Recommends globally available examinations and aptitude tests based on student profile.
    """
    
    def __init__(self):
        """
        Initialize the global examination recommender.
        """
        # Define examination categories
        self.exam_categories = {
            "academic": "Standard academic assessments measuring subject knowledge and skills",
            "aptitude": "Tests measuring inherent abilities and potential rather than acquired knowledge",
            "competition": "Competitive examinations that rank students against peers",
            "talent_search": "Programs identifying gifted students through specialized testing",
            "certification": "Assessments providing recognized credentials in specific areas"
        }
        
        # Define global examinations by age group
        self.examinations = {
            "elementary": {
                "academic": [
                    {
                        "name": "International Schools Assessment (ISA)",
                        "description": "Assessment for international schools measuring reading, math, and science",
                        "age_range": "Grades 3-10",
                        "regions": "Global",
                        "website": "https://www.acer.org/isa",
                        "benefits": [
                            "International benchmarking",
                            "Detailed skill analysis",
                            "Comparison with similar schools globally"
                        ],
                        "preparation": "Regular classroom learning with focus on reading comprehension and problem-solving"
                    },
                    {
                        "name": "ASSET (Assessment of Scholastic Skills through Educational Testing)",
                        "description": "Diagnostic test assessing conceptual understanding across subjects",
                        "age_range": "Grades 3-10",
                        "regions": "International",
                        "website": "https://www.ei-india.com/asset/",
                        "benefits": [
                            "Detailed feedback on conceptual understanding",
                            "Identifies specific learning gaps",
                            "Benchmarking against peers"
                        ],
                        "preparation": "Focus on understanding concepts rather than memorization"
                    },
                    {
                        "name": "Cambridge Primary Checkpoint",
                        "description": "Assessments for Cambridge Primary students in English, Math, and Science",
                        "age_range": "Ages 5-11",
                        "regions": "Global (Cambridge schools)",
                        "website": "https://www.cambridgeinternational.org/",
                        "benefits": [
                            "International standards assessment",
                            "Detailed feedback reports",
                            "Preparation for Cambridge Secondary"
                        ],
                        "preparation": "Following Cambridge Primary curriculum with regular practice"
                    }
                ],
                "aptitude": [
                    {
                        "name": "Cognitive Abilities Test (CogAT)",
                        "description": "Measures reasoning abilities in verbal, quantitative, and nonverbal areas",
                        "age_range": "K-12",
                        "regions": "Global",
                        "website": "https://www.riversideinsights.com/solutions/cogat",
                        "benefits": [
                            "Identifies cognitive strengths and learning styles",
                            "Helps predict academic success",
                            "Useful for gifted program placement"
                        ],
                        "preparation": "Exposure to diverse problem-solving activities and puzzles"
                    },
                    {
                        "name": "Naglieri Nonverbal Ability Test (NNAT)",
                        "description": "Nonverbal test of general ability using geometric shapes and patterns",
                        "age_range": "K-12",
                        "regions": "Global",
                        "website": "https://www.pearsonassessments.com/",
                        "benefits": [
                            "Culturally neutral assessment",
                            "Identifies spatial reasoning abilities",
                            "Useful for ELL students and diverse populations"
                        ],
                        "preparation": "Practice with pattern recognition and spatial reasoning puzzles"
                    },
                    {
                        "name": "Otis-Lennon School Ability Test (OLSAT)",
                        "description": "Measures abstract thinking and reasoning ability",
                        "age_range": "K-12",
                        "regions": "Global",
                        "website": "https://www.pearsonassessments.com/",
                        "benefits": [
                            "Assesses verbal and nonverbal reasoning",
                            "Used for gifted program admission",
                            "Identifies learning potential"
                        ],
                        "preparation": "Practice with verbal and nonverbal reasoning problems"
                    }
                ],
                "competition": [
                    {
                        "name": "International Mathematics Olympiad (IMO) - Elementary Level",
                        "description": "Mathematics competition for elementary students",
                        "age_range": "Grades 1-5",
                        "regions": "Global",
                        "website": "Various national organizations",
                        "benefits": [
                            "Develops problem-solving skills",
                            "Builds mathematical confidence",
                            "Provides recognition for mathematical talent"
                        ],
                        "preparation": "Regular practice with mathematical puzzles and problems beyond grade level"
                    },
                    {
                        "name": "International English Olympiad (IEO)",
                        "description": "English language and comprehension competition",
                        "age_range": "Grades 1-12",
                        "regions": "Global",
                        "website": "Various national organizations",
                        "benefits": [
                            "Enhances vocabulary and grammar",
                            "Improves reading comprehension",
                            "Develops communication skills"
                        ],
                        "preparation": "Regular reading practice and language exercises"
                    },
                    {
                        "name": "International Science Olympiad (ISO)",
                        "description": "Science competition covering age-appropriate scientific concepts",
                        "age_range": "Grades 1-12",
                        "regions": "Global",
                        "website": "Various national organizations",
                        "benefits": [
                            "Develops scientific thinking",
                            "Encourages curiosity and exploration",
                            "Builds knowledge beyond curriculum"
                        ],
                        "preparation": "Exploring scientific concepts through experiments and reading"
                    },
                    {
                        "name": "Math Kangaroo",
                        "description": "International mathematical competition with age-appropriate problems",
                        "age_range": "Grades 1-12",
                        "regions": "Global (80+ countries)",
                        "website": "https://www.mathkangaroo.org/",
                        "benefits": [
                            "Accessible mathematical challenge",
                            "Focus on logical thinking rather than calculation",
                            "International recognition"
                        ],
                        "preparation": "Regular practice with mathematical puzzles and problems"
                    }
                ],
                "talent_search": [
                    {
                        "name": "Johns Hopkins Center for Talented Youth (CTY)",
                        "description": "Talent search program identifying academically gifted young students",
                        "age_range": "Grades 2-8",
                        "regions": "Global",
                        "website": "https://cty.jhu.edu/",
                        "benefits": [
                            "Access to advanced courses",
                            "Summer programs for gifted students",
                            "Recognition of academic talent"
                        ],
                        "preparation": "Strong performance on school assessments and qualifying exams"
                    },
                    {
                        "name": "Duke Talent Identification Program (TIP)",
                        "description": "Talent search identifying academically talented students",
                        "age_range": "Grades 4-6",
                        "regions": "Global",
                        "website": "https://tip.duke.edu/",
                        "benefits": [
                            "Access to enrichment resources",
                            "Summer studies programs",
                            "Above-level testing opportunities"
                        ],
                        "preparation": "Strong academic performance and qualifying test scores"
                    }
                ],
                "certification": [
                    {
                        "name": "Cambridge English: Young Learners (YLE)",
                        "description": "English language certification for young learners",
                        "age_range": "Ages 7-12",
                        "regions": "Global",
                        "website": "https://www.cambridgeenglish.org/",
                        "benefits": [
                            "Internationally recognized English certification",
                            "Age-appropriate assessment",
                            "Foundation for future language qualifications"
                        ],
                        "preparation": "Regular English language practice and specific exam preparation"
                    },
                    {
                        "name": "DELF Prim",
                        "description": "French language certification for young learners",
                        "age_range": "Ages 7-12",
                        "regions": "Global",
                        "website": "http://www.ciep.fr/en/delf-prim",
                        "benefits": [
                            "Official French language certification",
                            "Age-appropriate assessment",
                            "Recognition by French Ministry of Education"
                        ],
                        "preparation": "French language study and specific exam preparation"
                    }
                ]
            },
            "middle": {
                "academic": [
                    {
                        "name": "International Schools Assessment (ISA)",
                        "description": "Assessment for international schools measuring reading, math, and science",
                        "age_range": "Grades 3-10",
                        "regions": "Global",
                        "website": "https://www.acer.org/isa",
                        "benefits": [
                            "International benchmarking",
                            "Detailed skill analysis",
                            "Comparison with similar schools globally"
                        ],
                        "preparation": "Regular classroom learning with focus on reading comprehension and problem-solving"
                    },
                    {
                        "name": "Cambridge Secondary 1 Checkpoint",
                        "description": "Assessments for Cambridge Secondary 1 students in English, Math, and Science",
                        "age_range": "Ages 11-14",
                        "regions": "Global (Cambridge schools)",
                        "website": "https://www.cambridgeinternational.org/",
                        "benefits": [
                            "International standards assessment",
                            "Detailed feedback reports",
                            "Preparation for Cambridge IGCSE"
                        ],
                        "preparation": "Following Cambridge Secondary 1 curriculum with regular practice"
                    },
                    {
                        "name": "TIMSS (Trends in International Mathematics and Science Study)",
                        "description": "International assessment of mathematics and science knowledge",
                        "age_range": "Grades 4 and 8",
                        "regions": "Global (60+ countries)",
                        "website": "https://timssandpirls.bc.edu/",
                        "benefits": [
                            "International comparison of educational systems",
                            "Comprehensive assessment of math and science",
                            "Identifies educational trends"
                        ],
                        "preparation": "Strong foundation in grade-level mathematics and science"
                    }
                ],
                "aptitude": [
                    {
                        "name": "Cognitive Abilities Test (CogAT)",
                        "description": "Measures reasoning abilities in verbal, quantitative, and nonverbal areas",
                        "age_range": "K-12",
                        "regions": "Global",
                        "website": "https://www.riversideinsights.com/solutions/cogat",
                        "benefits": [
                            "Identifies cognitive strengths and learning styles",
                            "Helps predict academic success",
                            "Useful for advanced program placement"
                        ],
                        "preparation": "Exposure to diverse problem-solving activities and puzzles"
                    },
                    {
                        "name": "Secondary School Admission Test (SSAT)",
                        "description": "Admission test for independent schools measuring verbal, quantitative, and reading skills",
                        "age_range": "Grades 5-11",
                        "regions": "Global",
                        "website": "https://www.ssat.org/",
                        "benefits": [
                            "Required for many private school admissions",
                            "Measures academic abilities",
                            "Provides percentile rankings"
                        ],
                        "preparation": "Practice tests and targeted study in verbal, math, and reading"
                    },
                    {
                        "name": "Independent School Entrance Examination (ISEE)",
                        "description": "Admission test for independent schools measuring verbal and quantitative reasoning",
                        "age_range": "Grades 4-12",
                        "regions": "Global",
                        "website": "https://www.erblearn.org/families/isee-by-erb/",
                        "benefits": [
                            "Required for many private school admissions",
                            "Measures both achievement and potential",
                            "Multiple test levels based on grade"
                        ],
                        "preparation": "Practice tests and targeted study in verbal and quantitative reasoning"
                    }
                ],
                "competition": [
                    {
                        "name": "American Mathematics Competition 8 (AMC 8)",
                        "description": "25-question multiple choice contest for middle school students",
                        "age_range": "Grades 6-8",
                        "regions": "Global (open to international students)",
                        "website": "https://www.maa.org/math-competitions/amc-8",
                        "benefits": [
                            "Develops problem-solving skills",
                            "Preparation for higher-level competitions",
                            "Recognition for mathematical talent"
                        ],
                        "preparation": "Practice with previous AMC 8 problems and middle school competition math"
                    },
                    {
                        "name": "Math Counts",
                        "description": "National middle school coaching and competition program",
                        "age_range": "Grades 6-8",
                        "regions": "US (with international participation)",
                        "website": "https://www.mathcounts.org/",
                        "benefits": [
                            "Develops mathematical problem-solving",
                            "Builds teamwork skills",
                            "Provides recognition for mathematical talent"
                        ],
                        "preparation": "Regular practice with competition-style problems and team strategies"
                    },
                    {
                        "name": "International Junior Science Olympiad (IJSO)",
                        "description": "International science competition for middle school students",
                        "age_range": "Under 16 years old",
                        "regions": "Global",
                        "website": "http://www.ijso-official.org/",
                        "benefits": [
                            "Develops scientific knowledge and skills",
                            "International recognition",
                            "Preparation for higher-level science competitions"
                        ],
                        "preparation": "In-depth study of scientific concepts beyond curriculum"
                    },
                    {
                        "name": "International Junior Math Olympiad (IJMO)",
                        "description": "International competition for middle school students",
                        "age_range": "Grades 6-8",
                        "regions": "Global",
                        "website": "https://www.ijmo.org/",
                        "benefits": [
                            "Develops advanced mathematical thinking",
                            "International recognition",
                            "Preparation for higher-level competitions"
                        ],
                        "preparation": "Practice with olympiad-style problems and proof techniques"
                    }
                ],
                "talent_search": [
                    {
                        "name": "Johns Hopkins Center for Talented Youth (CTY)",
                        "description": "Talent search program identifying academically gifted students",
                        "age_range": "Grades 2-8",
                        "regions": "Global",
                        "website": "https://cty.jhu.edu/",
                        "benefits": [
                            "Access to advanced courses",
                            "Summer programs for gifted students",
                            "Recognition of academic talent"
                        ],
                        "preparation": "Strong performance on school assessments and qualifying exams"
                    },
                    {
                        "name": "Northwestern University's Midwest Academic Talent Search (NUMATS)",
                        "description": "Talent search program for academically talented students",
                        "age_range": "Grades 3-9",
                        "regions": "Global (primarily US)",
                        "website": "https://www.ctd.northwestern.edu/program/numats",
                        "benefits": [
                            "Above-grade-level testing",
                            "Access to advanced programs",
                            "Recognition of academic talent"
                        ],
                        "preparation": "Strong academic performance and qualifying test scores"
                    }
                ],
                "certification": [
                    {
                        "name": "Cambridge English: Key (KET) for Schools",
                        "description": "Basic level English language certification for school-age learners",
                        "age_range": "Middle school and above",
                        "regions": "Global",
                        "website": "https://www.cambridgeenglish.org/",
                        "benefits": [
                            "Internationally recognized English certification",
                            "School-focused content",
                            "Foundation for higher-level certifications"
                        ],
                        "preparation": "English language study and specific exam preparation"
                    },
                    {
                        "name": "DELF Junior",
                        "description": "French language certification for school-age learners",
                        "age_range": "Middle school and above",
                        "regions": "Global",
                        "website": "http://www.ciep.fr/en/delf-junior",
                        "benefits": [
                            "Official French language certification",
                            "School-focused content",
                            "Recognition by French Ministry of Education"
                        ],
                        "preparation": "French language study and specific exam preparation"
                    },
                    {
                        "name": "Microsoft Office Specialist (MOS)",
                        "description": "Certification validating skills in Microsoft Office applications",
                        "age_range": "No age restriction (suitable for middle school+)",
                        "regions": "Global",
                        "website": "https://www.microsoft.com/en-us/learning/mos-certification.aspx",
                        "benefits": [
                            "Industry-recognized certification",
                            "Validates practical digital skills",
                            "Enhances academic and career prospects"
                        ],
                        "preparation": "Practice with Microsoft Office applications and specific exam preparation"
                    }
                ]
            },
            "high": {
                "academic": [
                    {
                        "name": "PSAT/NMSQT (Preliminary SAT/National Merit Scholarship Qualifying Test)",
                        "description": "Preliminary version of the SAT, used for National Merit Scholarships",
                        "age_range": "Grades 10-11",
                        "regions": "Global (primarily US)",
                        "website": "https://www.collegeboard.org/",
                        "benefits": [
                            "Preparation for SAT",
                            "Qualification for scholarships",
                            "College readiness assessment"
                        ],
                        "preparation": "Practice tests and targeted study in critical reading, math, and writing"
                    },
                    {
                        "name": "SAT (Scholastic Assessment Test)",
                        "description": "College admission test measuring reading, writing, and math skills",
                        "age_range": "Grades 11-12",
                        "regions": "Global",
                        "website": "https://www.collegeboard.org/",
                        "benefits": [
                            "Required for many college applications",
                            "Scholarship qualification",
                            "Standardized measure of college readiness"
                        ],
                        "preparation": "Regular practice tests and subject-specific study"
                    },
                    {
                        "name": "ACT (American College Testing)",
                        "description": "College admission test covering English, math, reading, and science",
                        "age_range": "Grades 11-12",
                        "regions": "Global",
                        "website": "https://www.act.org/",
                        "benefits": [
                            "Alternative to SAT for college applications",
                            "Includes science section",
                            "Scholarship qualification"
                        ],
                        "preparation": "Practice tests and subject-specific study"
                    },
                    {
                        "name": "Cambridge IGCSE",
                        "description": "International qualification for 14-16 year olds",
                        "age_range": "Ages 14-16",
                        "regions": "Global",
                        "website": "https://www.cambridgeinternational.org/",
                        "benefits": [
                            "Internationally recognized qualification",
                            "Subject-specific assessments",
                            "Preparation for further education"
                        ],
                        "preparation": "Following IGCSE curriculum with regular practice"
                    },
                    {
                        "name": "International Baccalaureate (IB) Diploma Programme",
                        "description": "Rigorous pre-university course of studies",
                        "age_range": "Ages 16-19",
                        "regions": "Global",
                        "website": "https://www.ibo.org/",
                        "benefits": [
                            "Internationally recognized qualification",
                            "Comprehensive educational approach",
                            "Highly regarded by universities worldwide"
                        ],
                        "preparation": "Two-year IB Diploma Programme coursework"
                    }
                ],
                "aptitude": [
                    {
                        "name": "Graduate Record Examinations (GRE)",
                        "description": "Standardized test for graduate school admissions",
                        "age_range": "High school seniors and above",
                        "regions": "Global",
                        "website": "https://www.ets.org/gre",
                        "benefits": [
                            "Required for many graduate programs",
                            "Measures verbal, quantitative, and analytical writing skills",
                            "Valid for five years"
                        ],
                        "preparation": "Practice tests and targeted study in verbal, quantitative, and analytical writing"
                    },
                    {
                        "name": "Graduate Management Admission Test (GMAT)",
                        "description": "Standardized test for business school admissions",
                        "age_range": "High school seniors and above",
                        "regions": "Global",
                        "website": "https://www.mba.com/exams/gmat",
                        "benefits": [
                            "Required for many business school programs",
                            "Measures analytical, writing, quantitative, and verbal skills",
                            "Specifically designed for business program success"
                        ],
                        "preparation": "Practice tests and targeted study in all test sections"
                    },
                    {
                        "name": "Law School Admission Test (LSAT)",
                        "description": "Standardized test for law school admissions",
                        "age_range": "High school seniors and above",
                        "regions": "Global",
                        "website": "https://www.lsac.org/",
                        "benefits": [
                            "Required for most law school programs",
                            "Measures reading comprehension and logical reasoning",
                            "Strong predictor of first-year law school success"
                        ],
                        "preparation": "Practice tests and targeted study in logical reasoning and reading comprehension"
                    }
                ],
                "competition": [
                    {
                        "name": "American Mathematics Competition (AMC 10/12)",
                        "description": "Mathematics competition for high school students",
                        "age_range": "Grades 9-12",
                        "regions": "Global (open to international students)",
                        "website": "https://www.maa.org/math-competitions",
                        "benefits": [
                            "Develops advanced mathematical problem-solving",
                            "Pathway to higher competitions (AIME, USAMO)",
                            "Recognition for mathematical talent"
                        ],
                        "preparation": "Regular practice with challenging math problems and competition preparation"
                    },
                    {
                        "name": "International Mathematical Olympiad (IMO)",
                        "description": "Prestigious international competition for high school students",
                        "age_range": "Under 20 years old",
                        "regions": "Global",
                        "website": "https://www.imo-official.org/",
                        "benefits": [
                            "Highest level of mathematical competition for secondary students",
                            "International recognition",
                            "Highly regarded by top universities"
                        ],
                        "preparation": "Extensive training in advanced mathematical problem-solving and proof techniques"
                    },
                    {
                        "name": "International Physics Olympiad (IPhO)",
                        "description": "Physics competition for high school students",
                        "age_range": "Under 20 years old",
                        "regions": "Global",
                        "website": "https://www.ipho-official.org/",
                        "benefits": [
                            "Develops advanced physics knowledge",
                            "International recognition",
                            "Highly regarded by science and engineering programs"
                        ],
                        "preparation": "In-depth study of physics beyond high school curriculum"
                    },
                    {
                        "name": "International Chemistry Olympiad (IChO)",
                        "description": "Chemistry competition for high school students",
                        "age_range": "Under 20 years old",
                        "regions": "Global",
                        "website": "https://www.icho-official.org/",
                        "benefits": [
                            "Develops advanced chemistry knowledge",
                            "International recognition",
                            "Highly regarded by science programs"
                        ],
                        "preparation": "In-depth study of chemistry beyond high school curriculum"
                    },
                    {
                        "name": "International Olympiad in Informatics (IOI)",
                        "description": "Computer programming competition for secondary school students",
                        "age_range": "Under 20 years old",
                        "regions": "Global",
                        "website": "https://ioinformatics.org/",
                        "benefits": [
                            "Develops advanced programming and algorithmic skills",
                            "International recognition",
                            "Highly regarded by computer science programs"
                        ],
                        "preparation": "Advanced programming practice and algorithm study"
                    }
                ],
                "talent_search": [
                    {
                        "name": "Research Science Institute (RSI)",
                        "description": "Summer research program for high school students",
                        "age_range": "High school juniors",
                        "regions": "Global",
                        "website": "https://www.cee.org/programs/research-science-institute",
                        "benefits": [
                            "Conduct original scientific research",
                            "Work with professional scientists",
                            "Highly regarded by top universities"
                        ],
                        "preparation": "Strong academic record and demonstrated interest in scientific research"
                    },
                    {
                        "name": "Program in Mathematics for Young Scientists (PROMYS)",
                        "description": "Summer program in mathematics for high school students",
                        "age_range": "High school students",
                        "regions": "Global",
                        "website": "https://promys.org/",
                        "benefits": [
                            "Explore advanced mathematical concepts",
                            "Develop mathematical thinking and research skills",
                            "Highly regarded by mathematics programs"
                        ],
                        "preparation": "Strong interest and ability in mathematics"
                    }
                ],
                "certification": [
                    {
                        "name": "Cambridge English: Advanced (CAE)",
                        "description": "High-level English language certification",
                        "age_range": "High school and above",
                        "regions": "Global",
                        "website": "https://www.cambridgeenglish.org/",
                        "benefits": [
                            "Internationally recognized advanced English certification",
                            "Accepted by universities worldwide",
                            "Valuable for academic and professional purposes"
                        ],
                        "preparation": "Advanced English language study and specific exam preparation"
                    },
                    {
                        "name": "IELTS (International English Language Testing System)",
                        "description": "English language proficiency test for study, work, and migration",
                        "age_range": "No minimum age (typically 16+)",
                        "regions": "Global",
                        "website": "https://www.ielts.org/",
                        "benefits": [
                            "Required for study and immigration in many countries",
                            "Recognized by over 10,000 organizations worldwide",
                            "Available in Academic and General Training formats"
                        ],
                        "preparation": "English language study and specific exam preparation"
                    },
                    {
                        "name": "TOEFL (Test of English as a Foreign Language)",
                        "description": "English language proficiency test for academic purposes",
                        "age_range": "No minimum age (typically 16+)",
                        "regions": "Global",
                        "website": "https://www.ets.org/toefl",
                        "benefits": [
                            "Required for non-native English speakers at many universities",
                            "Measures academic English proficiency",
                            "Recognized by over 11,000 institutions worldwide"
                        ],
                        "preparation": "Academic English study and specific exam preparation"
                    },
                    {
                        "name": "AP (Advanced Placement) Exams",
                        "description": "College-level exams in specific subject areas",
                        "age_range": "High school students",
                        "regions": "Global",
                        "website": "https://apstudents.collegeboard.org/",
                        "benefits": [
                            "Can earn college credit",
                            "Demonstrates subject mastery",
                            "Enhances college applications"
                        ],
                        "preparation": "AP courses and intensive subject study"
                    }
                ]
            }
        }
    
    def recommend_examinations(self, student_info, analysis_results):
        """
        Recommends globally available examinations based on student profile.
        
        Args:
            student_info (dict): Student information
            analysis_results (dict): Results from learning style analysis
            
        Returns:
            dict: Examination recommendations
        """
        # Extract relevant information
        age = student_info.get("age", 10)
        grade = student_info.get("grade", age - 5)  # Estimate grade if not provided
        
        learning_styles = analysis_results.get("learning_styles", {})
        traits = analysis_results.get("traits", {})
        interests = analysis_results.get("interests", {})
        
        primary_style = learning_styles.get("primary", "")
        top_traits = traits.get("top_traits", [])
        top_interests = interests.get("top_interests", [])
        
        # Determine age group
        if age <= 10:
            age_group = "elementary"
        elif age <= 13:
            age_group = "middle"
        else:
            age_group = "high"
        
        # Get examinations for the age group
        age_group_exams = self.examinations.get(age_group, {})
        
        # Select recommended examinations based on learning style, traits, and interests
        recommended_exams = self._select_recommended_exams(
            age_group_exams,
            primary_style,
            top_traits,
            top_interests
        )
        
        # Generate personalized recommendations
        personalized_recommendations = self._generate_personalized_recommendations(
            recommended_exams,
            primary_style,
            top_traits
        )
        
        # Generate preparation strategies
        preparation_strategies = self._generate_preparation_strategies(
            primary_style,
            top_traits
        )
        
        # Compile the complete recommendations
        exam_recommendations = {
            "age_group": age_group,
            "recommended_exams": recommended_exams,
            "personalized_recommendations": personalized_recommendations,
            "preparation_strategies": preparation_strategies
        }
        
        return exam_recommendations
    
    def _select_recommended_exams(self, age_group_exams, primary_style, top_traits, top_interests):
        """
        Selects recommended examinations based on learning style, traits, and interests.
        
        Args:
            age_group_exams (dict): Examinations for the age group
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            top_interests (list): Top interest areas
            
        Returns:
            dict: Selected examinations by category
        """
        recommended = {}
        
        # Define category weights based on learning style
        category_weights = {
            "visual": {
                "academic": 0.7,
                "aptitude": 0.8,
                "competition": 0.6,
                "talent_search": 0.7,
                "certification": 0.6
            },
            "auditory": {
                "academic": 0.8,
                "aptitude": 0.7,
                "competition": 0.5,
                "talent_search": 0.6,
                "certification": 0.7
            },
            "kinesthetic": {
                "academic": 0.6,
                "aptitude": 0.7,
                "competition": 0.8,
                "talent_search": 0.7,
                "certification": 0.6
            },
            "logical": {
                "academic": 0.7,
                "aptitude": 0.9,
                "competition": 0.8,
                "talent_search": 0.8,
                "certification": 0.6
            },
            "social": {
                "academic": 0.7,
                "aptitude": 0.6,
                "competition": 0.7,
                "talent_search": 0.6,
                "certification": 0.7
            },
            "independent": {
                "academic": 0.8,
                "aptitude": 0.8,
                "competition": 0.7,
                "talent_search": 0.8,
                "certification": 0.7
            }
        }
        
        # Get weights for the primary learning style
        weights = category_weights.get(primary_style, {
            "academic": 0.7,
            "aptitude": 0.7,
            "competition": 0.7,
            "talent_search": 0.7,
            "certification": 0.7
        })
        
        # Adjust weights based on traits
        if "analytical" in top_traits:
            weights["aptitude"] += 0.1
            weights["competition"] += 0.1
        if "creative" in top_traits:
            weights["talent_search"] += 0.1
        if "persistent" in top_traits:
            weights["competition"] += 0.1
            weights["certification"] += 0.1
        if "leadership" in top_traits:
            weights["talent_search"] += 0.1
        
        # Adjust weights based on interests
        interest_category_map = {
            "technology": ["certification", "competition"],
            "arts": ["talent_search", "certification"],
            "entrepreneurship": ["certification", "academic"],
            "science": ["competition", "talent_search"],
            "language": ["certification", "academic"],
            "mathematics": ["competition", "aptitude"]
        }
        
        for interest in top_interests:
            if interest in interest_category_map:
                for category in interest_category_map[interest]:
                    weights[category] += 0.1
        
        # Select top exams from each category based on weights
        for category, exams in age_group_exams.items():
            weight = weights.get(category, 0.7)
            num_to_select = max(1, int(len(exams) * weight))
            
            # Prioritize exams related to interests
            scored_exams = []
            for exam in exams:
                score = 1.0  # Base score
                
                # Increase score for exams related to interests
                exam_name = exam.get("name", "").lower()
                exam_desc = exam.get("description", "").lower()
                
                for interest in top_interests:
                    if interest.lower() in exam_name or interest.lower() in exam_desc:
                        score += 0.5
                
                scored_exams.append((score, exam))
            
            # Sort by score and select top exams
            scored_exams.sort(reverse=True)
            selected_exams = [exam for _, exam in scored_exams[:num_to_select]]
            
            recommended[category] = selected_exams
        
        return recommended
    
    def _generate_personalized_recommendations(self, recommended_exams, primary_style, top_traits):
        """
        Generates personalized examination recommendations.
        
        Args:
            recommended_exams (dict): Selected examinations by category
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            list: Personalized recommendations
        """
        recommendations = []
        
        # Add learning style-based recommendation
        style_recommendations = {
            "visual": "Focus on examinations that include visual elements, diagrams, or spatial reasoning. You may excel in aptitude tests with visual components and competitions that involve pattern recognition.",
            "auditory": "Consider examinations that allow for verbal processing or discussion. Language certifications and verbal reasoning sections of aptitude tests may align well with your learning style.",
            "kinesthetic": "Look for examinations with practical components or that allow for active engagement. Competitions with hands-on elements may be particularly engaging for your learning style.",
            "logical": "Your logical learning style is well-suited for aptitude tests and mathematical competitions. Focus on examinations that involve systematic problem-solving and analytical thinking.",
            "social": "Consider participating in team-based competitions or collaborative examination preparation. Your social learning style can be an advantage in group settings.",
            "independent": "Your independent learning style is well-suited for self-directed examination preparation. Focus on developing personalized study strategies for your chosen examinations."
        }
        
        if primary_style in style_recommendations:
            recommendations.append(style_recommendations[primary_style])
        
        # Add trait-based recommendation
        trait_recommendations = {
            "analytical": "Your analytical nature will be an asset in examinations requiring detailed analysis and critical thinking. Consider aptitude tests and academic competitions that reward careful reasoning.",
            "creative": "Your creative thinking can be valuable in examinations with open-ended components. Look for opportunities that allow you to demonstrate innovative approaches to problems.",
            "persistent": "Your persistence will serve you well in preparing for challenging examinations. Consider competitions or certifications that require sustained effort and practice.",
            "leadership": "Your leadership qualities can be showcased through participation in team competitions or talent search programs that value initiative and direction.",
            "collaborative": "Your collaborative nature can enhance group preparation for examinations. Consider forming study groups for academic tests or participating in team competitions.",
            "organized": "Your organizational skills will be valuable in managing examination preparation. Create structured study plans for your chosen examinations to maximize effectiveness."
        }
        
        if top_traits and top_traits[0] in trait_recommendations:
            recommendations.append(trait_recommendations[top_traits[0]])
        
        # Add category-specific recommendations
        if recommended_exams.get("academic"):
            recommendations.append("Academic assessments like " + 
                                  recommended_exams["academic"][0]["name"] + 
                                  " will provide valuable benchmarking of your academic progress and help identify areas for growth.")
        
        if recommended_exams.get("aptitude"):
            recommendations.append("Aptitude tests like " + 
                                  recommended_exams["aptitude"][0]["name"] + 
                                  " can help identify your inherent strengths and potential, providing insights for educational and career planning.")
        
        if recommended_exams.get("competition"):
            recommendations.append("Competitions like " + 
                                  recommended_exams["competition"][0]["name"] + 
                                  " offer opportunities to challenge yourself, develop advanced skills, and gain recognition for your abilities.")
        
        if recommended_exams.get("certification"):
            recommendations.append("Certifications like " + 
                                  recommended_exams["certification"][0]["name"] + 
                                  " provide recognized credentials that can enhance your academic profile and future opportunities.")
        
        # Add balanced approach recommendation
        recommendations.append("Consider a balanced approach to examinations, including a mix of academic assessments, aptitude tests, competitions, and certifications to develop a well-rounded profile and diverse set of experiences.")
        
        return recommendations
    
    def _generate_preparation_strategies(self, primary_style, top_traits):
        """
        Generates examination preparation strategies based on learning style and traits.
        
        Args:
            primary_style (str): Primary learning style
            top_traits (list): Top personality traits
            
        Returns:
            list: Preparation strategies
        """
        # General strategies
        general_strategies = [
            "Start preparation well in advance of examination dates",
            "Familiarize yourself with examination format and requirements",
            "Practice with sample questions or past papers",
            "Develop a consistent study schedule",
            "Balance preparation with regular breaks and self-care"
        ]
        
        # Learning style-specific strategies
        style_strategies = {
            "visual": [
                "Use visual study aids like mind maps, diagrams, and charts",
                "Color-code notes and study materials",
                "Convert text information into visual formats",
                "Use flashcards with visual cues",
                "Practice with visual practice questions and problems"
            ],
            "auditory": [
                "Record and listen to study materials",
                "Discuss concepts verbally with others",
                "Use mnemonic devices and verbal repetition",
                "Participate in study groups with discussion",
                "Read important information aloud"
            ],
            "kinesthetic": [
                "Incorporate movement into study sessions",
                "Use hands-on practice whenever possible",
                "Take breaks for physical activity",
                "Create physical models or manipulatives",
                "Practice writing out solutions and answers"
            ],
            "logical": [
                "Organize study materials in logical sequences",
                "Create systematic study plans",
                "Look for patterns and connections between concepts",
                "Break down complex problems into logical steps",
                "Practice with problem-solving questions"
            ],
            "social": [
                "Form study groups",
                "Teach concepts to others",
                "Discuss practice questions with peers",
                "Use collaborative study techniques",
                "Seek feedback from teachers or mentors"
            ],
            "independent": [
                "Create personalized study schedules",
                "Find quiet, focused study environments",
                "Set individual study goals",
                "Self-test regularly",
                "Reflect on and adjust study strategies as needed"
            ]
        }
        
        # Trait-specific strategies
        trait_strategies = {
            "analytical": [
                "Practice analyzing complex questions",
                "Develop systematic approaches to different question types",
                "Focus on understanding underlying principles",
                "Review mistakes analytically to identify patterns"
            ],
            "creative": [
                "Look for creative connections between concepts",
                "Develop multiple approaches to problem-solving",
                "Create memorable associations for key information",
                "Use creative study methods like storytelling or visualization"
            ],
            "persistent": [
                "Set incremental goals for sustained progress",
                "Track progress to maintain motivation",
                "Develop strategies for overcoming challenging content",
                "Build regular review into study plans"
            ],
            "leadership": [
                "Take initiative in organizing study groups",
                "Help peers understand difficult concepts",
                "Set example with disciplined study habits",
                "Coordinate collaborative preparation efforts"
            ],
            "collaborative": [
                "Share resources and study materials with peers",
                "Participate actively in study groups",
                "Give and receive constructive feedback",
                "Develop collaborative problem-solving skills"
            ],
            "organized": [
                "Create detailed study plans and schedules",
                "Maintain organized notes and resources",
                "Use checklists to track preparation progress",
                "Systematically review all required content"
            ]
        }
        
        # Compile strategies
        strategies = general_strategies.copy()
        
        # Add learning style-specific strategies
        if primary_style in style_strategies:
            strategies.extend(style_strategies[primary_style][:3])  # Add top 3 style strategies
        
        # Add trait-specific strategies
        if top_traits and top_traits[0] in trait_strategies:
            strategies.extend(trait_strategies[top_traits[0]][:2])  # Add top 2 trait strategies
        
        # Add exam-specific strategies
        strategies.extend([
            "For academic assessments: Focus on thorough understanding of curriculum content",
            "For aptitude tests: Practice with diverse problem types to develop flexible thinking",
            "For competitions: Study beyond standard curriculum and practice with challenging problems",
            "For certifications: Focus on meeting specific requirements and standards"
        ])
        
        return strategies
