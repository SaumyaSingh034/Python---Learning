Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> for i in range(0,100):
	t.forward(100)
	t.right(179)

	
>>> t.reset()
>>> for i in range(1,100):
	t.forward(100)
	t.right(95)

	
>>> t.reset()
>>> t.right(180)
>>> t.forward(50)
>>> t.right(180)
>>> for i in range(1,20):
	t.forward(100)
	t.right(95)

	
>>> t.up()
>>> t.left(100)
>>> t.right(180)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(95)
>>> t.forward(50)
>>> t.forward(20)
>>> t.down()
>>> for i in range(1,20):
	t.forward(100)
	t.right(95)

	
>>> t.up()
>>> t.foward(100)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t.foward(100)
AttributeError: 'Turtle' object has no attribute 'foward'
>>> t.forward(100)
>>> t.forward(50)
>>> t.down()
>>> for i in range(1,20):
	t.forward(100)
	t.right(95)

	
>>> 
