from turtle import Turtle,Screen
import time
from snake import Snake
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game ")
screen.tracer(0)
our_snake = Snake()
screen.listen()

screen.onkey(key="w",fun=our_snake.up)
screen.onkey(key="s",fun=our_snake.down)
screen.onkey(key="d",fun=our_snake.move_d)
screen.onkey(key="a",fun=our_snake.Move_A)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    our_snake.move()
    

        
        
        









screen.exitonclick()