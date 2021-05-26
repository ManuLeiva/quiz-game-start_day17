from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

# Iterating through question_data
for question in question_data:
    # We create 2 variables, one for the text key, 2nd one for the answer key.
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # We create the question-objects
    new_question = Question(question_text, question_answer)
    # We append it in the question_bank list.
    question_bank.append(new_question)


quizz = QuizBrain(question_bank)

while not quizz.still_has_questions():
    quizz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quizz.score}/{len(quizz.question_list)}")



