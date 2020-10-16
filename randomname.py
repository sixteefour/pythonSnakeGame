# Drawing a car
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
t.forward(20)
t.right(90)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
t.up()
t.left(90)
t.forward(70)
t.right(45)
t.color("brown")
t.begin_fill()
t.down()
t.forward(100)
t.left(45)
t.left(45)
t.forward(100)
t.left(45)
t.left(45)
t.left(45)
t.forward(143)
t.end_fill()
# the sun
t.color("red")
t.up()
t.forward(300)
t.left(90)
t.forward(200)
t.right(90)
t.forward(50)
t.color("yellow")
t.begin_fill()
t.left(90)
t.down()
t.circle(50)
t.end_fill()
t.up()
t.left(90)
t.forward(50)
t.forward(250)
t.down()


# Setup the Screen
wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("Basic Turtle Graphics")


while True:
    wn.update()


wn.mainloop()
