from data import question_data
from question_model import Question
from quiz_brain import quizzBrain

questions = [Question(i["text"], i["answer"]) for i in question_data]
quizz_brain = quizzBrain(questions)


while not quizz_brain.is_end_of_questions():
    quizz_brain.display_question()
    user_answer = input("Your answer : True or False")
    quizz_brain.is_valid(user_answer)
