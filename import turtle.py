import turtle

screen=turtle.Screen() 
image="australia_state.gif"
screen.addshape(image)

turtle.shape(image)

screen.listen()
def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)


turtle.mainloop()


