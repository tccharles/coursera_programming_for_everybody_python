largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done": break
    if len(num) < 1: break #Check for empty line
    #print num

    try:
        num = int(num)
    except:
        print "Invalid input"
        continue


    if largest is None or num > largest:
    	largest = num
    if smallest is None or num < smallest:
    	smallest = num

print "Maximum is ", largest
print "Minimum is ", smallest
