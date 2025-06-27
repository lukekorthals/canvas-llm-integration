# canvas-llm-integration
Integrating the Canvas LMS with the OpenAI API for automated grading and feedback. 

I piloted this pipeline in a programming course in January 2025. The associated paper "AI grading and feedback - Insights from a programming course" was accepted to the [late breaking results track at AIED 2025](https://aied2025.itd.cnr.it/index.php/program/accepted-papers/late-breaking-results/).

# Quick Start

1. Clone the repository

```bash
git clone https://github.com/lukekorthals/canvas-llm-integration
cd canvas-llm-integration
```

2. Copy the `[EXAMPLE]environment.yml` file and rename it to `environment.yml`.
Then, enter a name for the virtual environment and fill the required variables in the `environment.yml` file. 

```yaml
name: canvas-llm-integration

variables:
  CANVAS_API_URL: ENTER_YOUR_URL
  CANVAS_API_KEY: ENTER_YOUR_KEY
  CANVAS_USER_ID: ENTER_YOUR_ID
  OPENAI_API_KEY: ENTER_YOUR_KEY
  OPENAI_BASE_URL: ENTER_YOUR_URL
```

3. Create a virtual environment from the `environment.yaml` file:

```bash 
conda env create -f environment.yaml
```

4. Copy the `[EXAMPLE]settings.yaml` file and rename it to `settings.yaml`.
Enter all relevant information in the `settings.yaml` file.

5. Open the `refactor.ipynb`notebook and set the `ASSIGNMENT_NUMBER` to the number corresponding to the number in  the `settings.yaml` for the assignment you want to grade.

```yaml
assignments:
    1: # this is the assignment number in the settings.yml file
        ...
```
```python
ASSIGNMENT_NUMBER = 1  # Set this to the assignment number you want to grade
```

6. Run the notebook cell by cell.


