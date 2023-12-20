import random
import turtle
from turtle import Turtle


screen=turtle.Screen()
prediction = screen.textinput(title='Predict', prompt="who will win this race? 'red', 'blue', 'green', 'grey', 'brown'or 'black' ")

colors=['red', 'blue', 'green', 'grey', 'brown','black']
timmy_position=[-40, -10, 20, 50, 80,110]
new_turtle=[]
is_race_on=False
for index in range(0, len(colors)):
    timmy = Turtle(shape='turtle')
    timmy.penup()
    timmy.goto(x=-270, y=timmy_position[index])
    timmy.color(colors[index])
    new_turtle.append(timmy)

if prediction:
    is_race_on=True
while is_race_on:

    for tim in new_turtle:
        movement = random.randint(0, 10)
        tim.forward(movement)
        if tim.xcor() >270:
            is_race_on=False
            winning_color=tim.pencolor()
            if winning_color == prediction.lower():
                print(f'you won!, the winning turtle is "{winning_color}" turtle')
            else:
                print(f'you lost!, the winning turtle is "{winning_color}" turtle')


screen.setup(height=500, width=600)
screen.exitonclick()


