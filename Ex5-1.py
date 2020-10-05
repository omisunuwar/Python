largest=None
smallest=None
while True:
    num=input('Enter a number: ')
    if(num=='done'):
        break
    try:
        fnum=float(num)
    except:
        print('Invalid Input')
        continue
    if largest is None:
        largest=fnum
    if smallest is None:
        smallest=fnum
    if(fnum>largest):
        largest=fnum
    if(fnum<smallest):
        smallest=fnum
    print(fnum,largest,smallest)
print('Maximum is',int(largest))
print('Minimum is',int(smallest))
