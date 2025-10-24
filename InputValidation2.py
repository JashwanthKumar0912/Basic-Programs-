#Input validation
#Only three lines of code are required for an input validation algorithm:


#num = int(input("Enter a number between 1 and 10: "))
#while num < 1 or num > 10:
#    num = int(input("Try again, it must be between 1 and 10: "))



#Using this structure, create a program that asks the user for the marks they achieved in their end of topic test.  The test was out of 40, so validate the input to be between 0 and 40.

#Calculate the percentage and display this to the user.



percentage = 0
marks = int(input("Enter the marks you achieved in the End of unit test: "))
while marks < 0 or marks > 40: 
  marks = int(input("Try again, it must be between 0 and 40: "))
percentage = marks / 40 * 100#
percentage = str(percentage)
print(percentage+ "%" )
