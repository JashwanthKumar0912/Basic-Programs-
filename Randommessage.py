#Create a Python program that generates a random number between 1 and 5.  Depending on the number generated, display a random message.


# Getting a predefined function into the code 

import random
# Generating a random number 
number = random.randint(1,5)

# Using a if statement to compare and print random messages
if number == 1:
    print("Your Dumb ")
elif number == 2:
    print("I am cool")
elif number == 3:
    print("Smart choice!!!")
elif number == 4:
    print("Not bad")
else:
    print("Mr murry is so cool")
