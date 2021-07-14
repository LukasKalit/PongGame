from turtle import Turtle
from score import Score_Board


RANGE_BUMP = 50
# random.randrange(0, 360, 45)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = Turtle("circle")
        self.ball.penup()
        self.ball.color("White")
        self.ball.shapesize(1)
        self.ball.setposition(0, 0)
        self.ball.setheading(45)
        self.score = Score_Board()
        self.speed_game = 0.007

    def hit(self, rpadle, lpadle):
        if self.ball.distance(rpadle) < RANGE_BUMP and self.ball.xcor() < -330 \
                or self.ball.distance(lpadle) < RANGE_BUMP and self.ball.xcor() > 330:
            bump = self.ball.heading() * -1 + 180
            self.ball.setheading(bump)
            if self.speed_game > 0.001:
                self.speed_game *= 0.9

    def move_ball(self):
        self.ball.fd(2)

    def hit_wall(self):
        if self.ball.ycor() < -280 or self.ball.ycor() > 280:
            bump = self.ball.heading() * -1
            self.ball.setheading(bump)

    def miss_left(self):
        if self.ball.xcor() > 350:
            self.score.r_point()
            self.ball.setposition(x=0, y=0)
            bump = self.ball.heading() * -1 + 180
            self.ball.setheading(bump)
            self.speed_game = 0.007

    def miss_right(self,):
        if self.ball.xcor() < -350:
            self.score.l_point()
            self.ball.setposition(x=0, y=0)
            bump = self.ball.heading() * -1 + 180
            self.ball.setheading(bump)
            self.speed_game = 0.007




