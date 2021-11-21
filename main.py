import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=600, height=550)
user_bet = screen.textinput(title="Chose your turtle", prompt="Which colour do you want?: ")
colour = ["red", "yellow", "orange", "green", "blue", "purple"]
y_position = [-100, -50, 0, 50, 100, 150]
all_turtle = []

for turtle_index in range(0, 6):
    tantan = Turtle(shape="turtle")
    tantan.color(colour[turtle_index])
    tantan.penup()
    tantan.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(tantan)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            win_colour = turtle.pencolor()
            if win_colour == user_bet:
                print(f"You've won! the {win_colour} turtle is winner.")
            else:
                print(f"You've lost! the {win_colour} turtle is winner.")

        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)

screen.exitonclick()

# def move_forward():
#     tantan.forward(15)
#
#
# def move_back():
#     tantan.back(15)
#
#
# def turn_left():
#     tantan.left(15)
#
#
# def turn_right():
#     tantan.right(15)
#
# def clear():
#     tantan.clear()
#     tantan.penup()
#     tantan.home()
#     tantan.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)
