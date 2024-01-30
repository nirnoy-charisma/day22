from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

end_writing=Turtle
screen = Screen()
screen.screensize(600, 800)
screen.bgcolor("cyan")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


def clear_objects():
    for obj in [r_paddle, l_paddle, ball, score]:
        obj.clear()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_on = True
while is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # making the ball bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detecting the ball and paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
    #missing the ball
    if ball.xcor() >380 :
        ball.new_position()
        score.point_l()

    if ball.xcor() <-380:
        ball.new_position()
        score.point_r()

    if score.l_score >= 10 or score.r_score >= 10:
        is_on = False
        winner_turtle = Turtle()
        winner_turtle.color("white")
        winner_turtle.penup()
        winner_turtle.hideturtle()
        winner_turtle.goto(0, 0)
        winner_turtle.write(
            "Left Side Wins" if score.l_score > score.r_score else "Right Side Wins",
            align="center",
            font=("Arial", 70, "normal"),
        )
        time.sleep(2)
        clear_objects()
screen.exitonclick()
