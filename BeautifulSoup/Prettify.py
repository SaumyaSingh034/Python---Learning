Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<html><head><title>Hello World</title><p>Hii this is a paragaraph<strong>Saumya SIngh</html>","html.parser")
>>> soup.prettify
<bound method Tag.prettify of <html><head><title>Hello World</title><p>Hii this is a paragaraph<strong>Saumya SIngh</strong></p></head></html>>
>>> print(soup.prettify())
<html>
 <head>
  <title>
   Hello World
  </title>
  <p>
   Hii this is a paragaraph
   <strong>
    Saumya SIngh
   </strong>
  </p>
 </head>
</html>
>>> 
