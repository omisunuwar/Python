fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    #print(email)
    lst=list()
#for e in email:
    parts=email.split('@')
    domain=parts[1]
    #lst.append(domain)
    print(domain)
