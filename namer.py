from turtle import Turtle

class State_name(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        
    def turtplace(self,x,y,aple):
        self.goto(x,y)
        self.write(f"{aple}", False, "center",('Arial', 8, 'normal'))

    def end_game(self):
        self.home()
        self.write("Congrats you have named all of the states ", False, "center",('comic Sans MS', 32, 'bold'))
