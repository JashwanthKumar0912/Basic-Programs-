# Your program should ask the user how many people are in the room.  Ask each person what their height is in metres.  Calculate the average height in the room and display an appropriate message to the user.

people = int(input("How many people are in the room: "))
Average = str
total = 0
for i in range(people):
    height = float(input("Please enter the height in m:"))
    total = total + height
    Average = total/people
Average = str(Average)
print("The average height is "+ Average + " metres.")
