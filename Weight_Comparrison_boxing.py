#A boxing tournament is taking place, and the organisers would like to use a program to keep track of who is below the weight limit of 63.5kg.

#Your program should ask for how many entrants there are.
#For each entrant, get their weight in kilograms and store it in an array.
#Loop through each weight in the array and display any weights that are less than or equal to the limit of 63.5.


Entrants = int(input("Enter the number of entrants:"))
Weights = []
for i in range (Entrants):
    Weight = float(input("Enter the weight in kg: "))
    Weights.append(Weight)
print("The following weights were allowed")
for i in range (Entrants):
    if Weights[i] <= 63.5:
        print(str(Weights[i])+"kg")

