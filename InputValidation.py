#Ask the user for a number between 1 and 10 (inclusive).  If they enter a number that is outwith that range, display a message asking them to try again.  When they finally enter a valid number, display "Well done".

number = int(input("Enter a number"))
while number < 1 or number > 10:
    print("Try again")
    number = int(input("Enter a number"))

print("Well done") 
