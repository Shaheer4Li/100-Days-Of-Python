from turtle import Turtle,Screen
import random
screen = Screen()

screen.setup(width= 505,height=404)
screen.bgpic("bg.png")
race_status = False
user_bet = screen.textinput(title= "Select your turtle",prompt="enter Color of your turtle")
xpos = -230
ypos = -140
colors =["white","blue","yellow","orange","purple","red"]
turtles =[]
for color in colors:
    tim = Turtle("turtle")
    tim.color(color)
    tim.penup()
    tim.goto(xpos,ypos)
    
    ypos+= 60
    turtles.append(tim)
if user_bet:
    race_status = True
while race_status:
    for turtl in turtles:
        if turtl.xcor() > 230:
            race_status = False
            winning = turtl.pencolor()
            if winning == user_bet:
                print(f"Congrats your {winning} turte has won")
            else:
                print(f"you lost wining turtle is {winning} color")
        distance = random.randint(1,10)
        turtl.fd(distance)
        

screen.exitonclick()


