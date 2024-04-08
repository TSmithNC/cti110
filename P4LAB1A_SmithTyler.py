 
#this code contains uses turtle to draw a square and triangle. Turtle turns left when he should turn right.
#Turtle draws a primitive house.

import turtle
wn = turtle.Screen()
wn.bgcolor("gray")
Turtle = turtle.Turtle()
Turtle.shape("turtle")
Turtle.color("blue")

Turtle.pendown()
size = 50

for i in [0,1,2,3]:
    Turtle.speed(1)
    Turtle.forward(100)
    Turtle.left(90)
Turtle.penup()
Turtle.left(90)
Turtle.forward(110)
Turtle.pendown()
Turtle.right(90)
for i in [0,1,2]:
    Turtle.speed(1)
    Turtle.forward(100)
    Turtle.left(120)

