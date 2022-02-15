from turtle import Turtle, Screen
import random

race_ongoing = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-250,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_ongoing = True

while race_ongoing:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 250:
            race_ongoing = False
            if user_bet == turtle.pencolor():
                print(f"And the winner is, {turtle.pencolor()}")
                print("Congratulations, congratulations. You win")
            else:
                print(f"And the winner is, {turtle.pencolor()}")
                print("Sorry. You lose")
            

screen.exitonclick()
