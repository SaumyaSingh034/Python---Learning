Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f = open("WriteFile.txt","a")
>>> f.write("\n This is my appending text, lets see if it works or not")
56
>>> f.close()
>>> f = open("WriteFile.txt","r")
>>> f.read()
'A new file is created \n Lets see if it works or not\n This is my appending text, lets see if it works or not'
>>> 
