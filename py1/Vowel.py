ch=input("Enter a character to check vowel or consonant:")
ch=ch.lower()
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("Vowel")
elif ch=='1' or ch=='2' or ch=='3' or ch=='4' or ch=='5' or ch=='6' or ch=='7' or ch=='8' or ch=='9' or ch=='0':
    print("Enter an alphabet")
else:
    print("Consonant")