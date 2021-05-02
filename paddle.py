from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_len=6, stretch_wid=1)
        self.penup()
        self.goto(position)
        self.xcor()
        self.ycor()

    def go_right(self):
        if self.xcor() + 80 < 400:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() - 80 > - 400:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())
