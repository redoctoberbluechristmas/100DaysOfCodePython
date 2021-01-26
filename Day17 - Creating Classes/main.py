from quiz_brain import QuizBrain
from question_model import Question
from data import question_data


question_bank = []
# for text, answer in question_data:
#     question_bank += Question(question_data[text], question_data[answer])

# How to Add Objects to List, based on dictionary input.

# Data will often be in listed dictionary format; we're converting it to something we can more readily use.
# Converting string keys into objects.

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # Create the object to add to list.
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Referencing the attribute, text, for the object at index 0 of our list, question_bank.
# print(question_bank[0].text)

quiz_brain = QuizBrain(question_bank)

quiz_brain.next_question()
