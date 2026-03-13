from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game ")
screen.setup(width=600,height=600)
screen.tracer(0)
our_snake = Snake()
screen.listen()
khana = Food()
screen.onkey(key="w",fun=our_snake.up)
screen.onkey(key="s",fun=our_snake.down)
screen.onkey(key="d",fun=our_snake.move_d)
screen.onkey(key="a",fun=our_snake.Move_A)
our_score = Score()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    our_snake.move()
    if khana.distance(our_snake.head) < 15:
        khana.random()
        our_score.increment()
        our_snake.extends()
    if our_snake.head.xcor() > 290 or our_snake.head.xcor() < -290 or our_snake.head.ycor() > 290 or our_snake.head.ycor() < -290:
        game_is_on = False
        our_score.game_over()
    for body in our_snake.Snake_body:
        if body == our_snake.head:
            pass
        elif body.distance(our_snake.head)<10:
         game_is_on = False
         our_score.game_over()
        

        
        
        









screen.exitonclick()