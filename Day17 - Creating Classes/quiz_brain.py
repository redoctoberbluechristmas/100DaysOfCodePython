

# TODO: asking the questions
# TODO: checking if answer was right
# TODO: checking if we're at the end of quiz


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0   # Start at zero, because all quizzes will start at question 0. This attribute will
        # track which question a user is currently on; will be used to go through question_list.
        self.question_list = q_list   # List of questions, which will be passed over to QuizBrain object when
        # initialized.

    def next_question(self):
        current_question = self.question_list[self.question_number]
        # Write current_question.text to get the value of the text attribute, for the Question object held in the
        # variable, current_question
        user_response = input(f"Q.{self.question_number}: {current_question.text} (True/False)?")