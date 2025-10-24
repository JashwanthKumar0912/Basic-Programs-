#The Programming club is open to any student who is aged between 14 and 17 (inclusive).

#Your program should ask for the user's age.  If they are under 14 or over 17, tell them they cannot join the club.

#Otherwise, tell them they are welcome to join the club.

#Public Test Cases
#Input	Expected Output
#15	You are welcome to join Programming club
#11	Sorry, you must be between 14 and 17 to join Programming club


age = 0
age = int(input("Enter your age: "))
if age >=14 and age <= 17:
  print("You are welcome to join Programming club")
else:
  print("Sorry, you must be between 14 and 17 to join Programming club")
