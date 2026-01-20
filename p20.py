'''Print even numbers from give range without using % .'''
a=int(input("enter starting number: "))
b=int(input("enter ending number: "))
for i in range(a,b):
    if i//2*2==i:
        print(i)