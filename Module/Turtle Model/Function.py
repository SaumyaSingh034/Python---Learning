Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> def square(side):
	for in in range(0,5):
		
SyntaxError: invalid syntax
>>> def square(side):
	for i in range(0,5):
		t.forward(side)
		t.left(90)

		
>>> square(10)
>>> square(30)
>>> square(50)
>>> square(100)
>>> square(500)
>>> t.reset()
>>> def square(side):
	for i in range(0,5):
		t.forward(side)
		t.left(90)

		
>>> square(50)
>>> square(30)
>>> t.up()
>>> t.right(180)
>>> t.forward(50)
>>> t.down()
>>> def rectangle(sidex,sidey):
	for i in range(0,5):
		t.forward(sidex)
		t.left(sidey)

		
>>> rectangle(4,5)
>>> def rectangle(sidex,sidey):
	for i in range(0,5):
		t.forward(sidex)
		t.left(90)

		
>>> rectangle(4,5)
>>> def circle(radius):
	t.circle(radius)

	
>>> circle(20)
>>> circle(50)
>>> circle(80)
>>> 
