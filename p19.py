'''Write a program to display numbers which are divisible by 13 from given range.'''
a=int(input("enter starting number: "))
b=int(input("enter ending number: "))
for i in range(a,b):
    if i%13==0:
        print(i)
    