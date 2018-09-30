from turtle import *
speed(0)
colors = ["red","blue","purple","yellow","grey"]
colormode()
for color in colors:
    pencolor(color)
    fillcolor(color)
    begin_fill()
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    end_fill()

mainloop()