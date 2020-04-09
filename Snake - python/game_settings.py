from settings import *
from player import Player
from apple import Apple
from score import Score
import time, turtle

class Game():
    def __init__(self):
        super().__init__()
        self.window = turtle.Screen()
        self.window.title("snake")
        self.window.bgcolor("black")
        self.window.screensize(700, 700)
        self.window.tracer(2)
        self.window.listen()

    def new_game(self):
        # creating game objects
        self.border_setup = Border()
        self.player = Player()
        self.apple = Apple()
        self.score = Score()
        # setup functions
        self.border_setup.draw_border()

        self.run()

    def run(self):
        self.playing = True

        while self.playing:
            self.events()
            self.update()

    def events(self):
        self.window.onkeypress(self.player.turn_left, "Left")
        self.window.onkeypress(self.player.turn_right, "Right")
        self.window.onkeypress(self.player.go_up, "Up")
        self.window.onkeypress(self.player.go_down, "Down")

    def update(self):
        self.window.update()

        time.sleep(0.06)
        self.player.border_checking()

        if self.apple.is_collision(self.player, self.apple):
            self.apple.jump()

            self.score.change_score()
            self.score.update_score()

            self.new_segment = turtle.Turtle()
            self.new_segment.speed(0)
            self.new_segment.shape("square")
            self.new_segment.color("darkgreen")
            self.new_segment.penup()
            self.player.body.append(self.new_segment)

        for index in range(len(self.player.body) - 1, 0, -1):
            x = self.player.body[index - 1].xcor()
            y = self.player.body[index - 1].ycor()
            self.player.body[index].goto(x, y)

        if len(self.player.body) > 0:
            x = self.player.xcor()
            y = self.player.ycor()
            self.player.body[0].goto(x, y)

        self.player.move()
