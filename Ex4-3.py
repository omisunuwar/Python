hrs=input('Enter hours:')
rate=input('Enter rate:')
fh=float(hrs)
fr=float(rate)
def computepay(a,b):
    pay=((fh-40.0)*1.5+40)*fr
    return pay
p=computepay(fh,fr)
print('Pay:',p)
