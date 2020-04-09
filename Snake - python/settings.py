import turtle

class Border(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.shape("square")
        self.pensize(3)
        self.goto(-350, -350)
    
    def draw_border(self):
        self.pendown()
        for i in range(4):
            self.forward(700)
            self.left(90)
        self.penup()
