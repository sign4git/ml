import turtle
import pandas as pd

# read states data
states_data = pd.read_csv("50_states.csv")
state_list = states_data["state"].to_list()

# initialize screen and mount the map
screen = turtle.Screen()
screen.title("United States - Guess the States")
image_file = "blank_states_img.gif"
screen.addshape(image_file)
turtle.shape(image_file)

# list of states guessed correctly
guessed_states = []

while len(guessed_states) < 50:
    # get the state name from the user
    state_name = screen.textinput(title=f"States Guessed {len(guessed_states)}/50",
                                  prompt="Guess the state: ").title()

    # if the user types "Exit" exit from the game
    if state_name == "Exit":
        break

    # check if the state is valid and add to guessed_states list if valid and not guessed previously
    if state_name not in guessed_states and state_name in state_list:
        current_state_df = states_data[states_data["state"] == state_name]
        co_ordinates = (current_state_df["x"].to_list()[0], current_state_df["y"].to_list()[0])
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(co_ordinates)
        new_turtle.write(f"{state_name}", align="center", font=("Arial", 8, "normal"))
        guessed_states.append(state_name)


# export list of states to be learnt
states_to_learn = []
for state in state_list:
    new_state = {}
    if state not in guessed_states:
        new_state["state"] = state
        states_to_learn.append(new_state)

states_to_learn = pd.DataFrame(states_to_learn)
states_to_learn.to_csv("states_to_learn.csv")
