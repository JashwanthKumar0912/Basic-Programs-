#Ask user for height in cm.

#If height is 195 or more, say "You're very tall!"

#Otherwise say "Thanks!"

height  = int(input("Enter your height in cm: "))
if height >= 195:
    print("You\'re very tall!")
elif height < 195:
    print("Thanks!")
