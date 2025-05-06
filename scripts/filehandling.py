# Functions related to file handling and folders

# Package imports
import os
from typing import Iterable


# Functions
def make_student_folders(student_id: int, week: int, submissions_path: str = "submissions") -> None:
    """Create folder structure for a student for a given week."""
    assert week in range(1, 5)
    
    # Create the student folder
    os.makedirs(f"{submissions_path}/stu-{student_id}/week-{week}/json", exist_ok=True)