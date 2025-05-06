# Functions to create surveys in Canvas

# Package imports
from canvasapi.quiz import Quiz
from canvasapi.course import Course
import json


# Functions
def add_question_to_quiz(quiz: Quiz, quiz_question: dict):
    """Adds a question to a Canvas quiz."""
    quiz.create_question(question=quiz_question)


def prepare_quiz_question_simple(question_settings: dict, position: int):
    """Prepares a simple quiz question."""
    quiz_question = {
        "id": position,
        "position": position,
        "points_possible": 0,
        "question_name": question_settings["question_name"],
        "question_text": question_settings["question_text"],
        "question_type": question_settings["question_type"]
    }

    return quiz_question


def prepare_quiz_question_table_of_dropdowns(question_settings: dict, position: int):
    """Prepares a quiz question comprised of a table of dropdowns."""
    # Elements to create the QuizQuestion question_text
    questions = question_settings["questions"]
    scale = question_settings["scale"]
    question_text_template = question_settings["question_text_template"]
    indicator_template = question_settings["indicator_template"]
    question_template = question_settings["question_template"]

    # Create question indicators
    indicators = [indicator_template.format(I=i+1) for i in range(len(questions))]

    # Create answers
    answers = []
    for indicator in indicators:
        new_answers = [{"text": answer, "blank_id": indicator} for answer in scale]
        answers += new_answers

    # Create question text
    formatted_questions = ""
    for question, indicator in zip(questions, indicators):
        formatted_questions += question_template.format(QUESTION=question, INDICATOR=indicator)

    # Create QuizQuestion
    quiz_question = {
        "id": position,
        "position": position,
        "points_possible": 0,
        "question_name": question_settings["question_name"],
        "question_text": question_text_template.format(QUESTIONS=formatted_questions),
        "question_type": question_settings["question_type"],
        "answers": answers
    }

    return quiz_question


def prepare_quiz_question_multiple_choice(question_settings: dict, position: int):
    """Prepares a multiple choice quiz question."""
    scale = question_settings["scale"]

    # Create answers
    answers = [{"text": answer} for answer in scale]

    # Create QuizQuestion
    quiz_question = {
        "id": position,
        "position": position,
        "points_possible": 0,
        "question_name": question_settings["question_name"],
        "question_text": question_settings["question_text"],
        "question_type": question_settings["question_type"],
        "answers": answers
    }

    return quiz_question

def prepare_quiz_question(question_path: dict, position: int):
    """Prepares a quiz question based on its type."""
    with open(question_path) as f:
        question_settings = json.load(f)

    if question_settings["question_type"] == "multiple_choice_question":
        return prepare_quiz_question_multiple_choice(question_settings, position)
    elif question_settings["question_type"] == "multiple_dropdowns_question":
        return prepare_quiz_question_table_of_dropdowns(question_settings, position)
    else:
        return prepare_quiz_question_simple(question_settings, position)
        

def create_survey(course: Course, survey_definition: dict, survey_questions: dict) -> Quiz:
    """Creates a survey in a Canvas course."""
    # Create the quiz
    quiz_data = {
        "title": survey_definition["title"],
        "description": survey_definition["description"],
        "quiz_type": "survey",
        "one_question_at_a_time": True,
        "published": False,
    }
    quiz = course.create_quiz(quiz = quiz_data)

    # Add questions to the quiz
    for i, question in enumerate(survey_definition["questions"]):
        quiz_question = prepare_quiz_question(survey_questions[question], i)
        add_question_to_quiz(quiz, quiz_question)

    return quiz