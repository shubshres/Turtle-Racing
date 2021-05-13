import turtle
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win this race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
list_of_turtles = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    list_of_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:

    for turtle in list_of_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The {winner} turtle was the winner!")
            else:
                print(f"You lost! The {winner} turtle was the winner")

        random_distance = random.randint(0,5)
        turtle.forward(random_distance)

screen.exitonclick()