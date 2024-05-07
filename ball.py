from turtle import Turtle
from scoreboard import Scoreboard

class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x=10
        self.y=10
    def move(self):
        x_cor=self.xcor()+self.x   
        y_cor=self.ycor()+self.y
        self.goto(x_cor,y_cor)   
    def bounce(self):
        self.y*=-1
    def collison(self):
        self.x*=-1
    