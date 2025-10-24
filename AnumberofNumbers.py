#Ask the user for how many numbers they want to add.

#Allow the user to enter each of the numbers, adding them all up as you go.

#Display the total to the user.


total = 0 
number = int(input("Enter how many number would you like to add: "))
for i in range(number):
    x = int(input("Enter a number:"))
    total = total + x 
print(total)
