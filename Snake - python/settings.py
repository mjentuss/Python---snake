import turtle

class Window(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.window = turtle.Screen()
        self.window.title("Snake - oop")
        self.window.bgcolor("grey")
        self.window.screensize(700, 700)
        self.window.tracer(2)
        self.window.listen()

    def events(self, _player):
        self.window.onkeypress(_player.turn_left, "Left")
        self.window.onkey(_player.turn_right, "Right")
        self.window.onkey(_player.go_up, "Up")
        self.window.onkeypress(_player.go_down, "Down")


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
