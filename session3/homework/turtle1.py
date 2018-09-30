from turtle import *

speed(0)
colormode()
pencolor("blue")
for _ in range (4):
    forward (100)
    left (90)
pencolor("red")
left (60)
forward (100)
right (120)
forward (100)
left(132)

forward(100)
for _ in range (3):
    left (72)
    forward (100)

pencolor("yellow")
left(72)
for _ in range (6):
    forward (100)
    left (60)

pencolor("grey")
for _ in range (7):
    forward(100)
    left (180.0 -(900/7))




mainloop()