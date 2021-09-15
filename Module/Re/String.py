Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> string = "Just waiting for the day where I could make my parents happy"
>>> string
'Just waiting for the day where I could make my parents happy'
>>> import re
>>> string = "Just waiting for the day where I could make my parents happy"
>>> re.search("parents",string)
<_sre.SRE_Match object; span=(47, 54), match='parents'>
>>> string.start()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    string.start()
AttributeError: 'str' object has no attribute 'start'
>>> position = re.search("parents",string)
>>> position.start()
47
>>> position.end()
54
>>> string[position.start(),position.end()]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    string[position.start(),position.end()]
TypeError: string indices must be integers
>>> string[position.start():position.end()]
'parents'
>>> 
