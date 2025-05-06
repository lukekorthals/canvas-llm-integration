# General utility functions for the project

# Package imports
import json
import numpy as np
import os
import pandas as pd
import re
from typing import Tuple
import yaml


# Functions
def ensure_folder_exists(folder_path):
    # Remove filename if provided
    if "." in folder_path:
        folder_path = "/".join(folder_path.split("/")[:-1])
    # Create folder if not exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def create_file_list(path: str, indicators_pos: list = [], indicators_neg: list = [], sort: callable = None):
    """Gets all files in a directory according to the indicators"""
                
    # create condition based on all indicators
    condition_pos = lambda x: all([indicator in x for indicator in indicators_pos])
    condition_neg = lambda x: all([indicator not in x for indicator in indicators_neg])
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if condition_pos(file) and condition_neg(file):
                file_list.append(os.path.join(root, file))
    return file_list


def load_json(filepath: str):
    """Loads a json file"""
    
    with open(filepath, "r") as file:
        data = json.load(file)
    return data


def read_files_to_dict(path_dict: dict) -> dict:
    """Replaces a dictionary of file paths with a dictionary of file contents."""
    for key, path in path_dict.items():
        with open(path) as f:
            path_dict[key] = f.read()
    return path_dict


def load_jsonified_resources(assignment_nr: int, resources_path: str = "resources", keys: list = ["questions", "rubrics", "solutions", "goals"]) -> dict:
    """Loads jsonified questions, rubrics, solutions, and learning goals for a given week."""
    base_path = f"{resources_path}/assignment-{assignment_nr}/json/assignment-{assignment_nr}"
    jsonified_resources = {}
    for key in keys:
        jsonified_resources[key] = json.load(open(f"{base_path}_{key}.json"))
        jsonified_resources[key] = {k: "\n".join(v) for k, v in jsonified_resources[key].items()}   
    return jsonified_resources 


def deduplicate_highest_attempt(file_paths):
    """
    Finds the highest attempt for each unique file (ignoring `try-(\d+)`) 
    and returns the list of file paths with the highest attempt.
    """
    submission_dict = {}

    for path in file_paths:
        # Remove try-(\d+) to get the unique key
        normalized_path = re.sub(r'try-\d+', 'try-', path)
        match = re.search(r'try-(\d+)', path)
        
        attempt_number = int(match.group(1)) if match else 0
        
        # Keep the path with the highest attempt
        if normalized_path not in submission_dict or attempt_number > submission_dict[normalized_path][1]:
            submission_dict[normalized_path] = (path, attempt_number)

    return [value[0] for value in submission_dict.values()]

def deduplicate_files_with_manual_fixes(file_list):

    # Helper function to extract que and att identifiers from a filename
    def extract_identifiers(filename):
        match = re.search(r'try-(\d+)_que-(\d+)_att-(\d+)', filename)
        if match:
            return match.group(1), match.group(2), match.group(3)
        return None, None

    # Dictionary to hold the preferred file for each identifier pair
    preferred_files = {}

    for file in file_list:
        try_, que, att = extract_identifiers(file)
        if (try_, que, att) == (None, None):
            continue  # Skip files that don't match the pattern

        if (try_, que, att) not in preferred_files or "ManualFixes" in file:
            # Update if no file is recorded yet or if this file has "ManualFixes"
            preferred_files[(try_, que, att)] = file

    # Return the list of preferred files
    return list(preferred_files.values())

def load_settings_to_globals(settings_path, week_nr) -> None:
    """Loads the settings to set global variables"""
    # Load settings
    with open(settings_path) as f:
            settings = yaml.safe_load(f)

    # Week
    global WEEK_NUMBER 
    global WEEK
    WEEK_NUMBER = week_nr
    WEEK = settings["weeks"][week_nr]

    # Canvas settings
    global COURSE_ID
    global ASSIGNMENT_ID
    global QUIZ_ID
    global R_QUIZ_QUESTION_ID
    global ADV_QUIZ_QUESTION_ID
    global LOCK_GRADES_DATE
    COURSE_ID = settings["global"]["canvas"]["course_id"]
    ASSIGNMENT_ID = WEEK["canvas"]["assignment_id"]
    QUIZ_ID = WEEK["canvas"]["quiz_id"]
    R_QUIZ_QUESTION_ID = WEEK["canvas"]["r_quiz_question_id"]
    ADV_QUIZ_QUESTION_ID = WEEK["canvas"]["adv_quiz_question_id"]
    LOCK_GRADES_DATE = WEEK["lock_grades_date"]


    # LLM Settings
    global MODEL
    global GRADING_TEMPERATURE
    global FEEDBACK_TEMPERATURE
    global N_CHOICES_GRADING
    global N_CHOICES_FEEDBACK
    global PROMPTS
    MODEL = settings["global"]["llm"]["model"]
    GRADING_TEMPERATURE = settings["global"]["llm"]["grading_temperature"]
    FEEDBACK_TEMPERATURE = settings["global"]["llm"]["feedback_temperature"]
    N_CHOICES_GRADING = settings["global"]["llm"]["n_choices_grading"]
    N_CHOICES_FEEDBACK = settings["global"]["llm"]["n_choices_feedback"]
    PROMPTS = {k: read_files_to_dict(settings["global"]["llm"]["prompts"][k]) for k in settings["global"]["llm"]["prompts"].keys()}
    
    # Paths
    global RESOURCES_PATH
    global SUBMISSIONS_PATH
    global STUDENT_SUBMISSION_TEMPLATE
    global STUDENT_SUBMISSION_JSON_TEMPLATE
    global LLM_COMPLETION_REPORT_TEMPLATE
    global LLM_FEEDBACK_REPORT_TEMPLATE
    global LLM_GRADING_REPORT_TEMPLATE
    RESOURCES_PATH = settings["global"]["paths"]["resources"]
    SUBMISSIONS_PATH = settings["global"]["paths"]["submissions"]
    STUDENT_SUBMISSION_TEMPLATE = settings["global"]["paths"]["student_submission_template"]
    STUDENT_SUBMISSION_JSON_TEMPLATE = settings["global"]["paths"]["student_submission_json_template"]
    LLM_COMPLETION_REPORT_TEMPLATE = settings["global"]["paths"]["llm_completion_report_template"]
    LLM_FEEDBACK_REPORT_TEMPLATE = settings["global"]["paths"]["llm_feedback_report_template"]
    LLM_GRADING_REPORT_TEMPLATE = settings["global"]["paths"]["llm_grading_report_template"]

    # Randomization 
    global GROUPS
    global SEED
    GROUPS = settings["global"]["randomization"]["groups"]
    SEED = settings["global"]["randomization"]["seed"]

    # Surveys
    global SURVEY_QUESTIONS
    global SURVEY_DEFINITIONS
    SURVEY_QUESTIONS = settings["surveys"]["survey_questions"]
    SURVEY_DEFINITIONS = settings["surveys"]["survey_definitions"]


