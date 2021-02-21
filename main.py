from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=600, height=600)
score = Scoreboard()
screen.bgcolor("black")
screen.title('Snake Game')
screen.tracer(0)
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.head.distance(food) < 14:
        food.refresh()
        snake.extend()
        score.refresh()

    if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -285 or snake.head.ycor() > 285:
        game_is_on = False
        score.game_over()

    for segment in snake.snake_parts[1:]:
        if snake.head.distance(segment) < 8:
            game_is_on = False
            score.game_over()

screen.exitonclick()
