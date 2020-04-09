import turtle

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("square")
        self.speed = 0
        self.direction = "stop"
        self.body = []

    def get_player_pos(self):
        return "x:{} y:{}".format(self.xcor(), self.ycor())

    def move(self):
        #self.forward(self.speed)
        if self.direction == "down":
            self.sety(self.ycor() - 20)
        if self.direction == "up":
            self.sety(self.ycor() + 20)
        if self.direction == "left":
            self.setx(self.xcor() - 20)
        if self.direction == "right":
            self.setx(self.xcor() + 20)

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"

    def turn_left(self):
        #self.left(90)
        if self.direction != "right":
            self.direction = "left"
    
    def turn_right(self):
        #self.right(90)
        if self.direction != "left":
            self.direction = "right"
    
    def border_checking(self):
        if self.xcor() > 350:
            self.setposition(-350, self.ycor())
        if self.xcor() < -350:
            self.setposition(350, self.ycor())
        if self.ycor() > 350:
            self.setposition(self.xcor(), -350)
        if self.ycor() < -350:
            self.setposition(self.xcor(), 350)
