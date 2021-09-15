Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> time.localtime()
time.struct_time(tm_year=2017, tm_mon=8, tm_mday=10, tm_hour=14, tm_min=42, tm_sec=1, tm_wday=3, tm_yday=222, tm_isdst=0)
>>> t = localtime()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t = localtime()
NameError: name 'localtime' is not defined
>>> t = time.localtime()
>>> year = t[0]
>>> day = t[2]
>>> month = t[1]
>>> year
2017
>>> day
10
>>> month
8
>>> print(day+" " +month+ " " +year+" ")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(day+" " +month+ " " +year+" ")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(str(day)+" " +str(month)+ " " +str(year)+" ")
10 8 2017 
>>> print(str(day)+"/" +str(month)+ "/" +str(year)+)
SyntaxError: invalid syntax
>>> 
