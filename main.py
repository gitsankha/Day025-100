import turtle
import pandas


FONT = ('Arial', 8, 'normal')


screen = turtle.Screen()
screen.title("U.S. Statename Game")
screen.bgpic("blank_states_img.gif")


df = pandas.read_csv("50_states.csv")
stateslist = df.state.to_list()



guessed_state_list = []
while len(guessed_state_list) < 50:
    answer = screen.textinput(title = f"{len(guessed_state_list)}/50 States", prompt = "Enter a state name:").title()
    
    if answer == "Exit":
        not_guessed_list = []
        for state in stateslist:
            if state not in guessed_state_list:
                not_guessed_list.append(state)
        missed_states = pandas.DataFrame(not_guessed_list)
        missed_states.to_csv("states_to_learn.csv")
        break
    
    for state in stateslist:
        if state == answer:
            guessed_state_list.append(answer)
            state_x = df[df["state"] == answer].x.item()
            state_y = df[df["state"] == answer].y.item()
            statename = turtle.Turtle()
            statename.hideturtle()
            statename.penup()
            statename.goto(state_x, state_y)
            statename.write(arg = answer, align = "center", font  = FONT)



           
screen.mainloop()

