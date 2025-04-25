"""
Diagnostic Questionnaire for K-12 Students
This module contains the questions for the diagnostic assessment.
"""

# Age group categories
AGE_GROUPS = {
    "elementary": {"min_age": 5, "max_age": 10},  # K-5
    "middle": {"min_age": 11, "max_age": 13},     # 6-8
    "high": {"min_age": 14, "max_age": 18}        # 9-12
}

# Question categories
CATEGORIES = [
    "learning_style",
    "problem_solving",
    "behavior",
    "creativity",
    "time_management",
    "communication",
    "interests"
]

# Common questions for all age groups
COMMON_QUESTIONS = [
    {
        "id": "ls_1",
        "category": "learning_style",
        "type": "multiple_choice",
        "question": "When learning something new, I prefer to:",
        "options": [
            "Watch videos or demonstrations",
            "Listen to someone explain it",
            "Try it out myself",
            "Read about it first"
        ],
        "learning_style_mapping": ["visual", "auditory", "kinesthetic", "logical"]
    },
    {
        "id": "ls_2",
        "category": "learning_style",
        "type": "multiple_choice",
        "question": "I remember things best when I:",
        "options": [
            "See pictures or diagrams",
            "Hear the information",
            "Do hands-on activities",
            "Organize information in my head"
        ],
        "learning_style_mapping": ["visual", "auditory", "kinesthetic", "logical"]
    },
    {
        "id": "ls_3",
        "category": "learning_style",
        "type": "multiple_choice",
        "question": "When working on a project, I prefer to:",
        "options": [
            "Work with a group of friends",
            "Work by myself",
            "Have a teacher or parent help me",
            "Switch between working alone and with others"
        ],
        "learning_style_mapping": ["social", "independent", "guided", "flexible"]
    },
    {
        "id": "ps_1",
        "category": "problem_solving",
        "type": "situational",
        "question": "If you get stuck on a difficult problem, what do you usually do first?",
        "options": [
            "Look for similar examples to follow",
            "Ask someone for help right away",
            "Try different approaches until something works",
            "Take a break and come back to it later"
        ],
        "trait_mapping": ["example-based", "help-seeking", "persistent", "reflective"]
    },
    {
        "id": "bh_1",
        "category": "behavior",
        "type": "situational",
        "question": "When left alone with a task, I usually:",
        "options": [
            "Follow the instructions exactly",
            "Find my own way to complete it",
            "Get distracted and do something else",
            "Feel unsure about what to do next"
        ],
        "trait_mapping": ["structured", "independent", "distractible", "guidance-seeking"]
    },
    {
        "id": "cr_1",
        "category": "creativity",
        "type": "situational",
        "question": "When asked to create something new, I prefer to:",
        "options": [
            "Follow a template or example",
            "Combine ideas from different sources",
            "Come up with something completely original",
            "Improve on existing ideas"
        ],
        "trait_mapping": ["structured", "combinatorial", "innovative", "iterative"]
    },
    {
        "id": "tm_1",
        "category": "time_management",
        "type": "situational",
        "question": "When working on a project with a deadline, I usually:",
        "options": [
            "Start right away and finish early",
            "Make a plan and follow it step by step",
            "Wait until closer to the deadline to start",
            "Work on it a little bit each day"
        ],
        "trait_mapping": ["proactive", "methodical", "pressure-driven", "consistent"]
    },
    {
        "id": "cm_1",
        "category": "communication",
        "type": "multiple_choice",
        "question": "When explaining my ideas to others, I prefer to:",
        "options": [
            "Draw pictures or diagrams",
            "Write them down in detail",
            "Act them out or demonstrate",
            "Explain them verbally"
        ],
        "trait_mapping": ["visual", "written", "demonstrative", "verbal"]
    },
    {
        "id": "in_1",
        "category": "interests",
        "type": "multiple_choice",
        "question": "Which of these activities do you enjoy the most?",
        "options": [
            "Solving puzzles or math problems",
            "Creating art or music",
            "Building or making things",
            "Reading or writing stories"
        ],
        "interest_mapping": ["math", "arts", "tech", "language"]
    },
    {
        "id": "in_2",
        "category": "interests",
        "type": "multiple_choice",
        "question": "If you could learn more about one of these topics, which would you choose?",
        "options": [
            "Robots and coding",
            "Starting your own business",
            "Art and design",
            "Science experiments"
        ],
        "interest_mapping": ["tech", "entrepreneurship", "arts", "science"]
    }
]

