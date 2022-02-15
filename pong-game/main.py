from turtle import Screen, Turtle
from bar import Bar
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

r_bar = Bar((350, 0))
l_bar = Bar((-350, 0))

screen.listen()
screen.onkey(r_bar.go_up, "Up")
screen.onkey(r_bar.go_down, "Down")
screen.onkey(l_bar.go_up, "w")
screen.onkey(l_bar.go_down, "s")

game_active = True

while game_active:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    if ball.distance(r_bar) < 50 and ball.xcor() > 320 or ball.distance(l_bar) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
