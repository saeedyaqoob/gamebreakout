from turtle import Screen

from paddle import Paddle
from ball import Ball
from brick import build_bricks
import time
from scoreboard import Scoreboard


screen = Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


paddle = Paddle((0, -275))
ball = Ball()
bricks = build_bricks()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect win
    if scoreboard.score == 27:
        scoreboard.win()
        game_is_on = False

    # Detect collision with bricks
    for i in range(len(bricks)):
        if ball.distance(bricks[i]) < 40:
            ball.bounce_back(ball.distance(bricks[i]))
            bricks[i].delete()
            scoreboard.points()

    # Detect collision with side walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 50:
        ball.bounce_back(ball.distance(paddle))

    # Detect paddle misses
    if ball.ycor() < -280:
        scoreboard.miss()
        if scoreboard.lives == 0:
            scoreboard.game_over()
            game_is_on = False
        else:
            ball.reset_position((paddle.xcor(), paddle.ycor()))


screen.exitonclick()
