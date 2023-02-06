from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


ball = Ball()
right_paddle = Paddle((370,0))
left_paddle = Paddle((-370,0))



screen.listen()
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(left_paddle.move_up, "w")

right_score = Score((100, 250))
left_score = Score((-100, 250))

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    #Detect collision with paddle
    if ball.distance(right_paddle) < 25 or ball.distance(left_paddle) < 25:
        ball.paddle_hit()
    #Detect collision with side wall
    if ball.xcor() > 380:
        left_score.increase_score()
        left_score.update_score()
        ball.setposition(0,0)
    if ball.xcor() < -380:
        right_score.increase_score()
        right_score.update_score()
        ball.setposition(0,0)

    if left_score.score == 5:
        left_score.game_over()
        game_is_on = False
    if right_score.score == 5:
        right_score.game_over()
        game_is_on = False








screen.exitonclick()
