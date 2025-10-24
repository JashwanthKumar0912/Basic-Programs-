#Your program should ask the user for how much money they have.

#If they have 6.95 or more, tell them they can buy the Super Meal Deal.
#If they don't have at least 6.95 but they do have 4.45 or more, tell them they can buy the Regular Meal Deal.
#Otherwise, tell them they don't have enough money for any meal deals.

#Public Test Cases
#Input	Expected Output
#9.23	You can buy the Super Meal Deal
#5.13	You can buy the Regular Meal Deal
#1.63	You don't have enough money for any meal deals

amount = float(input("Enter your cash"))
if amount >= 6.95:
    print("You can buy the Super Meal Deal")
elif amount >= 4.45 and amount < 6.95:
    print("You can buy the Regular Meal Deal")
else:
    print("You don't have enough money for any meal deals")
