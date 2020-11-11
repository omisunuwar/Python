s=input('Enter score between 0.0 and 1.0')
try:
    fs=float(s)
except:
    print('Error: cannot convert str to float')
if(fs>1.0):
   print('Score out of range')
elif(fs>=0.9):
   print('A')
elif(fs>=0.8):
   print('B')
elif(fs>=0.7):
   print('C')
elif(fs>=0.6):
   print('D')
elif(fs<0.6):
   print('F')
#elif(fs<0):
#    print("Error: Score out of range")
#print("Error: Score out of range")
#print("All done")
