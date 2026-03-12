from turtle import Turtle
startx =0
move_distance =20
up =90
down=270
left = 180
right = 0
class Snake:
    def __init__(self):
        self.Snake_body =[]
        self.crete_snake()
        self.head = self.Snake_body[0]
    def crete_snake(self):
        start = startx
        for i in range(3):
            new_box = Turtle("square")
            new_box.color("white")
            new_box.penup()
            new_box.goto(start,0) 
            start +=20
            self.Snake_body.append(new_box)
    def move(self):
        for i in range(len(self.Snake_body)-1,0,-1):
            newx = self.Snake_body[i-1].xcor()
            newy = self.Snake_body[i-1].ycor()
            self.Snake_body[i].goto(newx,newy)
        self.Snake_body[0].fd(move_distance)
    def up(self):
        if self.head.heading() != down:
            self.head.seth(up)
    def down(self):
        if self.head.heading() != up:
            self.head.seth(down)
    def move_d(self):
        if self.head.heading() != left:
            self.head.seth(right)
    def Move_A(self):
        if self.head.heading() != right:
            self.head.seth(left)
            
