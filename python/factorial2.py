from math import factorial
a=int(input("enter a number"))
print(f"factorial of a is :",factorial(a))
num=3
c,b=0,1
for _ in range(num):
    print(c,end=" ")
    c,b=b,c+b
list1=[1,2,3,4,5]
sum1=sum(list1)
print("\n",sum1)