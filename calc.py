x= int(input("Enter a number:"))
operation= input("Enter an operation (+, -, * or /)")
y= int(input ("Enter another number:"))

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x-y)
elif operation== "*":
    print(x*y)
elif operation == "/":
    print(x/y)
else:
    print("Sorry, operation not recognized!")