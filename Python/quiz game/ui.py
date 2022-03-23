import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(height=250, width=300, bg="white")
        self.text = self.canvas.create_text(150, 125, width=280, text="Some question text", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky='EW')

        self.true_image = tk.PhotoImage(file="images/true.png")
        self.true_btn = tk.Button(image=self.true_image, command=self.guess_true)
        self.true_btn.grid(row=2, column=0)

        self.false_image = tk.PhotoImage(file="images/false.png")
        self.false_btn = tk.Button(image=self.false_image, command=self.guess_false)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            next_question = self.quiz_brain.next_question()
            self.canvas.itemconfig(tagOrId=self.text, text=next_question)
        else:
            self.canvas.itemconfig(tagOrId=self.text, text="You've reached the end of the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def guess_true(self):
        self.give_feedback(self.quiz_brain.check_answer(True))

    def guess_false(self):
        self.give_feedback(self.quiz_brain.check_answer(False))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
