#The computing club lets in members when they are over 14 years old and have completed the S2 Computing Course.

#You should make a program that asks the user if they would like to join the club.  If they say "yes", ask them for their age.  If they are over 14 years old, display a message that says "Welcome to Computing Club".  If they aren't old enough, say "You are too young.  Try again in the future".  If they didn't say "yes" to joining the club, say "Oh well, goodbye".


option = str(input("yes/no:"))
if (option ==  "yes"): 
    age_person = int(input("Enter your age :"))
    if (age_person > 14):
        print("Welcome to Computing Club")
    elif (age_person <= 14):
        print("You are too young. Try again in the future")
elif (option == "no"):
    print("Oh well, goodbye")
