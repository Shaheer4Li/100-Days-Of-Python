from turtle import Turtle, Screen
import turtle
import random
import colorgram
screen = Screen()
timmy = Turtle()
timmy.speed(0)
turtle.colormode(255)
pallete =[]
colors = colorgram.extract("image.jpg",10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    pallete.append((r,g,b))
timmy.hideturtle()
timmy.penup()
timmy.seth(220)
timmy.forward(400)
timmy.seth(0)
timmy.pendown()
y = timmy.ycor()
x =timmy.xcor()
for i in range(10):
    timmy.setpos(x,y)
    y += 55
    for j in range(12):
        timmy.pendown()
        timmy.dot(20,random.choice(pallete))
        timmy.penup()
        timmy.forward(55)
        

