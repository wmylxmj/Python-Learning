import turtle
import random
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("green")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.pensize(7)
turtle.pencolor("red")
turtle.circle(0,0)
turtle.pensize(10)
for j in range(20):
    turtle.penup()
    turtle.goto(random.uniform(-325,325),random.uniform(-175,175))
    turtle.color(random.random(),random.random(),random.random())
    turtle.pendown()
    turtle.circle(0,0)
x=0
y=0
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
for k in range(100):
    turtle.color(random.random(),random.random(),random.random())
    x=x+random.uniform(-25,25)
    y=y+random.uniform(-25,25)
    turtle.goto(x,y)
turtle.done()

