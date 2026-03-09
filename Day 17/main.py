from question_model import Sawal
from data import question_data
from quiz_brain import QuizBrain

Question_bank = []

for Question in question_data:
    text = Question["text"]
    answer = Question["answer"]
    Quest = Sawal(text,answer) 
    Question_bank.append(Quest)
quiz = QuizBrain(Question_bank)
while quiz.is_question_remaining():
    quiz.next_question()
print("Congratulations you have completed Quiz")
print(f"Your Final Score is {quiz.score} /  {len(Question_bank)}")
