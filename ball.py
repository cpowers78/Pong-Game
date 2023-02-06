from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.color("purple")
        self.goto(0,0)
        self.y_move = 10
        self.x_move = 10

    def move(self):
       new_x = self.xcor() + self.x_move
       new_y = self.ycor() + self.y_move
       self.goto(new_x, new_y)

    def bounce(self):
        self.y_move = -(self.y_move)

    def paddle_hit(self):
        self.x_move = -(self.x_move)




