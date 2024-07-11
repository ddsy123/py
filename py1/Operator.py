a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
print("Enter operator +,*,-,/: ")
c=(input('Enter operator:'))
if c=='-':
    d=a-b
    print(d)
elif c=='+':
    d=a+b
    print(d)
elif c=='*':
    d=a*b
else:
    d=a/b
    print(d)