import html


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.actual_answer = None

    def next_question(self):
        question = self.question_list[self.question_number]
        self.actual_answer = bool(question.answer)
        self.question_number += 1
        question_text = html.unescape(question.text)
        return f"Q{self.question_number}. {question_text} (True/False): "

    def still_has_questions(self):
        return self.question_number <= len(self.question_list) - 1

    def check_answer(self, user_answer: bool) -> bool:
        if user_answer == self.actual_answer:
            print("You got it right")
            self.score += 1
            return True
        else:
            print("That's wrong")
            return False
