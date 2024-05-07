from turtle import Turtle,Screen
from paddle import Paddle
from turtle import *
import random
from ball import Ball
import time
from scoreboard import Scoreboard
score=Scoreboard()
# My screen Setup
screen=Screen()
screen.bgcolor("black")

screen.setup(700,700)
# screen.tracer(0)

l_paddle=Paddle((-320,0))
r_paddle=Paddle((320,0))
# def lup():
#         l_paddle.go_up(self)
# def ldown():
#         l_paddle.go_down()
# def r_up():
#         r_paddle.go_up()
# def r_down():
#         r_paddle.go_down()
screen.listen()
screen.onkeypress(l_paddle.go_up,"Up")
screen.onkeypress(l_paddle.go_down,"Down")
screen.onkeypress(r_paddle.go_up,'w')
screen.onkeypress(r_paddle.go_down,'s')

# Creating a ball
x_position=random.randint(0,600)
y_position=random.randint(0,600)

ball=Ball()
game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()>320 or ball.ycor()<-320:
        ball.bounce()
    
    if ball.distance(r_paddle)<30:
       ball.collison()
       score.update_score()
    if ball.xcor()>320 or ball.xcor()<-320:
       score.game_over()
       game_is_on=False
           
    if ball.distance(l_paddle)<30 :
        ball.collison()
        print(score.update_score())
        # game_is_on=False
    


screen.exitonclick()
screen.mainloop()