from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_obj = Question(question["question"], question["correct_answer"])
    question_bank.append(question_obj)

quiz_brain = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz_brain)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")
