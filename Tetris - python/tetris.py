import turtle
import random
import time

window = turtle.Screen()
window.title("T E T R I S")
window.bgcolor("black")
window.setup(width=600, height=800)
window.tracer(0)
window.bgcolor("grey")
window.listen()
window.onkey(lambda: shape.move_right(grid), "d")
window.onkey(lambda: shape.move_left(grid), "a")

grid = []
grid_elements = [0] * 12
for i in range(24):
    grid.append(grid_elements.copy())

#Class representing score
class Score(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.score_count = 0
        self.color('red')
        self.up()
        self.hideturtle()
        self.goto(0, 250)
        self.write('score: 0', align='center', font=('Arial', 22, 'normal'))

#Class representing shapes
class Shape():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1,6)

        #Shapes
        self.square = [[1,1],[1,1]]
        self.L_shape = [[1,0],[1,0],[1,1]]
        self.t = [[1,1,1],[0,1,0]]
        self.hor = [[1,1,1]]
        self.ver = [[1],[1],[1]]

        self.shapes = [self.square, self.L_shape, self.t, self.hor, self.ver]
        self.shape_choice = random.choice(self.shapes)
        self.height = len(self.shape_choice)
        self.width = len(self.shape_choice[0])

    def move_right(self, grid):
        if self.x < 11 - self.width + 1:
            if grid[self.y][self.x + self.width] == 0: 
                self.erase_shape(grid) 
                self.x += 1

    def move_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.erase_shape(grid)
                self.x -= 1

    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape_choice[y][x] == 1:
                    grid[self.y + y][self.x + x] = self.color

    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape_choice[y][x] == 1:
                    grid[self.y + y][self.x + x] = 0

    def can_move(self, grid):
        for x in range(self.width):
            if self.shape_choice[self.height-1][x] == 1:
                if grid[self.y + self.height][self.x + x] != 0:
                    return False
        return True


class Pen(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.up()
        self.speed(0)
        self.shapesize(0.9, 0.9)

#Draw grid on the screen
def draw_grid(pen, grid):
    pen.clear()
    top = 230
    left = -110
    colors = ["black", "red", "yellow", "lightblue", "blue", "green", "orange"]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 20)
            screen_y = top - (y * 20)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()

#Check grid for full row
def check_grid(grid):
    for y in range(0,24):
        result = True
        for x in range(0, 12):
            if grid[y][x] == 0:
                result = False
        if result:
            for y in range(22, -1, -1):
                for x in range(0, 12):
                    grid[y+1][x] = grid[y][x]
            score.score_count += 1
            score.clear()
            score.write("Score: {}".format(score.score_count), align='center', font=('Courier', 24, 'normal'))
            print('score')


pen = Pen()
shape = Shape()
score = Score()

while True:
    window.update()

    if shape.y == 23 - shape.height + 1:
        check_grid(grid)
        shape = Shape()

    elif shape.can_move(grid):
        shape.erase_shape(grid)
        shape.y += 1
        shape.draw_shape(grid)
    else:
        check_grid(grid)
        shape = Shape()

    draw_grid(pen ,grid)
    time.sleep(0.03)