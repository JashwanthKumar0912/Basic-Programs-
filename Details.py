# Write a program to get the user to input values and print the list

l=[]
no = int(input("How many types of values would you like to enter: "))
for i in range(no):
    value = input("Enter the value: ")
    l.append(value)
print(l)
