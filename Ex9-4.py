fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short2.txt"
fhand = open(fname)

enames=list()
counts=dict()

for line in fhand:
    line.rstrip()
    words=line.split()
    if words[0]!='From:' or len(words)<2 continue
    else:
        enames.append(word[1])

for ename in enames:
    count[ename]=counts.get(ename,0)+1

bigcount=None
bigname=None
for ename,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigename=ename

print(bigename,bigcount)
