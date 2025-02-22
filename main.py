
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off automatic screen updates

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keyboard inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with walls
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or \
            snake.segments[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with itself
    for segment in snake.segments[1:]:  # Ignore the head
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()