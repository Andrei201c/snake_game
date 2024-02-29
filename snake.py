from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.draw_snake()
        self.head = self.segments[0]

    def draw_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed('fast')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            cor_x = self.segments[seg_num - 1].xcor()
            cor_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(cor_x, cor_y)
        self.head.forward(20)

    def reset(self):
        for seg in self.segments:
            seg.goto(1001,1001)
        self.segments = []
        self.draw_snake()
        self.head = self.segments[0]

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
