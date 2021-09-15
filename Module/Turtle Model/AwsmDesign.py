from turtle import *

shape("turtle")
wheel = 12
bgcolor("powderblue")
pensize(10)
pencolor("red")

for i in range(wheel):
    begin_fill();rt(90);fd(100);lt(120);fd(150);lt(100);fd(100);end_fill()
    fd(200)
