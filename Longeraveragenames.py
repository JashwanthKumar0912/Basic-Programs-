#Create a program that asks the user to enter 20 names then stores the names in an array.

#After the names have been entered, calculate the average length of a name.

#After calculating the average name length, loop through all names and display the names that are longer than average.


names = [] 
name_len = 0
length = 0
average = 0 
for i in range(20):
    name = str(input("Enter the name"))
    names.append(name)
for i in range(20):
    name_len = len(names[i])
    length = name_len +length 
average = length / 20
print("The following names are longer than average:")
for i in range(20):
    if len(names[i]) > average:
        print(names[i])
