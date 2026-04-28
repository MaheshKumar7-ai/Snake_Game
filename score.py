from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt",'r') as f:
            str_high_score=f.read()
            int_high_score=int(str_high_score)
        self.score=0
        self.high_score=int_high_score
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"HighScore={self.high_score}  Score={self.score}",align="center",font=("Courier",24,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
    def game_over(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("highscore.txt",'w') as f:
                f.write(str(self.high_score))
        self.goto(0,0)
        self.write("    GAME OVER\n Press 'r' to restart",align="center",font=("Courier",24,"normal"))
    def reset_score(self):
        self.score=0
        self.clear()
        self.goto(0,270)
        self.update_score()