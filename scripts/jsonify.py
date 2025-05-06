# Functions to jsonify resources and student submissions

# Package imports
import json
import os
import re
import warnings
import zipfile

# Local imports
from .utils import create_file_list


# Functions
def jsonify(input_files: str | list, output_filename: str) -> list:
    """Parse a file into json according to the question indicators."""
        
    # Read files
    if isinstance(input_files, str):
        input_files = [input_files]
    text = ""
    for file in input_files:
        with open(file, "r") as f:
            text += f.read() + "\n\n\n"
        
    # Detect question indicators
    indicators = re.compile(r"(#R\d+|#Radv\d+|#Python\d+):?\s*\n").findall(text)

    # Initialize the result dictionary
    result = {}
    
    # Parse the text
    for i, indicator in enumerate(indicators):
        start_idx = text.find(indicator) + len(indicator)
        end_idx = text.find(indicators[i+1]) if i < len(indicators)-1 else len(text)
        result[indicator] = text[start_idx:end_idx].strip().split('\n')
        text = text[end_idx:]
    
    # Create folder if it does not exist
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    
    # Save the dictionary as a JSON file
    with open(output_filename, 'w') as json_file:
        json.dump(result, json_file, indent=4)
    
    # Return for debugging
    return indicators


def jsonify_resources(assignment_idx: int, resources_path: str = "resources") -> dict:
    """Jsonify all resources for a given assignment."""
    assert assignment_idx in range(1, 5)

    # Ignore json and yaml files
    indicators_neg = [".json", ".yaml", ".html", "OLD"]
    
    # Create file lists
    file_lists = {
        "questions": create_file_list(f"{resources_path}/assignment-{assignment_idx}", 
                                    indicators_pos=["questions"], 
                                    indicators_neg=indicators_neg),
        "rubrics": create_file_list(f"{resources_path}/assignment-{assignment_idx}", 
                                indicators_pos=["rubrics"], 
                                indicators_neg=indicators_neg),
        "solutions": create_file_list(f"{resources_path}/assignment-{assignment_idx}", 
                                    indicators_pos=["solutions"], 
                                    indicators_neg=indicators_neg),
        "goals": create_file_list(f"{resources_path}/assignment-{assignment_idx}", 
                                indicators_pos=["goals"], 
                                indicators_neg=indicators_neg),
        "weights": create_file_list(f"{resources_path}/assignment-{assignment_idx}",
                                    indicators_pos=["weights"],
                                    indicators_neg=indicators_neg)
    }
    
    # jsonify each file list
    result = {key: jsonify(file_lists[key], f"{resources_path}/assignment-{assignment_idx}/json/assignment-{assignment_idx}_{key}.json") for key in file_lists}
    result = {key: sorted(result[key], key=lambda x: (x.split('#')[1].strip('0123456789'), int(''.join(filter(str.isdigit, x))))) for key in result}
    
    # Make sure all indicators are the same for each resource
    indicators = result["questions"]
    if not all([indicators == result[key] for key in result]):
        warnings.warn("WARNING!!! Indicators are not the same for all resources")
    return result
        
        
def count_matched_indicators(indicators: list, pattern: str = r"(R|Radv|Python)") -> int:
    """Count the number of indicators that match a pattern."""
    return len(re.compile(pattern).findall("\n".join(indicators)))


def analyze_jsonify_results(results: dict, level: int = 0) -> None:
    """Analyze the results of jsonifying for debugging."""
    prefix = "\t" * level
    for key in results:
        if isinstance(results[key], dict):
            print(f"{prefix}{key}:")
            analyze_jsonify_results(results[key], level + 1)
        else:
            total = count_matched_indicators(results[key])
            r = count_matched_indicators(results[key], r"(R)\d+")
            radv = count_matched_indicators(results[key], r"(Radv)\d+")
            python = count_matched_indicators(results[key], r"(Python)\d+")
            print(f"{prefix}{key}: {total} (R: {r}, Radv: {radv}, Python: {python})")
            