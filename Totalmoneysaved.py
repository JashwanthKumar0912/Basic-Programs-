#A program is required to calculate the total amount of money saved by the user.

#The program should ask for the number of weeks the user has been saving for, then ask for the amount saved in each week. The program should keep track of the running total and display this to the user at the end.


week = 0
saving =0
week_saving = 0
week = int(input("How many weeks have you been saving money: "))
for i in range(week):
    week_saving = float(input("How much money last week: "))
    saving = saving + week_saving
week = str(week)
saving = str(saving)
print("After "+ week + " weeks you have saved £" + saving + "!")
