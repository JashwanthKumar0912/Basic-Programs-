#Your program should ask the user how many people are in the class.

#For each person, ask them if they would like to join the school band, The Black Parade.

#Keep track of how many people say "yes" and "no" and display the total to the user at the end.

count = 0
count_2 = 0
no_people = int(input("Enter the number of people in class: "))
for i in range(no_people):
    number = str(input("Enter yes or no"))
    if number == "Yes" or number == "yes":
        count = count + 1
    elif number == "No" or number == "no":
        count_2 = count_2 + 1
count_2 = str(count_2)         
count = str(count)   
print(count+" people want to join The Black Parade. "+ count_2+ " people do not want to join The Black Parade.")
