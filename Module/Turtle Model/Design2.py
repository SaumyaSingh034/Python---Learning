import turtle
localWindow = turtle.Screen()
turtle.colormode(255)

turtle.speed(0)

sides = 6

def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)


for i in range(50):
    shape(2*i,sides)
    turtle.left(i)

    
