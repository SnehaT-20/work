'''age = int(input("enter your age"))
if age>18:
    print("eligible for voting")
else:
    print("user  is minor")

'''
'''num = int(input("enter your number"))
if num>=0:
    print("number is positive")
else:
    print("num is negative")'''




age = int(input("enter your age"))
if age>=0 and age<2:
    print("infant")
elif age>=3 and age<18:
    print("minor")
elif age>=19 and age<50:
    print("adult")
elif age>=51 and age<70:
    print("senior")
elif age>=70:
    print("super senior")
else:
    print("age is invalid")