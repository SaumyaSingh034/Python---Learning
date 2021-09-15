Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: D:/Practice/Python/FileInput/Read.py ===============
Traceback (most recent call last):
  File "D:/Practice/Python/FileInput/Read.py", line 2, in <module>
    print(file.read())
AttributeError: 'tuple' object has no attribute 'read'
>>> 
=============== RESTART: D:/Practice/Python/FileInput/Read.py ===============
This is a Python File.


Python is a fantastic Language


I love Python.....
>>> 
=============== RESTART: D:/Practice/Python/FileInput/Read.py ===============
This is a Python File.


Python is a fantastic Language


I love Python.....

>>> file.read()
''
>>> file.read()
''
>>> file.seek(0,0)
0
>>> 
KeyboardInterrupt
>>> file.read()
'This is a Python File.\n\n\nPython is a fantastic Language\n\n\nI love Python.....'
>>> file.read()
''
>>> file.seek(0,0)
0
>>> file.read(21)
'This is a Python File'
>>> file.read(21)
'.\n\n\nPython is a fanta'
>>> file.tell()
45
>>> 
