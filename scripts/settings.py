# Sets all global variables based on the settings file

# Package imports
import yaml

# Local imports 
from scripts.utils import read_files_to_dict


# Load settings
with open("settings.yaml") as f:
    settings = yaml.safe_load(f)

# Grading
global MAX_GRADE
MAX_GRADE = settings["global"]["grading"]["max_grade"]

# Week
global ASSIGNMENTS
ASSIGNMENTS = settings["assignments"]

# Canvas settings
global COURSE_ID
COURSE_ID = settings["global"]["canvas"]["course_id"]


# LLM Settings
global MODEL
global GRADING_TEMPERATURE
global FEEDBACK_TEMPERATURE
global N_CHOICES_GRADING
global N_CHOICES_FEEDBACK
global PROMPTS
global USE_UVA
MODEL = settings["global"]["llm"]["model"]
GRADING_TEMPERATURE = settings["global"]["llm"]["grading_temperature"]
FEEDBACK_TEMPERATURE = settings["global"]["llm"]["feedback_temperature"]
N_CHOICES_GRADING = settings["global"]["llm"]["n_choices_grading"]
N_CHOICES_FEEDBACK = settings["global"]["llm"]["n_choices_feedback"]
PROMPTS = {k: read_files_to_dict(settings["global"]["llm"]["prompts"][k]) for k in settings["global"]["llm"]["prompts"].keys()}
USE_UVA_OPENAI = settings["global"]["llm"]["use_uva_openai"]

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