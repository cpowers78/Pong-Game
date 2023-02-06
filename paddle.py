from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        new_ycor = self.ycor() + 30
        self.goto(self.xcor(), new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 30
        self.goto(self.xcor(), new_ycor)

