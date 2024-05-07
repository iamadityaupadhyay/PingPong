from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position) :
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.color("white")
        self.shapesize(stretch_wid=4,stretch_len=0.8)
        self.penup()
        self.goto(position)
        self.showturtle()
    # Moving Up
    def go_up(self):
        
        y=self.ycor()+20
        self.goto(self.xcor() ,y)
    # Moving Down  
    def go_down(self):
        y=self.ycor()-20
        self.goto(self.xcor() ,y)

