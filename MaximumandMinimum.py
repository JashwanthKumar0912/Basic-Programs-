#Write a program which gets a teacher to enter every students mark out of 20. You have to convert it to percentage store it into an array and find the minimum and maximum percentage.

percentage = 0
marks = []
no = int(input("Enter the number of students in your classroom: "))
for i in range(no):
    mark = int(input("Enter the mark of the students: "))
    percentage = (mark/20)*100
    marks.append(percentage)
print("The maximum score was:",max(marks))
print("The minimum score was:",min(marks))
