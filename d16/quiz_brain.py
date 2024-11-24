from dataclasses import dataclass
from question_model import Question


@dataclass
class quizzBrain:
    questions: list[Question]
    score: int = 0
    number_question: int = 0

    def display_question(self):
        print("Score: ", self.score)
        print(f"Q:{self.number_question+1} {
              self.questions[self.number_question].question}")

    def next_question(self):
        self.number_question += 1

    def is_valid(self, user_answer):
        if self.questions[self.number_question].answer == user_answer:
            print("BRAVO")
            self.score += 1
        else:
            print("BIIIIP la réponse est :",
                  self.questions[self.number_question].answer)
        self.next_question()

    def is_end_of_questions(self):
        if self.number_question >= len(self.questions):
            print("FIN DE QUIZZ")
            self.number_question = 0
            self.score = 0

            return True
        return False
