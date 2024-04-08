#Tyler Smith
#P4Lab1
#04/04/24
#Turtle writes Initials for Tyler Smith.
import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
Turtle = turtle.Turtle()
Turtle.shape("turtle")
Turtle.color("cyan")
Turtle.pensize(11)
Turtle.pendown()
size = 50
#T
Turtle.speed(1)
Turtle.forward(100)
Turtle.left(180)
Turtle.forward(50)
Turtle.left(85)
Turtle.forward(100)
Turtle.left(5)
time.sleep(1)
Turtle.penup()
#Move right
Turtle.left(90)
Turtle.forward(60)
#S
Turtle.pendown()
Turtle.forward(40)
for i in range(180):
    Turtle.forward(.4363333334)
    Turtle.left(1)
for i in range(180):
    Turtle.forward(.4363333334)
    Turtle.right(1)
#Turtle forward
Turtle.forward(40)
Turtle.penup()
Turtle.forward(40)
Turtle.right(1980)
time.sleep(5)


