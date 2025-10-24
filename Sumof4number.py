#Ask the user to enter 4 numbers.  Add them all together and show the answer.

total = 0 
for i in range(0,4):
    x = int(input("Enter a number:"))
    total = total + x 
total = str(total)
print("The total is "+total)
