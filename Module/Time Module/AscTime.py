Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> time.asctime()
'Thu Aug 10 14:35:35 2017'
>>> tup = time.asctime(2017,15,15,8,45,12,6,0,0)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tup = time.asctime(2017,15,15,8,45,12,6,0,0)
TypeError: asctime expected at most 1 arguments, got 9
>>> tup = (2017,15,15,3,45,16,6,0,0)
>>> time.asctime(tup)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    time.asctime(tup)
ValueError: month out of range
>>> tup = (2017,8,15,3,45,16,6,0,0)
>>> time.asctime(tup)
'Sun Aug 15 03:45:16 2017'
>>> 
