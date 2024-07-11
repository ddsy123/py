year=int(input("Enter a year to check leap year:"))
if year%4==0 and year%400==0:
    print("Leap Year")
else:
    print("Not a Leap Year")