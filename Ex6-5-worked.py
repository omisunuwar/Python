text = "X-DSPAM-Confidence:    0.8475";
atpos=text.find(':')
ntext=text[atpos+5:]
print(float(ntext))
