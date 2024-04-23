import pandas
import turtle

screen = turtle.Screen()
screen.title("US State Game")

IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)
turtle.hideturtle()

# TODO: convert guess to title case
answer_state = turtle.textinput(title="Guess the State", prompt="What is the another state name?: ").capitalize()

# TODO: check if guess is among the 50 states
states_data = pandas.read_csv("50_states.csv")
print(states_data)
states = states_data["state"].to_list()
print(states)


def write_state_names(state_name, x_cord, y_cord):
    new_turtle = turtle.Turtle()
    new_turtle.goto(x_cord, y_cord)
    new_turtle.write(state_name, align="center", font=("arial", 10, "bold"))


if answer_state in states:
    # TODO: write correct guess onto map
    state = states_data[states_data["state"] == answer_state]
    print(state.x.to_string())
    print(state.y)
    # write_state_names(state, state.x, state.y)

# TODO: use a loop to allow the user to keeping guessing

# TODO: record the correct guesses in a list

# TODO: keep track of the score


screen.exitonclick()
