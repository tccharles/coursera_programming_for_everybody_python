fname = raw_input("Enter file name: ")
try:
	fh = open(fname, 'r')
except:
	print 'No such file. File cannot be opened:', fname
	exit()

mylist = list()

for line in fh:
	line.strip()
	words = line.split()
	for word in words:
		if word not in mylist:
		    mylist.append(word)
	mylist.sort()
print mylist
