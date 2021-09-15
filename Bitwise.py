Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 15
>>> b = 10
>>> bin(a)
'0b1111'
>>> bin(b)
'0b1010'
>>> bin(a & b)
'0b1010'
>>> a&&b
SyntaxError: invalid syntax
>>> a&b
10
>>> bin(a|b)
'0b1111'
>>> bin(a^b)
'0b101'
>>> a = true
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a = true
NameError: name 'true' is not defined
>>> a = True
>>> b =False
>>> a and b
False
>>> a or b
True
>>> a not b
SyntaxError: invalid syntax
>>> not a
False
>>> not b
True
>>> 
