'''Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, 
print an error. If the score is between 0.0 and 1.0, print a grade using the following table:'''

input = raw_input("Enter a Score between 0.0 and 1.0:")
score = float(input)

if score <= 0.0 or score >= 1.0:
	print "You are out of range."
elif score >= 0.9:
	print 'A'
elif score >= 0.8:
	print 'B'
elif score >= 0.7:
	print 'C'
elif score >= 0.6:
	print 'D'						
elif score < 0.6:
	print 'F'
