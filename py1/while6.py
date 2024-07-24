first1=int(input("Enter a number:"))
second2=int(input("Enter another number:"))
if first1>second2:
    while first1>second2:    
        if second2%2==0:
            print(second2)
            second2=second2+1
else:
    while first1<second2:
        if first1%2==0:
            print(first1)
        first1=first1+1