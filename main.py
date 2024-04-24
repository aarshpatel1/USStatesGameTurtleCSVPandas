import pandas
import turtle

screen = turtle.Screen()
screen.title("US State Game")

IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# TODO: check if guess is among the 50 states
states_data = pandas.read_csv("50_states.csv")
# print(states_data)
states = states_data["state"].to_list()


# print(states)


def write_state_names(state_name, x_cord, y_cord):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(x_cord, y_cord)
    new_turtle.write(state_name)


# TODO: record the correct guesses in a list
correct_answer = []

# TODO: keep track of the score
score = 0

# TODO: use a loop to allow the user to keeping guessing
is_game_on = True
while is_game_on:
    # TODO: convert guess to title case
    answer_state = turtle.textinput(title=f"{score}/{len(states)}", prompt="What is the another state name?: ").title()
    if (answer_state in states) and (answer_state not in correct_answer):
        # TODO: write correct guess onto map
        state = states_data[states_data["state"] == answer_state]
        write_state_names(answer_state, int(state.x), int(state.y))
        correct_answer.append(answer_state)
        score += 1

    if score == 50:
        is_game_on = False

screen.exitonclick()
