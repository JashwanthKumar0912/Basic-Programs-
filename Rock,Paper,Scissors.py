''' Create a program to show a
Rock Paper and scissors game'''

import random
user = input("Enter an option Rock, Paper, or Scissors ")
options = ["Rock","Paper","Scissors"]
computer = random.choice(options)
print("You chose "+ user + " and the computer chose "+ computer)

while user == computer:
    print("It's a tie ")
    print("Try again!!")
    user = input("Enter an option Rock, Paper, or Scissors ")
    print("You chose "+ user + " and the computer chose "+ computer)
if user == "Rock":
    if computer == "Paper":
        print("You lose")
    elif computer == "Scissors":
        print("You win!!")

elif user == "Paper":
    if computer == "Scissors":
        print("You lose")
    elif computer == "Rock":
        print("You win!!")

elif user == "Scissors":
    if computer == "Rock":
        print("You lose")
    elif computer == "Paper":
        print("You win!!")

