from turtle import Screen
from snake_body import Snake
from food import Food
from score import Scoreboard
import time
s=Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)
global sn,fd,sc
sn=Snake()
fd=Food()
sc=Scoreboard()
s.listen()
s.onkey(sn.up,"Up")
s.onkey(sn.down,"Down")
s.onkey(sn.left,"Left")
s.onkey(sn.right,"Right")
def reset_game():
    sn.reset()
    fd.refresh()
    sc.reset_score()
    game_start()
def game_start():
    game_is_on=True
    while game_is_on:
        s.update()
        time.sleep(0.1)
        sn.move()
        if sn.head.distance(fd)<15:
            fd.refresh()
            sn.extend_seg()
            sc.increase_score()
        if sn.head.xcor()>280 or sn.head.xcor()<-280 or sn.head.ycor()>280 or sn.head.ycor()<-280:
            game_is_on=False
            sc.game_over()
        for segment in sn.segments[1:]:
            if sn.head.distance(segment)<10:
                game_is_on=False
                sc.game_over()

s.onkey(reset_game,"r")
game_start()
s.exitonclick()
    