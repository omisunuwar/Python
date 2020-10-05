#file is mbox-short2.txt

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short2.txt"

fhand = open(fname)
count = 0

for line in fhand:
    if not line.startswith('From:'):continue
    words=line.split()
    count=count+1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")
