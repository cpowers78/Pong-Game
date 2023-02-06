from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 35, 'normal')

class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.hideturtle()
        self.goto(position)
        self.penup()
        self.color("white")
        self.score = 0
        self.update_score()



    def update_score(self):
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)



    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER. ", align=ALIGNMENT, font=FONT)
