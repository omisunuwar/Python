import re
name=input('Enter filename:')
if len(name)<1: name='regex_sum_976999.txt'
try:
    fhand=open(name)
except:
    print("File cannot be opened")
    quit()

numlist=list()
for line in fhand:
    line=line.rstrip()
    stuff=re.findall('[0-9]+',line)
    for s in stuff:
        num=int(s)
        numlist.append(num)

sum=None

for num in numlist:
    if sum is None:
        sum=num
    else:
        sum=sum+num

print(sum)
