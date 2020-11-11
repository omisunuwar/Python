hrs=input('Enter hours:')
rate=input('Enter rate:')
#try block for input in string, can't change to float if input in str
ival=2
try:
    fh=float(hrs)
    fr=float(rate)
except:
    ival=-1
    print('Error',ival)
    quit()

if (ival>0):
    pay=((float(hrs)-40.0)*1.5+40)*float(rate)
    print(pay)
#print('All done')
