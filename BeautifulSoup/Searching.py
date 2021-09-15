Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  html_doc = """ <html><head><title>The Cindrella Story</title></head>
<body>
<p class = "title"><b>The Cindrella Story</b></p>
<p class = "story">Once upon a time there was a princess who lives with her step mother. Her step mother torture her very much
<a href = "http://princess.disney.com/cinderellas-story" class = "princess" id = "link1">Cindrella</a>,
<a href = "https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" class = "Stepmother" id = "link2">Marteinaa</a> and
<a href = "https://www.youtube.com/watch?v=AVCardOjkKM&index=57&list=PLV4q1BPMpwGNqbgkUrdYOWsoOpWdH8b04" class = "prince" id = "link3">Facsen</a>;
and ther live at the bottom of well</p>
<p class = "story">....</p>
"""
 
SyntaxError: unexpected indent
>>> html_doc = """ <html><head><title>The Cindrella Story</title></head>
<body>
<p class = "title"><b>The Cindrella Story</b></p>
<p class = "story">Once upon a time there was a princess who lives with her step mother. Her step mother torture her very much
<a href = "http://princess.disney.com/cinderellas-story" class = "princess" id = "link1">Cindrella</a>,
<a href = "https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" class = "Stepmother" id = "link2">Marteinaa</a> and
<a href = "https://www.youtube.com/watch?v=AVCardOjkKM&index=57&list=PLV4q1BPMpwGNqbgkUrdYOWsoOpWdH8b04" class = "prince" id = "link3">Facsen</a>;
and ther live at the bottom of well</p>
<p class = "story">....</p>
"""
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(html_docs,"html.parser")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    soup = BeautifulSoup(html_docs,"html.parser")
NameError: name 'html_docs' is not defined
>>> soup = BeautifulSoup(html_doc,"html.parser")
>>> print(soup.prettify())
<html>
 <head>
  <title>
   The Cindrella Story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Cindrella Story
   </b>
  </p>
  <p class="story">
   Once upon a time there was a princess who lives with her step mother. Her step mother torture her very much
   <a class="princess" href="http://princess.disney.com/cinderellas-story" id="link1">
    Cindrella
   </a>
   ,
   <a class="Stepmother" href="https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" id="link2">
    Marteinaa
   </a>
   and
   <a class="prince" href="https://www.youtube.com/watch?v=AVCardOjkKM&amp;index=57&amp;list=PLV4q1BPMpwGNqbgkUrdYOWsoOpWdH8b04" id="link3">
    Facsen
   </a>
   ;
and ther live at the bottom of well
  </p>
  <p class="story">
   ....
  </p>
 </body>
</html>
>>> soup.find_all("p")
[<p class="title"><b>The Cindrella Story</b></p>, <p class="story">Once upon a time there was a princess who lives with her step mother. Her step mother torture her very much
<a class="princess" href="http://princess.disney.com/cinderellas-story" id="link1">Cindrella</a>,
<a class="Stepmother" href="https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" id="link2">Marteinaa</a> and
<a class="prince" href="https://www.youtube.com/watch?v=AVCardOjkKM&amp;index=57&amp;list=PLV4q1BPMpwGNqbgkUrdYOWsoOpWdH8b04" id="link3">Facsen</a>;
and ther live at the bottom of well</p>, <p class="story">....</p>]
>>> soup.find_all('a')
[<a class="princess" href="http://princess.disney.com/cinderellas-story" id="link1">Cindrella</a>, <a class="Stepmother" href="https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" id="link2">Marteinaa</a>, <a class="prince" href="https://www.youtube.com/watch?v=AVCardOjkKM&amp;index=57&amp;list=PLV4q1BPMpwGNqbgkUrdYOWsoOpWdH8b04" id="link3">Facsen</a>]
>>> soup.find_all(id=link2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    soup.find_all(id=link2)
NameError: name 'link2' is not defined
>>> soup.find_all(id='link2')
[<a class="Stepmother" href="https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" id="link2">Marteinaa</a>]
>>> soup.find_all("a",id='link2')
[<a class="Stepmother" href="https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" id="link2">Marteinaa</a>]
>>> import re
>>> for tag in soup.find_all(re.compile("^b")):
	print(tag.name)

	
body
b
>>> for tag in soup.find_all(re.compile("t")):
	print(tag.name)

	
html
title
>>> 
