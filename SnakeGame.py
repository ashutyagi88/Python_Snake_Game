from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.right,key="Right")
screen.onkey(snake.up,key="Up")
screen.onkey(snake.left,key="Left")
screen.onkey(snake.down,key="Down")

game_is_on = True

while(game_is_on):
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Collision with food
    if(snake.head.distance(food)<15):
        food.change_location()
        snake.extend_snake()
        score.increase_score()
    
    #Detect Collision with wall
    if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_is_on = False
        score.game_over()

    #Detect Collision with tail
    for segment in snake.snake_segments[1:]:
        if(snake.head.distance(segment) < 10):
            game_is_on = False
            score.game_over()    

screen.exitonclick()