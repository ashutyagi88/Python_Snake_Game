from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def add_segment(self,position):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_segments.append(snake)

    def reset_snake(self):
        for seg in self.snake_segments:
            seg.goto(1000,1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend_snake(self):
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for seg in range(len(self.snake_segments)-1,0,-1):
            new_x = self.snake_segments[seg-1].xcor()
            new_y = self.snake_segments[seg-1].ycor()
            self.snake_segments[seg].goto(new_x,new_y)

        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def up(self):
        if(self.head.heading() != DOWN):    
            self.head.setheading(UP)

    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)


