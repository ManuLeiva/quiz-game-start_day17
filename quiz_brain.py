
# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz
# 2 attributes: question_number = 0
# question_list: we will use the question_number to keep track of the question number the user is on.
# method next_question() will pick up the question the user is on.

class QuizBrain:
    def __init__(self, q_list):
        # Attributes creation
        # question_number = 0
        # method next_question
        self.question_number = 0
        # initialize when create new quizbrain and we will passover the question bank,
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        number = int(len(self.question_list))
        if self.question_number == number:
            return True
        else:
            return False

    def next_question(self):
        # Retrieve the item at the current question_number from the question_list.
        # Use the input() function to show the user Question text and ask for the user's answer
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # we save the response on user_answer
        user_answer = input(f"Q.{self.question_number}  {current_question.text}. (True/False)")
        # we created the method check_answer and we will pass the values user_answer to have what the user has answered
        # and the current_question.answer, we take from the dictionary the answer key to have both and compare in the
        # method if it is correct or not.
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")








