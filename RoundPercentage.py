#The Computing Science exam is out of 80 marks.  Ask the user how many marks they achieved, then calculate their percentage.

#Round the percentage to a whole number and display the rounded percentage to the user.


Mark = int(input("Enter your mark out of 80:"))
total = 80 
Marks = Mark/80*100
total = Marks
total = round(total)
total = str(total)
print("You got " + total + "%")

