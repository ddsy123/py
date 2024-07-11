a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
if a<b and a<c:
    small=a
    if b<c:
        mid=b
        lg=c
    else:
        mid=c
        lg=b
elif b<a and b<c:
    small=b
    if a<c:
        mid=a
        lg=c
    else:
        mid=c
        lg=a
else:
    small=c
    if b<a:
        mid=b
        lg=a
    else:
        mid=a
        lg=b
print("Numbers in ascending order are:",small,mid,lg)
