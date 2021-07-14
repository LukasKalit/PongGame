from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.rpadle = Turtle("square")
        self.rpadle.penup()
        self.rpadle.color("White")
        self.rpadle.turtlesize(stretch_wid=1, stretch_len=5)
        self.rpadle.setposition(350, 0)
        self.rpadle.setheading(270)

        self.lpadle = Turtle("square")
        self.lpadle.penup()
        self.lpadle.color("White")
        self.lpadle.turtlesize(stretch_wid=1, stretch_len=5)
        self.lpadle.setposition(-350, 0)
        self.lpadle.setheading(270)

    def go_up_left(self):
        self.lpadle.back(25)

    def go_down_left(self):
        self.lpadle.fd(25)

    def go_up_right(self):
        self.rpadle.back(25)

    def go_down_right(self):
        self.rpadle.fd(25)
