Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> for i in range(0,8):
	t.forward(50)
	t.left(45)

	
>>> t.reset()
>>> for i in range(1,100)
SyntaxError: invalid syntax
>>> for i in range(1,100):
	t.forward(100)
	t.left(175)

	

tttt
>>> t.reset()
>>> for i in range(1,100):
	t.forward(100)
	t.left(95)

	
>>> t.reset()
>>> for i in range(1,100):
	t.forward(500)
	t.right(79)

	
Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    t.forward(500)
  File "C:\Users\ASUSLP\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1637, in forward
    self._go(distance)
  File "C:\Users\ASUSLP\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Users\ASUSLP\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 3178, in _goto
    self._pencolor, self._pensize, top)
  File "C:\Users\ASUSLP\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Users\ASUSLP\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 2463, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> for i in range(1,100):
	t.forward(100)
	t.right(79)

	
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    t.forward(100)
  File "C:\Users\ASUSLP\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1637, in forward
    self._go(distance)
  File "C:\Users\ASUSLP\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Users\ASUSLP\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 3158, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Users\ASUSLP\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 755, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Users\ASUSLP\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 2463, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
>>> 
