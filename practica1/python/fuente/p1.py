import turtle

import datetime

import time

 

 

hora_actual=datetime.datetime.now().time()

t = datetime.datetime.today().time()

 

lapiz = turtle.Turtle()

 

lapiz.speed(0)

 

lapiz.hideturtle()

lapiz.penup()

lapiz.goto(0,-180)

lapiz.pendown()

lapiz.circle(180)

 

 

for i in range (1,13):

    lapiz.pensize(3)

    lapiz.penup()

    lapiz.goto(0,0)

    lapiz.right(30)

    lapiz.forward(150)

    lapiz.pendown()

    lapiz.forward(30)

 

for i in range (1,61):

    lapiz.pensize(2)

    lapiz.penup()

    lapiz.goto(0,0)

    lapiz.right(6)

    lapiz.forward(170)

    lapiz.pendown()

    lapiz.forward(10)

 

lapiz.speed(0)

 

lapiz.showturtle()

lapiz.penup()

lapiz.goto(0,0)

lapiz.setheading(90)

lapiz.right(0.5*(60*t.hour+t.minute))

lapiz.pendown()

lapiz.forward(100)

 

lapiz.penup()

lapiz.goto(0,0)

lapiz.setheading(90)

lapiz.right(t.minute*360/60)

lapiz.pendown()

lapiz.forward(130)