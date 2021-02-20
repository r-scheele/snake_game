from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle(shape='square')
        turtle.color("white")
        turtle.shapesize(0.5, 1.0, 0.5)
        turtle.penup()
        turtle.goto(position)
        self.snake_parts.append(turtle)

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

    def move(self):
        for part in range(len(self.snake_parts) - 1, 0, -1):
            x = self.snake_parts[part - 1].xcor()
            y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        heading = self.head.heading()
        if heading == 0:
            self.head.left(90)
        elif heading == 180:
            self.head.right(90)

    def left(self):
        heading = self.head.heading()
        if heading == 90:
            self.head.left(90)
        elif heading == 270:
            self.head.right(90)

    def down(self):
        heading = self.head.heading()
        if heading == 90:
            self.head.right(90)
        elif heading == 180:
            self.head.left(90)
        elif heading == 0:
            self.head.right(90)

    def right(self):
        heading = self.head.heading()
        if heading == 90:
            self.head.right(90)
        elif heading == 270:
            self.head.left(90)
