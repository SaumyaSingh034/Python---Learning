Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> inputStatement = sys.stdin.readline()
This is a new way to take input but the only difference between this method and previous one it could only read upto where we want
>>> inputStatement
'This is a new way to take input but the only difference between this method and previous one it could only read upto where we want\n'
>>> inputStatement = sys.stdin.readline(20)
'This is a new way to take input but the only difference between this method and previous one it could only read upto where we want\n'
>>> inputStatement
"'This is a new way t"
>>> 
