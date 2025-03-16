#My code(during pause and do it yourself time)
# from turtle import Turtle, Screen
#
# screen = Screen()
# screen.setup(width=500, height=400)
# user_input = screen.textinput(title='Make your bet', prompt='Which color would you like to choose: ')
# colors = ["red", "green", "yellow", "blue", "orange", "purple"]
#
# y = -100
# for item in colors:
#     tum = Turtle(shape="turtle")
#     tum.color(item)
#     tum.penup()
#     tum.goto(-230, y)
#     y += 40
#
# screen.exitonclick()

#Angela ma'am's code


from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_game_on = False
user_input = screen.textinput(title='Make your bet', prompt='Which color would you like to choose: ')
colors = ["red", "green", "yellow", "blue", "orange", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[index])
    turtles.append(new_turtle)

if user_input:
    is_game_on = True

while is_game_on:
    for turtle in turtles:
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                screen.title(f"You won the bet, {user_input} won the race")
            else:
                screen.title(f"You lost the bet, {winning_color} won the race")

screen.exitonclick() # to keep the window open until we click on it.
screen.mainloop() # to keep the window