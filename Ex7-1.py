fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened")
    quit()
for line in fhand:
    line=line.rstrip()
    print(line.upper())
