import turtle
import pandas
screen = turtle.Screen()
screen.title("US State Game")
image = "./blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states =data["state"].to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="Whats the another state's name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)

        # states to learn.csv
        final_data = pandas.DataFrame(missing_states)
        final_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


turtle.mainloop() # makes sure that window doesnt close

"""
If answer_state is one of the states in all the states of the 50 states
    If they get it right
        create a turtle to write the name of the state at the state's x and y coordinate
"""