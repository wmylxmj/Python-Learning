import turtle
import random
turtle.setup(960,720)
turtle.pensize(10)
x=0
y=0
dx=0
dy=0
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
for k in range(500):
    turtle.color(random.random(),random.random(),random.random())
    dx=random.uniform(-50,50)
    dy=random.uniform(-50,50)
    x=x+dx
    y=y+dy
    if x>480:
        x=x-dx
    elif x<-480:
        x=x-dx
    if y>360:
        y=y-dy
    elif y<-360:
        y=y-dy
    turtle.goto(x,y)
turtle.done()

