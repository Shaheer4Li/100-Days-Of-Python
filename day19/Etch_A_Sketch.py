from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
tim.width(3)
tim.shape("turtle")
screen.colormode(255)
screen.bgcolor(200,200,200)
tim.color((70, 90, 70))
screen.listen()
def move_forward():
    tim.forward(20)
def move_backward():
    tim.bk(20)
def turn_clockwise():
    tim.rt(10)
def turn_anticlockwise():
    tim.lt(10)
def reset():
    screen.resetscreen()
screen.onkeypress(key = "w", fun= move_forward)
screen.onkeypress(key = "s", fun= move_backward)
screen.onkeypress(key = "d", fun= turn_clockwise)
screen.onkeypress(key = "a", fun= turn_anticlockwise)
screen.onkeyrelease(key = "c", fun= reset)

screen.exitonclick()