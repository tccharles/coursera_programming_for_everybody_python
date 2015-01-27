fname = raw_input("Enter file name: ")
try:
	fh = open(fname, 'r')
except:
	print 'No such file. File cannot be opened:', fname
	exit()

count = 0

for line in fh:
	line = line.rstrip()
	if not line.startswith('From '):
		continue
	words = line.split()
	count = count + 1
	print words[1]
print "There were", count, "lines in the file with From as the first word"