# Elementary school specific questions (K-5)
ELEMENTARY_QUESTIONS = [
    {
        "id": "elem_1",
        "category": "learning_style",
        "type": "multiple_choice",
        "question": "When learning about animals, I would rather:",
        "options": [
            "Look at pictures of animals",
            "Listen to animal sounds",
            "Visit a zoo to see real animals",
            "Read facts about animals"
        ],
        "learning_style_mapping": ["visual", "auditory", "kinesthetic", "logical"]
    },
    {
        "id": "elem_2",
        "category": "problem_solving",
        "type": "logic_puzzle",
        "question": "Which shape comes next in this pattern? [Square, Circle, Triangle, Square, Circle, ?]",
        "options": [
            "Triangle",
            "Square",
            "Circle",
            "Rectangle"
        ],
        "correct_answer": "Triangle",
        "trait_mapping": ["pattern_recognition"]
    },
    {
        "id": "elem_3",
        "category": "creativity",
        "type": "situational",
        "question": "If you could invent a new toy, what would it do?",
        "options": [
            "It would fly or move by itself",
            "It would change colors or shapes",
            "It would teach you new things",
            "It would tell stories or play music"
        ],
        "trait_mapping": ["mechanical", "visual", "educational", "entertainment"]
    },
    {
        "id": "elem_4",
        "category": "behavior",
        "type": "situational",
        "question": "When playing with friends, I usually:",
        "options": [
            "Like to be the leader",
            "Follow what others want to do",
            "Suggest new games to play",
            "Play by myself sometimes"
        ],
        "trait_mapping": ["leadership", "cooperative", "innovative", "independent"]
    },
    {
        "id": "elem_5",
        "category": "interests",
        "type": "visual_reasoning",
        "question": "Which picture shows something you'd like to learn more about?",
        "options": [
            "Computer/tablet with code on screen",
            "Art supplies and paintings",
            "Sports equipment",
            "Books and writing materials"
        ],
        "interest_mapping": ["tech", "arts", "physical", "language"]
    }
]

# Middle school specific questions (6-8)
MIDDLE_SCHOOL_QUESTIONS = [
    {
        "id": "mid_1",
        "category": "learning_style",
        "type": "multiple_choice",
        "question": "When working on a science project, I prefer to:",
        "options": [
            "Design and conduct experiments",
            "Research facts and information online",
            "Create visual models or diagrams",
            "Discuss ideas with classmates"
        ],
        "learning_style_mapping": ["kinesthetic", "logical", "visual", "social"]
    },
    {
        "id": "mid_2",
        "category": "problem_solving",
        "type": "logic_puzzle",
        "question": "If RED = 27, BLUE = 39, what does GREEN equal?",
        "options": [
            "57",
            "65",
            "52",
            "48"
        ],
        "correct_answer": "57",
        "trait_mapping": ["analytical"]
    },
    {
        "id": "mid_3",
        "category": "creativity",
        "type": "situational",
        "question": "If you could design an app, what would it do?",
        "options": [
            "Help people learn something new",
            "Connect people with similar interests",
            "Solve an everyday problem",
            "Create or share art, music, or stories"
        ],
        "trait_mapping": ["educational", "social", "practical", "creative"]
    },
    {
        "id": "mid_4",
        "category": "time_management",
        "type": "situational",
        "question": "When you have multiple homework assignments due, how do you handle it?",
        "options": [
            "Start with the easiest ones first",
            "Start with the most difficult ones first",
            "Start with the ones due soonest",
            "Make a schedule and follow it"
        ],
        "trait_mapping": ["confidence-building", "challenge-seeking", "deadline-driven", "organized"]
    },
    {
        "id": "mid_5",
        "category": "interests",
        "type": "multiple_choice",
        "question": "Which of these activities sounds most interesting to you?",
        "options": [
            "Building a website or creating a game",
            "Starting a small business",
            "Creating videos or digital art",
            "Conducting science experiments"
        ],
        "interest_mapping": ["tech", "entrepreneurship", "media", "science"]
    },
    {
        "id": "mid_6",
        "category": "communication",
        "type": "situational",
        "question": "When working on a group project, I usually:",
        "options": [
            "Take charge and assign tasks",
            "Focus on my part and let others handle theirs",
            "Help organize everyone's ideas",
            "Come up with creative solutions"
        ],
        "trait_mapping": ["leadership", "independent", "collaborative", "innovative"]
    }
]

