#file is romeo.txt

fname = input("Enter file name: ")
try:
    fhand = open(fname)
    #break --gives break outside of loop error
except:
    print('Cannot open file')
    quit()
wordlist = list()
after=None
initial=None
for line in fhand:
    #print(line.rstrip())
    word=line.split()
    #print(word)
    for w in word:
        if initial is None:
            initial=w
            wordlist.append(initial)
        elif w==initial: continue
        else:
            initial=w
            wordlist.append(initial)
        wordlist.sort()
    #sorts all the w(words) in word

i=0
lst=list()
for i in range(len(wordlist)):
    if after is None:
        after=wordlist[i]
        lst.append(after)
    elif wordlist[i]==after: continue
    else:
        after=wordlist[i]
        lst.append(after)
print(lst)
