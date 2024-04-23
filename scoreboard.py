from turtle import Turtle
ALIGN = "center"
FONT_FAMILY = "Times New Roman"
FONT_SIZE = 24
FONT_WEIGHT = "normal"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.write(f"Score : {self.score}",False,align=ALIGN,font=(FONT_FAMILY,FONT_SIZE,FONT_WEIGHT))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER.",False,align=ALIGN,font=(FONT_FAMILY,FONT_SIZE,FONT_WEIGHT))