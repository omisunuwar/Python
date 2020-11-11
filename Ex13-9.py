import urllib.request, urllib.error, urllib.parse
import json
import ssl

#Ignore ssl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter url: ")
uh=urllib.request.urlopen(url,context=ctx)
data=uh.read().decode()
print("Retrieved", len(data),"characters")
try:
    js=json.loads(data)
except:
    js=None
    quit()

#print(json.dumps(js,indent=2))

num=list()
for item in js["comments"]:
    num.append(item["count"])

print("Count: ",len(num))
print("Sum: ",sum(num))
