
from re import findall
import urllib.request
import os
os.system('cls')
# os.system('clear')


url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"

response = urllib.request.urlopen(url)

html = response.read()

htmlStr = html.decode()
print(htmlStr)
pdata = findall("\([1-9]{3}\) \d{3}-\d{4}", htmlStr)

for item in pdata:
    print(item)
