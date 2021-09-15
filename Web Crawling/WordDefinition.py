import re
import urllib.request

#http://www.dictionary.com/browse/fantastic

url = "http://www.dictionary.com/browse/"

word = input("Enter your Word : ")
try:
    url = url + word
    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")
    #print(data1)
    m = re.search('meta name="description" content="',data1)
    start = m.end()
    end = start+300
    newString = data1[start:end]
    #print(newString)
    m = re.search("See more",newString)
    end = m.start()-1
    definition = newString[0:end]
    print(definition)

except:
    print("This word is not found in dicitonary")
