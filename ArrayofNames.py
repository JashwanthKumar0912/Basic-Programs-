#Create a program that asks the user to enter 5 names.

#The program should store the names in an array.

#A fixed loop should be used to display an appropriate message for each name in the array.

Names = []
count = 0
for i in range (5):
    name = str(input("Enter the names"))
    Names.append(name)
    

for i in range (5):
    count = count+1
    print("Person " +str(count)+ " is called "+Names[i]+".")
