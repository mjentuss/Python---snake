import turtle
import random
import math

class Apple(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("orange")
        self.shapesize(1,1,1)
        self.setposition(random.randint(-290, 290), random.randint(-290, 290))
    
    def get_apple_pos(self):
        return "x:{} y:{}".format(self.xcor(), self.ycor())
    
    def get_distance_between_player_goal(self):
        return self.distance

    def is_collision(self, _player, _apple):
        x = (_player.xcor() - _apple.xcor())  # wspolrzedna x od obiektu player i apple
        y = (_player.ycor() - _apple.ycor())  # wspolrzedna y od obiektu player i apple
        self.distance = math.sqrt(x**2 + y**2)  # wzor na odleglosc srodka okregu od punktu
        if self.distance < 20:
            return True
    
    def jump(self):
        self.goto(random.randint(-290, 290), random.randint(-290, 290))