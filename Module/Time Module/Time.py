Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> def number(n):
	time1 = time.time()
	for i in range(0,100):
		print(i)
	time2 = time.time()
	print(str(time2-time1))

	
>>> def number(n):
	time1 = time.time()
	for i in range(0,max):
		print(i)
	time2 = time.time()
	print(str(time2-time1))

	
>>> number(10)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    number(10)
  File "<pyshell#9>", line 3, in number
    for i in range(0,max):
TypeError: 'builtin_function_or_method' object cannot be interpreted as an integer
>>> def number(n):
	time1 = time.time()
	for i in range(0,n):
		print(i)
	time2 = time.time()
	print(str(time2-time1))

	
>>> number(20)
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
0.2723064422607422
>>> 
