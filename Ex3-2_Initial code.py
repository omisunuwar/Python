hrs=input('Enter hours:')
rate=input('Enter rate:')
if(float(hrs)<40.0):
 print(float(hrs)*float(rate))
else:
 try:
  print(40*rate+(float(hrs)-40.0)*float(rate)*1.5)
 except:
     ival=-1
if(ival==-1):
 print('Error')
#print(ival)
print('All done')
