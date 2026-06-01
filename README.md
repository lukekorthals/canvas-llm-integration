# canvas-llm-integration
Integrating the Canvas LMS with the OpenAI API for automated grading and feedback. 

I piloted this pipeline in a programming course in January 2025. The associated paper "Grading University Students with LLMs: Performance and Acceptance of a Canvas-Based Automation" was accepted to the [late breaking results track at AIED 2025](https://link.springer.com/chapter/10.1007/978-3-031-99264-3_5). A 20 minute talk I gave at the VU Amsterdam is available on [YouTube](https://www.youtube.com/watch?v=UA-vX2UqO2Q&pp=ygUNbHVrZSBrb3J0aGFscw%3D%3D).

# cite as 
Korthals, L., Rosenbusch, H., Grasman, R., Visser, I. (2025). Grading University Students with LLMs: Performance and Acceptance of a Canvas-Based Automation. In: Cristea, A.I., Walker, E., Lu, Y., Santos, O.C., Isotani, S. (eds) Artificial Intelligence in Education. Posters and Late Breaking Results, Workshops and Tutorials, Industry and Innovation Tracks, Practitioners, Doctoral Consortium, Blue Sky, and WideAIED. AIED 2025. Communications in Computer and Information Science, vol 2591 . Springer, Cham. https://doi.org/10.1007/978-3-031-99264-3_5

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

  > [!CAUTION]
  > Note that assignments in our course had one question pertaining to R and one question pertaining to advanced R / Python. 
  > The `r_quiz_question_id` and `adv_quiz_question_id` are used to identify these subquestions and update the points scored by the student accordingly. 
  > You probably have a different setup and want to change the grading logic inside the `refactor.ipynb` notebook.

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


