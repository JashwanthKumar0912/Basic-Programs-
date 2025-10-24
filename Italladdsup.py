#A program is required to get numbers from the user until the total is over 100.

#The program should make use of a while loop.


total = 0
while total <= 100:
    number = int(input("Enter a number: "))
    total  = total + number
total = str(total)
print("Your total is " + total)
