from turtle import Turtle
DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        x = 0
        for _ in range(3):
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.goto(x, y=0)
            x -= 20
            self.segments.append(t)

    def extend(self):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        pos = (self.segments[-1].xcor(), self.segments[-1].ycor())
        t.goto(pos)
        self.segments.append(t)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)

        self.segments.clear()
        self.create_snake()

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)

    def up(self):
        curr_head = self.segments[0].heading()
        if curr_head==0 or curr_head==180:
            self.segments[0].setheading(90)

    def down(self):
        curr_head = self.segments[0].heading()
        if curr_head==0 or curr_head==180:
            self.segments[0].setheading(270)

    def left(self):
        curr_head = self.segments[0].heading()
        if curr_head==90 or curr_head==270:
            self.segments[0].setheading(180)

    def right(self):
        curr_head = self.segments[0].heading()
        if curr_head==90 or curr_head==270:
            self.segments[0].setheading(0)
