
from scripts.utils import create_file_list

def update_canvas_grade(user_id, r_quiz_question_id, adv_quiz_question_id, quiz_submissions, points_r, points_adv, used_adv, grade, canvas_submission):
    # Get the quiz_submission for this student
    for quiz_submission in quiz_submissions:
        if quiz_submission.user_id == int(user_id):
            break
    
    # Generate data for updating the score and comments
    if r_quiz_question_id == adv_quiz_question_id:
        data = [{"attempt": canvas_submission.attempt,
                    "questions": {str(r_quiz_question_id): {"score": grade, "comment": used_adv}}}]
    else:
        data = [{"attempt": canvas_submission.attempt,
                    "questions": {
                        str(r_quiz_question_id): {"score": points_r},
                        str(adv_quiz_question_id): {"score": points_adv, "comment": used_adv}}}]
    
    print(data)

    # Update the question scores and comments
    quiz_submission.update_score_and_comments(quiz_submissions=data)

def post_canvas_comments(canvas_submission, comments = [], files = []):
    for comment in comments:
        canvas_submission.edit(comment = {"text_comment": comment})
    for file in files:
        canvas_submission.upload_comment(file=file)
