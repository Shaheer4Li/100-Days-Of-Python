from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.random()
    def random(self):
        xpos = random.randint(-270,270)
        ypos = random.randint(-270,270)
        self.goto(xpos,ypos)