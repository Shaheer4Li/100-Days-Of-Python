
class QuizBrain:
    def __init__(self,list):
        self.list = list
        self.question_number =0
        self.score = 0
    def is_question_remaining(self):
        return self.question_number < len(self.list)
        
    def next_question(self):
        self.new_question = self.list[self.question_number]
        self.question_number +=1
        User_answer = input(f"Q. {self.question_number}  {self.new_question.text} (True/False)  ")
        self.answer_check(User_answer,self.new_question.answer)
    def answer_check(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Thats The right Answer")
            self.score +=1
        else:
            print("OOPs thats Wrong answer")
        print(f"Your Score is {self.score} / {self.question_number} ")
        print(f"correct answer is {correct_answer}")

        