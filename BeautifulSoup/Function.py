Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
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
>>> soup = BeautifulSoup(html_doc,"html.parser")
>>> soup
 <html><head><title>The Cindrella Story</title></head>
<body>
<p class="title"><b>The Cindrella Story</b></p>
<p class="story">Once upon a time there was a princess who lives with her step mother. Her step mother torture her very much
<a class="princess" href="http://princess.disney.com/cinderellas-story" id="link1">Cindrella</a>,
<a class="Stepmother" href="https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" id="link2">Marteinaa</a> and
<a class="prince" href="https://www.youtube.com/watch?v=AVCardOjkKM&amp;index=57&amp;list=PLV4q1BPMpwGNqbgkUrdYOWsoOpWdH8b04" id="link3">Facsen</a>;
and ther live at the bottom of well</p>
<p class="story">....</p>
</body></html>
>>> head_tag = soup.head
>>> head_tag
<head><title>The Cindrella Story</title></head>
>>> head_tag.contents
[<title>The Cindrella Story</title>]
>>> body_tag = soup.body
>>> for i in body_tag.children:
	print(i)

	


<p class="title"><b>The Cindrella Story</b></p>


<p class="story">Once upon a time there was a princess who lives with her step mother. Her step mother torture her very much
<a class="princess" href="http://princess.disney.com/cinderellas-story" id="link1">Cindrella</a>,
<a class="Stepmother" href="https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" id="link2">Marteinaa</a> and
<a class="prince" href="https://www.youtube.com/watch?v=AVCardOjkKM&amp;index=57&amp;list=PLV4q1BPMpwGNqbgkUrdYOWsoOpWdH8b04" id="link3">Facsen</a>;
and ther live at the bottom of well</p>


<p class="story">....</p>


>>> for i in body_tag.descendants:
	print(i)

	


<p class="title"><b>The Cindrella Story</b></p>
<b>The Cindrella Story</b>
The Cindrella Story


<p class="story">Once upon a time there was a princess who lives with her step mother. Her step mother torture her very much
<a class="princess" href="http://princess.disney.com/cinderellas-story" id="link1">Cindrella</a>,
<a class="Stepmother" href="https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" id="link2">Marteinaa</a> and
<a class="prince" href="https://www.youtube.com/watch?v=AVCardOjkKM&amp;index=57&amp;list=PLV4q1BPMpwGNqbgkUrdYOWsoOpWdH8b04" id="link3">Facsen</a>;
and ther live at the bottom of well</p>
Once upon a time there was a princess who lives with her step mother. Her step mother torture her very much

<a class="princess" href="http://princess.disney.com/cinderellas-story" id="link1">Cindrella</a>
Cindrella
,

<a class="Stepmother" href="https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" id="link2">Marteinaa</a>
Marteinaa
 and

<a class="prince" href="https://www.youtube.com/watch?v=AVCardOjkKM&amp;index=57&amp;list=PLV4q1BPMpwGNqbgkUrdYOWsoOpWdH8b04" id="link3">Facsen</a>
Facsen
;
and ther live at the bottom of well


<p class="story">....</p>
....


>>> 
for i in body_tag.string:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    for i in body_tag.string:
TypeError: 'NoneType' object is not iterable
>>> head_tag = soup.head
>>> head_tag.title
<title>The Cindrella Story</title>
>>> head_tag.title.string
'The Cindrella Story'
>>>  head_tag>string
 
SyntaxError: unexpected indent
>>> head_tag.string
'The Cindrella Story'
>>> head_tag.parent
<html><head><title>The Cindrella Story</title></head>
<body>
<p class="title"><b>The Cindrella Story</b></p>
<p class="story">Once upon a time there was a princess who lives with her step mother. Her step mother torture her very much
<a class="princess" href="http://princess.disney.com/cinderellas-story" id="link1">Cindrella</a>,
<a class="Stepmother" href="https://disneyland.disney.go.com/?DISCID=DI_mtt_chrome_dropdown_dlr" id="link2">Marteinaa</a> and
<a class="prince" href="https://www.youtube.com/watch?v=AVCardOjkKM&amp;index=57&amp;list=PLV4q1BPMpwGNqbgkUrdYOWsoOpWdH8b04" id="link3">Facsen</a>;
and ther live at the bottom of well</p>
<p class="story">....</p>
</body></html>
>>> head_tag.string.parent
<title>The Cindrella Story</title>
>>> 
