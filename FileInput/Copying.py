Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ufn = input("Enter your filename: ")
Enter your filename: TestFile.txt
>>> file1 = open(ufn,"r")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    file1 = open(ufn,"r")
FileNotFoundError: [Errno 2] No such file or directory: 'TestFile.txt'
>>> ufn = input("Enter your file Name: ")
Enter your file Name: WriteFile
>>> ufn = ufn+".txt"
>>> file1 = open(ufn,"r")
>>> file2 = open("CopyFile.txt","w")
>>> file2.write(file1.read())
119
>>> file1.close()
>>> file2.close()
>>> file2 = open("CopyFile.txt","r")
>>> file2.read()
'A new file is created \n Lets see if it works or not\n This is my appending text, lets see if it works or notSaumya singh'
>>> 
