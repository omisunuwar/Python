fname=input('Enter filename:')
if len(fname)<1: fname='mbox-short2.txt'
fhand=open(fname)
hrs=list()

for line in fhand:
    line.rstrip()
    words=line.split()
    if line==' ':continue #to ignore lines that start with blank space
    if len(words)<3:continue  # to ignore lines with 2 words
    if not line.startswith('From'):continue
    atpos=line.find(':')
    newword=line[atpos-2:atpos]
    hrs.append(newword)
    
hrs.sort() #sort key i.e. in alphabetically increasing order

#for making histogram 
counts=dict()
for hr in hrs:
    counts[hr]=counts.get(hr,0)+1
    
 #counts.items()gives two tupple of key, value 
 #to print tupple    
for key,val in counts.items():
  print(key,val)

#to create reverse tupple to sort accouding to counts  
lst=list()
for key,val in counts.items():
    revtup=(val,key)
    lst.append(revtup)
    
lst=sorted(lst,reverse=True) #sorts according to value in decreasing order

print('Tupple sorted according to value:')
for val,key in lst:
    print(key,val)
