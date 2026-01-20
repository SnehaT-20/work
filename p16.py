'''Print even numbers fall between 2 given numbers E.g user enter 10 20 
                                                    output 12,14,16,18'''
a=int(input("enter starting number: "))
b=int(input("enter ending number: "))
for i in range(a+1,b-1):
    if i%2==0:
        print(i)
    