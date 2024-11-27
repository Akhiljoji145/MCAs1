date=int(input("enter the date: "))
month=int(input("enter the month: "))
year=int(input("Enter the year: "))
print(f'{date}-{month}-{year}')
if year%4==0 and year%100!=0 or year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")