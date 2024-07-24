bill=int(input("Enter electricity used in units:"))
print("Units used are:",bill)
cost=0
if bill>0 and bill<=100:
    print("Bill is 0")
elif bill>100 and bill<=200:
    cost=(bill-100)*5
    print("Bill is:",cost)
else:
    cost=(100*5)+(bill-200)*10
    print("Bill is:",cost)
