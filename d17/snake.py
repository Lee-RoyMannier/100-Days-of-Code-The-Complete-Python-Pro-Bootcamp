from turtle import Turtle

COORD = [(0, 0), (-20, 0), (-40, 0)]


class Snake():
    def __init__(self):
        self.segments = []
        self.create_body()

    def create_body(self):
        for pos in COORD:
            self.create_segment(pos)

    def create_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_segment(self):
        self.create_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_body()

    def move(self):
        for t in range(len(self.segments)-1, 0, -1):
            xcor = self.segments[t-1].xcor()
            ycor = self.segments[t-1].ycor()
            self.segments[t].goto(xcor, ycor)

        self.segments[0].forward(20)

    def turn_left(self):
        if not self.segments[0].heading() == 0:
            self.segments[0].setheading(180)

    def turn_right(self):
        if not self.segments[0].heading() == 180:
            self.segments[0].setheading(0)

    def up(self):
        if not self.segments[0].heading() == 270:
            self.segments[0].setheading(90)

    def down(self):
        if not self.segments[0].heading() == 90:
            self.segments[0].setheading(270)
