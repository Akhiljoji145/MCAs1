a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b and a>c:
    print(f"{a} is greatest")
    d=a
elif b>a and b>c:
    print(f"{b} is greatest")
    d=b
else:
    print(f"{c} is greatest")
    d=c
sum=d+d**2+d**3
print(sum)
print("area of a circle = ",2*3.14*d)
print("perimeter of a circle = ",3.14*d**2)
