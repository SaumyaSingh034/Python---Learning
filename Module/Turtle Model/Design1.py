import turtle
localWindow = turtle.Screen();

turtle.speed(0)

sides = 5

def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(90)


for i in range(100):
    shape(5*i,sides)
    turtle.left(i)
