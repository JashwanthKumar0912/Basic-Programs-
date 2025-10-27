#Write a program to ask the user for 2 numbers and ask if they want it swapped or not if they say "Yes" then swap it. If they say "No" do swap it and print Sure, great choice.


temp =0
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
x = str(x)
y = str(y)
print("This is your first number: " + x + " This is your second number: " +y)

val = input("Would you like to swap your numbers? Yes/No: ")
if val == "Yes" or val == "yes":
    x = int(x)
    y = int(y)
    temp = x
    x = y
    y = temp

    x= str(x)
    y= str(y)
    print("This is your first swapped number: "+x+ " This is your second swapped number: " +y)
elif val == "No" or val == "no":
    print("Sure, great choice")
    print("This is your first number: " + x + " This is your second number: " +y)   

else:
    print("Sure, great choice") 
    print("This is your first number: " + x + " This is your second number: " +y)  
