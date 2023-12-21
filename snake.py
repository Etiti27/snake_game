from turtle import Turtle

all_snake = []
STARTING_POSITION = [(0,0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.total_snake = all_snake
        self.create_snake()
        self.head = self.total_snake[0]

    def create_snake(self):

        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        square = Turtle()
        square.penup()
        square.color('white')
        square.shape('square')

        square.goto(position)
        all_snake.append(square)


    def extend(self):
       self.add_segment(self.total_snake[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left_side(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right_side(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for seg_num in range(len(self.total_snake) - 1, 0, -1):
            new_x = self.total_snake[seg_num - 1].xcor()
            new_y = self.total_snake[seg_num - 1].ycor()
            self.total_snake[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
