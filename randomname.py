# Drawing a car


import time
import turtle
t = turtle.Pen()
t.color("red")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(20)
t.left(90)
t.forward(50)
t.right(45)
t.forward(20)
t.forward(30)
t.left(45)
t.forward(50)
t.left(45)
t.forward(20)
t.forward(30)
t.left(45)
t.forward(20)
t.left(90)
t.forward(50)
t.forward(50)
t.forward(50)
t.up()
t.right(90)
t.forward(20)
t.right(90)
t.right(90)
t.forward(10)
t.forward(10)
t.end_fill()
t.down()
# the first wheel
t.color("black")
t.begin_fill()
# The second wheel
t.circle(10)
t.end_fill()
t.up()
t.left(90)
t.forward(50)
t.forward(50)
t.right(90)
t.down()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()
t.up()
t.forward(60)
t.right(45)
t.down()
t.forward(200)
t.right(45)
t.right(45)
t.forward(300)
t.left(180)
t.forward(250)
t.color("white")
t.begin_fill()
t.left(45)
t.forward(20)
t.forward(20)
t.forward(35)
t.end_fill()

# Setup the Screen

wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("Basic Turtle Graphics")


# Main Game loop
while True:
    wn.update()


wn.mainloop()
