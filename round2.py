#Most places in the USA have a thing called sales tax.  This means that the price displayed in a shop isn't the price you pay, because shops don't include the sales tax.

#In Florida, sales tax is 6%.  Your job is to create a program that will take in the price of a product in dollars, then add sales tax at 6%, then round that number to 2 decimal places.

#Display the price that includes sales tax to the user.


price = float(input("Enter the price: "))
tot_price=price 
price = price*6/100
real_price=tot_price+price
real_price = round(real_price,2)
real_price = str(real_price)
print("$"+real_price)