# High school specific questions (9-12)
HIGH_SCHOOL_QUESTIONS = [
    {
        "id": "high_1",
        "category": "learning_style",
        "type": "multiple_choice",
        "question": "When preparing for an exam, I usually:",
        "options": [
            "Create visual study guides or mind maps",
            "Record and listen to key information",
            "Practice with sample problems or flashcards",
            "Explain concepts to someone else"
        ],
        "learning_style_mapping": ["visual", "auditory", "kinesthetic", "social"]
    },
    {
        "id": "high_2",
        "category": "problem_solving",
        "type": "logic_puzzle",
        "question": "In a certain code, KNOWLEDGE is written as MPQYNGFIG. How would EDUCATION be written in that code?",
        "options": [
            "GFWECVKQP",
            "GFWEVKQPC",
            "GFWECVKQP",
            "GFWECKQPV"
        ],
        "correct_answer": "GFWECVKQP",
        "trait_mapping": ["pattern_recognition"]
    },
    {
        "id": "high_3",
        "category": "creativity",
        "type": "open_ended",
        "question": "Describe a solution to a real-world problem you'd like to solve.",
        "trait_mapping": ["innovative", "practical", "visionary"]
    },
    {
        "id": "high_4",
        "category": "time_management",
        "type": "situational",
        "question": "When facing a long-term project, I typically:",
        "options": [
            "Break it down into smaller tasks with deadlines",
            "Focus intensely on it for long periods",
            "Work on it when I feel inspired",
            "Collaborate with others to divide the work"
        ],
        "trait_mapping": ["structured", "focused", "intuitive", "collaborative"]
    },
    {
        "id": "high_5",
        "category": "interests",
        "type": "multiple_choice",
        "question": "Which career field interests you the most?",
        "options": [
            "Technology and computer science",
            "Business and entrepreneurship",
            "Arts, design, or communication",
            "Science, research, or medicine"
        ],
        "interest_mapping": ["tech", "entrepreneurship", "creative", "science"]
    },
    {
        "id": "high_6",
        "category": "communication",
        "type": "situational",
        "question": "When presenting information to others, I prefer to:",
        "options": [
            "Use visual aids like slides or videos",
            "Prepare a detailed written report",
            "Create an interactive demonstration",
            "Lead a discussion or debate"
        ],
        "trait_mapping": ["visual", "written", "interactive", "verbal"]
    },
    {
        "id": "high_7",
        "category": "behavior",
        "type": "situational",
        "question": "When faced with a challenging task, I usually:",
        "options": [
            "Research different approaches before starting",
            "Jump in and learn as I go",
            "Seek advice from someone with experience",
            "Look for creative alternatives to the standard approach"
        ],
        "trait_mapping": ["analytical", "experiential", "guidance-seeking", "innovative"]
    },
    {
        "id": "high_8",
        "category": "open_ended",
        "type": "open_ended",
        "question": "What do you see yourself doing 5 years from now?",
        "trait_mapping": ["future_orientation", "goal_setting", "self_awareness"]
    }
]

# Parent mirror questions
PARENT_MIRROR_QUESTIONS = [
    {
        "id": "parent_1",
        "category": "learning_style",
        "type": "multiple_choice",
        "question": "How do you think your child prefers to learn new information?",
        "options": [
            "By seeing visual examples or demonstrations",
            "By listening to explanations",
            "By doing hands-on activities",
            "By reading and analyzing information"
        ],
        "learning_style_mapping": ["visual", "auditory", "kinesthetic", "logical"]
    },
    {
        "id": "parent_2",
        "category": "behavior",
        "type": "multiple_choice",
        "question": "When your child is left alone with a task, how do they typically behave?",
        "options": [
            "Follow instructions exactly",
            "Find their own way to complete it",
            "Get distracted easily",
            "Ask for help frequently"
        ],
        "trait_mapping": ["structured", "independent", "distractible", "guidance-seeking"]
    },
    {
        "id": "parent_3",
        "category": "problem_solving",
        "type": "multiple_choice",
        "question": "How does your child usually approach difficult problems?",
        "options": [
            "Looks for examples to follow",
            "Asks for help right away",
            "Tries different approaches until something works",
            "Takes a break and returns to it later"
        ],
        "trait_mapping": ["example-based", "help-seeking", "persistent", "reflective"]
    },
    {
        "id": "parent_4",
        "category": "creativity",
        "type": "multiple_choice",
        "question": "How creative do you consider your child to be?",
        "options": [
            "Very creative, always coming up with original ideas",
            "Somewhat creative, builds on existing ideas",
            "Prefers following established patterns",
            "Creativity varies depending on the subject"
        ],
        "trait_mapping": ["highly_creative", "moderately_creative", "structured", "context_dependent"]
    },
    {
        "id": "parent_5",
        "category": "interests",
        "type": "multiple_choice",
        "question": "Which area do you think your child shows the most interest in?",
        "options": [
            "Technology and computers",
            "Arts and creative activities",
            "Social activities and leadership",
            "Academic subjects and learning"
        ],
        "interest_mapping": ["tech", "arts", "social", "academic"]
    }
]

def get_questions_for_age(age):
    """
    Returns appropriate questions based on student age.
    
    Args:
        age (int): The age of the student
        
    Returns:
        list: List of question dictionaries appropriate for the age
    """
    questions = COMMON_QUESTIONS.copy()
    
    if age >= AGE_GROUPS["elementary"]["min_age"] and age <= AGE_GROUPS["elementary"]["max_age"]:
        questions.extend(ELEMENTARY_QUESTIONS)
    elif age >= AGE_GROUPS["middle"]["min_age"] and age <= AGE_GROUPS["middle"]["max_age"]:
        questions.extend(MIDDLE_SCHOOL_QUESTIONS)
    elif age >= AGE_GROUPS["high"]["min_age"] and age <= AGE_GROUPS["high"]["max_age"]:
        questions.extend(HIGH_SCHOOL_QUESTIONS)
    
    return questions

def get_parent_questions():
    """
    Returns questions for parents to answer about their child.
    
    Returns:
        list: List of question dictionaries for parents
    """
    return PARENT_MIRROR_QUESTIONS
