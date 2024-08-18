import turtle
import pandas as pd
from namer import State_name


country_images=["blank_states_img.gif"]
sname=State_name()
screen=turtle.Screen()

data=pd.read_csv("50_states.csv")
screen.title("United States game")
screen.listen()
screen.addshape("blank_states_img.gif")
count=0
turtle.shape("blank_states_img.gif")
guessed_states=[]

while count<50:
    answer_state=screen.textinput(f"{count}/50 states named","What's the next state?").title()
    if answer_state=="Exit":
        break


    elif answer_state in data.state.array:
        mango=data[data.state ==f"{answer_state}"]["x"]
        coco=data[data.state ==f"{answer_state}"]["y"]
        sname.turtplace(int(mango),int(coco),answer_state)
        guessed_states.append(answer_state)
        count+=1
    
states_left=[i for i in data.state.to_list() if i not in guessed_states]
newdat=pd.DataFrame(states_left)
newdat.to_csv("States_left.csv")



