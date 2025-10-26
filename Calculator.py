#Using python create a calculator
Value = 0
print(" If you want to do addition write 'Sum' and If you want to do subtraction write 'Difference' If you want to do multiplication write 'Product' If you want to do division write 'Quotient'")
operation = input("Enter the operation you want to do: ")
a = int(input("Enter your 1st number"))
b = int(input("Enter your 2nd number"))
if (operation == 'Sum' or operation == 'sum'):
    Value = a+b
    print(Value)
elif (operation == 'Difference' or operation == 'difference'):
    Value = a-b
    print(Value)
elif (operation == 'Product' or operation == 'product'):
    Value = a*b
    print(Value)
elif (operation == 'Quotient' or operation == 'quotient'):
    Value = a/b
    Value = round(Value,2)
    print(Value)
else:
    print("Your Dumb")
