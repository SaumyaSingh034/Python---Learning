import re
import urllib.request

#http://www.weather-forecast.com/locations/Varanasi/forecasts/latest

city = input("Enter your City : ")
url = "http://www.weather-forecast.com/locations/" +city+"/forecasts/latest"

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")


m = re.search('span class="phrase">',data1)
start = m.end()
end = start + 200

newString = data1[start:end]

print(newString)

