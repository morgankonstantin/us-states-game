import turtle

import pandas
import pandas as pd
from pandas import DataFrame

# Screen setup
screen = turtle.Screen()
screen.setup(width=750, height=500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_ans = 0  # Track correct guesses

data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()  # Convert the input to title case
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)  # Convert list to DataFrame
        new_data.to_csv("states_to_learn")  # Create a new csv with the missed states
        break
    # Check for the answer in the states_list, place label on the map if the guess is correct
    if answer_state in states_list:
        guessed_states.append(answer_state)
        states_list.remove(answer_state)
        new_label = turtle.Turtle()  # Create a new turtle object
        new_label.hideturtle()
        new_label.pu()  # penup() so it won't draw any line
        state_query = data.query(f" @answer_state == state ")
        new_label.goto(x=int(state_query.x), y=int(state_query.y))
        new_label.write(answer_state)

screen.exitonclick()
