#file is mbox-short2.txt

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short2.txt" #press enter defaults to mbox-short2.txt

fhand = open(fname)
count = 0

for line in fhand:
    line=line.rstrip()
    words=line.split()
    #if len(words)<3: continue #Guardian pattern to see if the word is short or 1 word
    if line=='':continue  #to skip blank lines
    if words[0]!='From' or len(words)<3:continue #doesn't work words[0] is blank space in someof the lines
    count=count+1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")

#if words[0]!='From:' or len(words)<3:continue --doesn't work

#if not line.startswith('From') or len(words)<3:continue
