from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

keep = True

screen.listen()
screen.onkey(snake.go_left, "a")
screen.onkey(snake.go_right, "d")
screen.onkey(snake.go_up, "w")
screen.onkey(snake.go_down, "s")

while keep:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    # Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    # Detect collision with the walls
    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        score.reset()
        snake.reset()

    # Detect the collision with body
    for segment in snake.segments[1:]:  # This part of code segments[1:] e de la list and slices ->
        if snake.head.distance(segment) < 10:          # si incepe sa verifice de na indexul unu sarind peste index 0 ->
            snake.reset()                                # poti sa adaugi si punct final si peste scat sa sara [2:3:1]
            score.reset()


screen.exitonclick()
