#Forrest Gump plans on running across the USA.  In order to plan his journey, Forrest would like a program that can calculate how many days it will take him to run the total distance.

#Your program should ask the user how far they plan on running (in miles) and how fast the user can run (in miles per hour).

#Your program should display the number of days it will take Forrest run the distance.  Assume that Forrest can run at a constant pace for the entire distance with no breaks for rest, eating or sleeping.

#Public Test Cases
#Input: 240, 4
#Expected Output: It will take Forrest 2.5 days to run 240 miles if he runs at 4 miles per hour.

distance = int(input("How many miles in total: "))
speed = int(input("How fast are you are travelling: "))
time = distance/speed
no_days = time/24
no_days = str(no_days)
distance = str(distance)
speed = str(speed)
print("It will take Forrest "+ no_days + " days to run "+ distance +" miles if he runs at "+ speed +" miles per hour.")
