

# TODO: asking the questions
# TODO: checking if answer was right
# TODO: checking if we're at the end of quiz


class QuizBrain:
    def __init__(self, q_list):
        # The attributes are like object-specific variables that you want to keep track of. You can use these in methods.
        self.question_number = 0   # Start at zero, because all quizzes will start at question 0. This attribute will
        # track which question a user is currently on; will be used to go through question_list.
        self.question_list = q_list   # List of questions, which will be passed over to QuizBrain object when
        # initialized.
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # if self.question_number < len(self.question_list):
        #    return True
        # else:
        #    print("That's it, no more questions.")
        #    return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Write current_question.text to get the value of the text attribute, for the Question object held in the
        # variable, current_question. The object is selected by the self.question_number attribute.
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Invoke a different method, passing outputs of this method.
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # Drop to lowercase to account for input diff.
        if user_answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}")
