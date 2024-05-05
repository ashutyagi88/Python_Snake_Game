from turtle import Turtle
ALIGN = "center"
FONT_FAMILY = "Times New Roman"
FONT_SIZE = 24
FONT_WEIGHT = "normal"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Projects/Snake_Game/data.txt") as data:
            self.highscore = int(data.read())
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscore}",False,align=ALIGN,font=(FONT_FAMILY,FONT_SIZE,FONT_WEIGHT))

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER.",False,align=ALIGN,font=(FONT_FAMILY,FONT_SIZE,FONT_WEIGHT))

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Projects/Snake_Game/data.txt","w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()