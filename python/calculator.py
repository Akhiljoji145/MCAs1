a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
choice=int(input("enter a choice"))
match choice:
    case 1:
        c=a+b
        print("Sum=",c)
    case 2:
        c=a-b
        print("difference=",c)
    case 3:
        c=a*b
        print("product=",c)
    case 4:
        c=a/b
        print("quotient=",c)
    case 5:
        c=a%b
        print("remainder=",c)
    case _:
        print("invalid input")
