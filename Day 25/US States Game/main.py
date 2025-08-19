from turtle import Turtle, Screen

# set up the screen
screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

# preparing the data
import pandas

states_data = pandas.read_csv("50_states.csv")

state_column = states_data.state.to_list()
x_column = states_data.x.to_list()
y_column = states_data.y.to_list()

states_data_dict = {}
x_index = 0
y_index = 0
for state in state_column:
    states_data_dict[state] = []
    states_data_dict[state].append(x_column[x_index])
    states_data_dict[state].append(y_column[y_index])
    x_index += 1
    y_index += 1

# logic of the game
import time
correct_guesses = 0
written_states = []
while correct_guesses < len(states_data_dict):
    user_guess = screen.textinput(f"Correct States US: {correct_guesses}/50", "What is the next state? ").title()
    if user_guess == "Exit":
        break
    new_turtle = Turtle()
    new_turtle.hideturtle()
    new_turtle.up()
    if user_guess in states_data_dict:
        if user_guess not in written_states:
            correct_guesses += 1
            written_states.append(user_guess)
            new_turtle.goto(states_data_dict[user_guess])
            new_turtle.write(arg=user_guess, align="center", font=("Courier", 10, "normal"))
    else:
        new_turtle.goto(0, 250)
        new_turtle.write(arg=f"Sorry, {user_guess} wasn't found it", align="center", font=("Courier", 15, "bold"))
        time.sleep(3)
        new_turtle.clear()

if len(written_states) == len(states_data_dict):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.up()
    turtle.goto(0, 250)
    turtle.write(arg="Congratulations yo did it!", align="center", font=("Courier", 20, "bold"))
else:
    with open("states_missing.csv", "w") as states_missing_file:
        states_missing_file.write("Missing states:\n")
        for state in states_data_dict:
            if state not in written_states:
                states_missing_file.write(state + '\n')

screen.exitonclick()