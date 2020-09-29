fname=input('Enter filename:')
if len(fname)<1: fname='mbox-short2.txt'
fhand=open(fname)
hrs=list()

for line in fhand:
    line.rstrip()
    #if not line.startswith('From'):continue
    #print(line)
    words=line.split()
    if line=='':continue #to ignore lines that start with blank space
    if len(words)<3:continue  # to ignore From: with 2 words
    if not line.startswith('From'):continue
    #if words[0]!='From':continue #Traceback:index is non-existant
    #word in words and w in word
    #print(line)
    atpos=line.find(':')
    newword=line[atpos-2:atpos]
    hrs.append(newword)
hrs.sort() #sort key i.e. in alphabetically(in increasing order)
#print(hrs)

#for making histogram of two tupple from list of hrs
counts=dict()
for hr in hrs:
    counts[hr]=counts.get(hr,0)+1
print(counts.items()) #counts.items()gives key, value pair i.e. tupple
    
#to print tupple    
for key,val in counts.items():
  print(key,val)



#########################################################
#to create reverse tupple to sort accouding to counts  
lst=list()
for key,val in counts.items():
    revtup=(val,key)
    lst.append(revtup)
    
lst=sorted(lst,reverse=True) #sorts according to value in decreasing order

print('Tupple sorted according to value:')
for val,key in lst:
    print(key,val)
