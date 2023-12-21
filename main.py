import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score

snake = Snake()
screen = Screen()
food = Food()
score = Score()
screen.bgcolor('black')
screen.title('My Snake Game')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left_side, 'Left')
screen.onkey(snake.right_side, 'Right')

is_game_on = True

while is_game_on:
    screen.update()

    snake.move()
    time.sleep(1)
    if snake.head.distance(food) < 15:
        print('collusion occurred')
        food.refresh_food_location()
        snake.extend()
        score.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print('Game over')
        is_game_on = False
        score.game_over()

    for segment in snake.total_snake[1:]:

        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
