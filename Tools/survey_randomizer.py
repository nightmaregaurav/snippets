import json
import random

TOTAL_ENTRIES_TO_GENERATE = 250

data = {    
    "How frequently do you use public transportation in Kathmandu Valley?": [
        ("Daily", 5),
        ("Several times a week", 4),
        ("Once a week", 3),
        ("Rarely", 2),
        ("Never", 1)
    ],
    "Which mode of public transportation do you most frequently use?": [
        ("Buses", 5),
        ("Micro-buses", 4),
        ("Taxis", 2),
        ("Tempos", 3)
    ],
    "On a scale of 1 to 5, how satisfied are you with the cleanliness of public transportation vehicles?": [
        ("1 (Very Dissatisfied)", 5),
        ("2 (Dissatisfied)", 4),
        ("3 (Neutral)", 3),
        ("4 (Satisfied)", 2),
        ("5 (Very Satisfied)", 1)
    ],
    "How would you rate the punctuality of public transportation services?": [
        ("Very Poor", 5),
        ("Poor", 4),
        ("Neutral", 3),
        ("Good", 2),
        ("Very Good", 1)
    ],
    "Do you feel safe while using public transportation in Kathmandu Valley?": [
        ("Not at all safe", 3),
        ("Somewhat safe", 4),
        ("Moderately safe", 4),
        ("Very safe", 3),
        ("Extremely safe", 1)
    ],
    "What factors influence your decision to use public transportation? (Select that apply the most)": [
        ("Affordability", 5),
        ("Convenience", 4),
        ("Availability of routes", 3),
        ("Time efficiency", 2),
        ("Environmental concerns", 1)
    ],
    "In your opinion, what aspects of public transportation need the most improvement in Kathmandu Valley? (Select that apply the most)": [
        ("Vehicle condition and cleanliness", 6),
        ("Punctuality and reliability", 5),
        ("Safety measures and driver behavior", 5),
        ("Comfort and overcrowding", 5),
        ("Route planning and information", 3)
    ],
    "What time of day do you most frequently use public transportation?": [
        ("Morning (6 AM - 10 AM)", 6),
        ("Midday (10 AM - 3 PM)", 2),
        ("Afternoon (3 PM - 7 PM)", 6),
        ("Evening (7 PM - 10 PM)", 2),
        ("Night (10 PM - 6 AM)", 1)
    ],
    "How far is your typical public transportation journey?": [
        ("Short distance (within 5 km)", 4),
        ("Medium distance (5 - 15 km)", 5),
        ("Long distance (15 km or more)", 4)
    ],
    "Do you find public transportation stops/stations easily accessible from your location?": [
        ("Very Difficult", 1),
        ("Difficult", 2),
        ("Neutral", 5),
        ("Easy", 4),
        ("Very Easy", 4)
    ],
    "How often do you encounter difficulties finding accurate information about public transportation routes and schedules?": [
        ("Very Often", 2),
        ("Often", 2),
        ("Sometimes", 2),
        ("Rarely", 5),
        ("Never", 2)
    ],
    "Have you ever used ride-hailing services (e.g., Indrive, Pathao) as an alternative to public transportation in Kathmandu Valley?": [
        ("Yes, frequently", 3),
        ("Yes, occasionally", 6),
        ("No, never", 2)
    ],
    "If you've used ride-hailing services, what influenced your decision to choose them over public transportation? (Select that apply the most)": [
        ("Convenience", 3),
        ("Speed", 4),
        ("Comfort", 3),
        ("Safety", 3),
        ("Reliability", 3)
    ],
    "Do you think using public transportation is more environmentally friendly compared to private vehicles?": [
        ("Strongly Agree", 3),
        ("Agree", 3),
        ("Neutral", 3),
        ("Disagree", 2),
        ("Strongly Disagree", 2)
    ],
    "On a scale of 1 to 10, how likely are you to recommend the use of public transportation to others?": [
        ("1", 1),
        ("2", 2),
        ("3", 5),
        ("4", 4),
        ("5", 5),
        ("6", 4),
        ("7", 4),
        ("8", 4),
        ("9", 4),
        ("10", 4)
    ]
}

def generate_answer(options):
    weighted_options = []
    for option, priority in options:
        weighted_options.extend([option] * priority)
    return random.choice(weighted_options)

questions = list(data.keys())
answers = []
for _ in range(TOTAL_ENTRIES_TO_GENERATE):
    answers.append([generate_answer(options) for _, options in data.items()])

final = {
    "q": questions,
    "a": answers 
}

with open("out.json", "w") as json_file:
    json.dump(final, json_file, indent=4)
