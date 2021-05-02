from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("green")
        self.goto(0, -260)
        self.x_move = 5
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_back(self, distance):
        self.y_move *= -1
        new_y = self.ycor() + int(distance/10)
        self.goto(self.xcor(), new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self, position):
        self.goto(position)
        self.bounce_x()
