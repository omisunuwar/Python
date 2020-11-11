import urllib.request, urllib.error, urllib.parse
import ssl

import xml.etree.ElementTree as ET

#Ignore SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter url: ")
html=urllib.request.urlopen(url,context=ctx).read()
print("Retrieved characters: ",len(html))

tree=ET.fromstring(html)
lst=tree.findall(".//count")
print("Count: ",len(lst))
newlst=list()
for count in lst:
    newlst.append(int(count.text))
print("Sum: ",sum(newlst))