def parsed_submissions_quality_check(assignment_nr, assignment_id, submissions_path="submissions", resources_path="resources"):
    # Get most recent jsonified submissions
    jsonified_submissions = create_file_list(path=submissions_path, indicators_pos=[".json", f"ass-{assignment_id}"])
    jsonified_submissions = deduplicate_files_with_manual_fixes(jsonified_submissions)
    jsonified_submissions = deduplicate_highest_attempt(jsonified_submissions)

    # Get required indicators
    required_indicators = list(json.load(open(create_file_list(resources_path, [f"assignment-{assignment_nr}_questions.json"])[0])).keys())
    
    # Get user ids
    user_ids = {re.compile(r"user-(\d+)").search(submission).group(1) for submission in jsonified_submissions}
    for i, user_id in enumerate(user_ids):
        user_submissions = [submission for submission in jsonified_submissions if user_id in submission]
        parsed_indicators = []
        for user_submission in user_submissions:
            # Get parsed indicators
            parsed_indicators += list(json.load(open(user_submission)).keys())

        # Find missing indicators
        missing_indicators = [indicator for indicator in required_indicators if indicator not in parsed_indicators]

        # Find common indicators
        common_indicators = [indicator for indicator in required_indicators if indicator in parsed_indicators]

        # Find additional indicators
        additional_indicators = [indicator for indicator in parsed_indicators if indicator not in required_indicators]


        # Create data frame
        dat = {"user_id": user_id,
                "found_indicators": ", ".join(common_indicators),
                "missing_indicators": ",".join(missing_indicators),
                "additional_indicators": ",".join(additional_indicators),
                "all_indicators_found": len(missing_indicators) == 0,
                "contains_additional_indicators": len(additional_indicators) > 0}

        if i == 0:
                df = pd.DataFrame(dat, index=[0])
        else:
                df = pd.concat([df, pd.DataFrame(dat, index=[0])])

    return df

def load_latest_jsonified_student_submission(assignment_id: int, user_id: int, submission_path: str = "submissions") -> Tuple[dict, int]:
    """Loadas the latest jsonified student submission which may be distributed over multiple files
    
    Args:
        assignment_id (int): The assignment id
        user_id (int): The user id
        submission_path (str): The path to the submission files
        
    Returns:
        dict: The submission as a dictionary"""

    # Create a list of all json files for this user and assignment
    json_files = create_file_list(submission_path, [f"ass-{assignment_id}", f"user-{user_id}", ".json"])

    # Prefer files with manual fixes
    json_files = deduplicate_files_with_manual_fixes(json_files)

    # Get the highest attempt
    json_files = deduplicate_highest_attempt(json_files)

    # Create and return submission dict
    submission_dict = {}
    attempt = 0
    for f in json_files:
        submission_dict.update(json.load(open(f)))
        attempt = int(re.compile(r"try-(\d+)").search(f).group(1))

    return submission_dict, attempt

def extract_html_content(text: str, tag: str):
    # Pattern allows for optional closing tag and captures content inside
    pattern = fr"<{tag}>(.*?)</{tag}>|<{tag}>(.*?)(?=<|$)"
    matches = re.findall(pattern, text, re.DOTALL)
    
    # Flatten the matches to handle the two different capturing groups
    return "\n".join([m[0] or m[1] for m in matches])


def get_weighted_points(points: dict, weights: dict) -> dict:
    return {key: np.float32(points[key]) * np.float32(weights[key]) for key in points.keys()}

def get_sum_points_for_pattern(points: dict, pattern: str) -> float:
    return np.sum([np.float32(points[key]) for key in points.keys() if re.match(pattern, key)])