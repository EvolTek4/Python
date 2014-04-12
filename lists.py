myList = [];                                         #Create empty list
add = int(raw_input("How many names to add? "))      #Get how many names to add to list
for x in range(add):                                 #Loop until all names are added
    name = raw_input("Enter a name: ")               #Get name to add to list
    myList.append(name)                              #Add name to list
print "Your current list is:", myList                #Print list to screen
remove = int(raw_input("How many names to remove? "))#Get how many list items to remove
for y in range(remove):                              #Loop to remove number stated
    print myList.pop() + " was removed."             #Print item removed
print "Your current list is", myList                 #Print list to screen
raw_input("Press Enter to Exit")
