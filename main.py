from turtle import Screen
from peddle import Peddle
from ball import Ball
from  score import ScoreBar
import time


screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Peddle((350, 0))
l_paddle = Peddle((-350, 0))
ball = Ball()
l_score = ScoreBar(-100, 200)
r_score = ScoreBar(100, 200)

screen.listen()
screen.onkey(r_paddle.pedal_up, "Up")
screen.onkey(r_paddle.pedal_down, "Down")
screen.onkey(l_paddle.pedal_up, "w")
screen.onkey(l_paddle.pedal_down, "s")

game_on = True
sleep = 0.1
while game_on:
    time.sleep(sleep)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with peddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep -= 0.005

    if ball.xcor() > 380:
        sleep = 0.1
        l_score.clear()
        l_score.l_score_up()
        ball.reset_position()
        time.sleep(0.5)
    if ball.xcor() < -380:
        sleep = 0.1
        r_score.r_score_up()
        ball.reset_position()
        time.sleep(0.5)




screen.exitonclick()
