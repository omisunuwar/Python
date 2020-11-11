text = "X-DSPAM-Confidence:    0.8475";
atpos=text.find(':')
spos=text.find('5',atpos)+1
#tab is 4 spaces hence atpos+5
ntxt=text[atpos+5:spos]
print(float(ntxt))
#itxt=int(ntxt)
#print(float(ntxt))
