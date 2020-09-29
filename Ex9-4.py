fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short2.txt"
fhand = open(fname)

enames=list()
counts=dict()

for line in fhand:
    line.rstrip()
    if not line.startswith('From:'):continue
    else:
        words=line.split()
       # if len(words)<3 or words[0]!='From:':continue
        enames.append(words[1])
    #print(enames)

for ename in enames:
    counts[ename]=counts.get(ename,0)+1

bigcount=None
bigename=None
for ename,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigename=ename

print(bigename,bigcount)
