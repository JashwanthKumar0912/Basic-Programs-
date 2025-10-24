#The city is building a new bridge and has asked a number of local school pupils to come up with a new name for the bridge.

#Using an array, store the suggestions that will be entered by 10 pupils.

#Once all suggestions have been entered, traverse the array and count how many of the names were more than 10 characters in length.

#Display the number of bridge names that were more than 10 characters in length to the user.


bridges = []
count = 0 
for i in range(10):
    name = str(input("Enter the name of the bridge: "))
    bridges.append(name)
for i in range(10):
    if len(bridges[i]) > 10:
        count = count + 1
count = str(count)
print("There are " + count + " suggestions with more than 10 characters.")
    
