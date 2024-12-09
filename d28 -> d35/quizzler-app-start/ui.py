import tkinter as tk
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:
    def check(self, statut):
        if statut:
            self.score_total += 1
            self.score.config(
                text=f"Score: {self.score_total}", fg="black", bg=THEME_COLOR)

            self.backgd_canvas.configure(bg="green")
        else:
            self.backgd_canvas.configure(bg="red")
        self.screen.after(1000, func=self.get_next_question)

    def wrong_answef(self):
        result = self.quizz.check_answer("False")
        self.check(result)

    def true_answef(self):
        result = self.quizz.check_answer("True")
        self.check(result)

    def __init__(self, quiz_brain: QuizBrain):
        self.score_total = 0
        self.quizz = quiz_brain
        self.screen = tk.Tk()
        self.screen.title("Quizzler")
        self.screen.config(padx=20, pady=20, bg=THEME_COLOR)

        # Creation de la fenetre Canvas + Question Text
        self.backgd_canvas = tk.Canvas(height=250, width=300, bg="white")
        self.question = self.backgd_canvas.create_text(
            150, 125, font=("Arial", 20, "italic"), text="", fill=THEME_COLOR, width=240)
        self.backgd_canvas.grid(column=0, row=1, columnspan=2)
        # Creation score
        self.score = tk.Label(text="Score: 0", fg="black", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.wrong = tk.PhotoImage(file="images/false.png")
        self.agree = tk.PhotoImage(file="images/true.png")

        self.wrong_btn = tk.Button(image=self.wrong, command=self.wrong_answef)
        self.agree_btn = tk.Button(image=self.agree, command=self.true_answef)
        self.wrong_btn.grid(column=0, row=2, pady=(30, 0))
        self.agree_btn.grid(column=1, row=2, pady=(30, 0))

        self.get_next_question()
        self.screen.mainloop()

    def get_next_question(self):
        self.backgd_canvas.configure(bg="white")
        if self.quizz.still_has_questions():
            nxt_question = self.quizz.next_question()
            self.backgd_canvas.itemconfig(self.question, text=nxt_question)
        else:
            self.wrong_btn["state"] = "disabled"
            self.agree_btn["state"] = "disabled"
