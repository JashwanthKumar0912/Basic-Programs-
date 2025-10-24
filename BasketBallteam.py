#The basketball coach wants to create a team of very tall people, but doesn't know if enough people in the PE class are tall enough to make a team.

#You must create a program that asks the user how many people want to join the team.  For each person, ask for their height in centimeters.  If they are over 185cm, they can join the team.  Keep track of how many people are tall enough to join the team.

#If there are 5 or more people who are over 185cm, display a message saying "You can make a team!".

#Otherwise, say "There aren't enough tall people to make a team."



heights = [] 
people = int(input("Enter the number of people wants to join this team: "))
for i in range(people):
  height = int(input("Enter the height in cm: "))
  if(height > 185):
    heights.append(height)
if len(heights) >= 5:
  print("You can make a team! ")
else: 
  print("There aren't enough tall people to make a team.")
  
