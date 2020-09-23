# Simple pong in Python 3 for beginners
# By Sixteefour
# Part 1 Getting started

import turtle

wn = turtle.Screen()
wn.title("Lalala")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("The Golden Rule", align="center", font=("Courier", 24, "bold"))

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write("Do your best!", align="center", font=("Courier", 24, "italic"))
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Be respectful to everyone in the world", align="center", font=("Courier", 24, "italic"))


# Main game loop
while True:
    wn.update()