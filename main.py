from turtle import Screen
from paddle import Paddle
import time
from ball import Ball

# initialing screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
ball = Ball()


screen.listen()
screen.onkey(paddle.go_up_left, "w")
screen.onkey(paddle.go_down_left, "s")
screen.onkey(paddle.go_up_right, "Up")
screen.onkey(paddle.go_down_right, "Down")

# main loop
game_is_on = True
while game_is_on:

    ball.hit(paddle.lpadle, paddle.rpadle)
    ball.move_ball()
    ball.hit_wall()
    ball.miss_left()
    ball.miss_right()
    time.sleep(ball.speed_game)
    screen.update()

screen.exitonclick()
