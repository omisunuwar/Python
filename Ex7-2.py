# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Cannot open file')
    quit()
count=0.0
tot=None
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        count=count+1
        atpos=line.find(':')
        nline=line[atpos+2:]
        fline=float(nline)
        #print(fline)
        if tot is None:
            tot=fline
        else:
            tot=tot+fline
    
print('Average spam confidence:',tot/count)

