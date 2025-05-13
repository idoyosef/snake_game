from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

# Handle snake movement
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Handle snake exiting boundaries
def check_boundaries():
    x_cor, y_cor = snake.head.position()

    if x_cor > 300:
        snake.head.goto(-300, y_cor)
    elif x_cor < -300:
        snake.head.goto(300, y_cor)

    if y_cor > 300:
        snake.head.goto(x_cor, -300)
    elif y_cor < -300:
        snake.head.goto(x_cor, 300)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.06)
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    check_boundaries()

    # Detect snake eating its own tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        else:
            if snake.head.distance(segment) < 15:
                scoreboard.game_over()
                game_is_on = False





screen.exitonclick()