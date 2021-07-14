from turtle import Turtle


class Score_Board(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("White")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.writing()

    def l_point(self):
        self.l_score += 1
        self.writing()

    def r_point(self):
        self.r_score += 1
        self.writing()

    def writing(self):
        self.clear()
        self.setposition(x=-200, y=270)
        self.write(arg=f"Score: {self.r_score}", move=False, align="center",
                               font=("Arial", 15, "normal"))
        self.setposition(x=200, y=270)
        self.write(arg=f"Score: {self.l_score}", move=False, align="center",
                         font=("Arial", 15, "normal"))


