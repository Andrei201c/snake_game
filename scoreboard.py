from turtle import Turtle
ALIGN = "center"
FONT = ("Verdana", 15, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data: # sintaxa de citire in fisierul data.txt
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} HIGH SCORE {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data: # sintaxa de scriere in fisierul data.txt
                data.write(str(self.high_score))
            self.clear()
        self.score = 0
        self.update_score()

    # def game_over(self):
        # self.goto(0, 0)
        # self.clear()
        # self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase(self):
        self.score += 1
        self.update_score()

