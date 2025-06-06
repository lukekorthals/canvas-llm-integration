# canvas-llm-integration
Integrating the Canvas LMS with the OpenAI API for automated grading and feedback. 

I piloted this pipeline in a programming course in January 2025. The associated paper "AI grading and feedback - Insights from a programming course" was accepted to the [late breaking results track at AIED 2025](https://aied2025.itd.cnr.it/index.php/program/accepted-papers/late-breaking-results/).

> [!CAUTION]
> I am currently in the process of refactoring everything because there were some quick and dirty fixes we had to make when we applied this during a course in January. 
> The `prepare.ipynb` and `pipeline.ipynb` will gradually stop working properly and the `refactor.ipynb` file will gradually take over all functionality. 

> [!CAUTION]
> Defined functions in scripts/... are currently in varying states of disarray. After the initial refactoring (putting the pipeline into `refactor.ipynb`) they will be completely overhauled as well. 


Pipeline of AI support systems for grading and feedback in programming and math courses as piloted in the PIPS 2025 course.
