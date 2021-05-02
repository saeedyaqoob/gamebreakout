from turtle import Turtle


def build_bricks():
    x_pos = -350
    y_pos = 250
    bricks = []
    for i in range(5):
        for j in range(9):
            if x_pos > 350:
                x_pos = -350
                y_pos -= 50
                break
            else:
                bricks.append(Brick((x_pos, y_pos)))
                x_pos += 100
    return bricks


class Brick(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.penup()
        self.goto(position)

    def delete(self):
        self.goto(1000, 1000)
