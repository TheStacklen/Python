from turtle import *
import math
bgcolor("black")
speed(10000)
color("red")
pensize(2)
def heart(n):
    x=15*math.sin(n)**3
    y=12*math.cos(n)-5*\
        math.cos(2*n)-2*\
        math.cos(3*n)-2*\
        math.cos(4*n)
    return x , y
for i in range(10):
    pendown()
    for j in range(0,100):
        x, y =heart(j/15)
        goto(x*i, y*i)
    penup()
    hideturtle()
done()

