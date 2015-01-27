fname = raw_input("Enter file name: ")
try:
	fh = open(fname, 'r')
except:
	print 'No such file. File cannot be opened:', fname
	exit()
count = 0
total = 0

for line in fh:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	else:
		colpos = line.find(':')
		value = float(line[colpos+1:].strip())
		total = total + value

		count = count + 1
	average = total / count

print 'Average spam confidence:', average
