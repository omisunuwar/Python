from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
count=input("Enter count: ")
count=int(count)
pos=input("Enter position: ")
pos=int(pos)

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tag=soup('a')
lnk=list()

for link in tag:
      lnk.append(link.get('href'))

print(lnk[pos-1])
pos1=pos
count=count-1

while(True):
    if count==0:break
    count=count-1
    url=lnk[pos-1]
    pos=pos1+len(lnk)
    html=urlopen(url, context=ctx).read()
    soup=BeautifulSoup(html,"html.parser")
    tag=soup("a")
    for link in tag:
        lnk.append(link.get('href'))
    print(lnk[pos-1])



