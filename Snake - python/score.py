import turtle

class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-300, 360)
        self.score = 0
        self.write('Score: 0', align='center', font=('Courier', 16, 'normal'))

    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align="center", font=("Courier", 16, "normal"))

    def change_score(self):
        self.penup()
        self.score += 1
        self.update_score()