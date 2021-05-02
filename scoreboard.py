from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-350, 280)
        self.write(f'Score:{self.score}', align="center", font=("Courier", 10, "normal"))
        self.goto(350, 280)
        self.write(f'Lives:{self.lives}', align="center", font=("Courier", 10, "normal"))

    def points(self):
        self.score += 1
        self.update_scoreboard()

    def miss(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -100)
        self.write('GAME OVER', align="center", font=("Courier", 100, "bold"))

    def win(self):
        self.goto(0, -100)
        self.write('You Win', align="center", font=("Courier", 100, "bold"))
