from turtle import Turtle

class Score(Turtle):
    number = 0
    def __init__(self):
        super().__init__()
        self.number = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(arg=f"Your Score is {self.number}",move=False,align='center',font= ( 'Roboto',15,'bold'))
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game over",move=False,align='center',font= ( 'Roboto',15,'bold'))
        
    def increment(self):
        self.number +=1
        self.clear()
        self.write(arg=f"Your Score is {self.number}",move=False,align='center',font= ( 'Roboto',15,'bold'))
