#Create a random number guess game

import random
guess = int(input("Type any number from 1 to 100: "))
random = random.randint(1,100)
while guess != random:
    if guess>random:
        print("It's smaller: ")
    else:
        print("It's larger: ")
    guess = int(input("Guess the numeber from 1-100: "))

print("Well Done!!!")
