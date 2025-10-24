#You must create a program that will calculate the volume of a cuboid.

#Get the width, height and length of the cuboid.  Each dimension must be between 1 and 100.  If the user enters a number outwith this range, ask them to try again.

#Display the volume of the cuboid once calculated.

Volume = 0

length = int(input("Enter the length: "))
while(length < 1 or length > 100):
    print("Try again.")
    length = int(input("Enter the length: "))

width = int(input("Enter the width: "))
while(width < 1 or width > 100):
    print("Try again.")
    width = int(input("Enter the width: "))

height = int(input("Enter the height: "))
while(height < 1 or height > 100):
    print("Try again.")
    height = int(input("Enter the width: "))

Volume = length * width * height
Volume = str(Volume)
print("The volume is " +Volume+ ".")

