text = "X-DSPAM-Confidence:    0.8475";
colpos = text.find(':')

number = text[colpos+1:].strip()
print float(number)

'''
line 1: creates a string called X-DSPAM-Confidence:    0.8475
line 2: find the colon in the string from line 1
line 3: extract everything to the right of the colon
line 4: convert it to a float
line 5: print line 4
'''

'''
num = x[pos+1:].strip()
print float(num)
'''
