'''print("1. addition","2.substraction","3.multiply","4.division","5.exit")
choice=int(input("enter your operation choice"))
match choice:
    case 1:'''


'''lst_city=['rajkot','ahemdabad','dwarka']
for i in lst_city:'''

'''num=int(input("enter your number"))'''
'''for num in range(3,101):
   temp=1
   for i in range(2,num):
    if num%i==0:
        temp=1
        print("not a prime")
        break
    else:
        temp=0
if temp==0:
    print("num is prime")'''

'''count total number of prime number nad not a prime number'''

'''num=int(input("enter your num"))
for i in range(num+1):
    #for j in range(i+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()'''
    
'''num=int(input("enter your num"))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()'''

'''num=int(input("enter your num"))
for i in range(num+1):
     for j in range(i):
        print(i, end=" ")
     print()'''

num=int(input("enter your num"))
k=1
for i in range(num):
     for j in range(i+1):
        print(k, end=" ")
     k+=2
     print()

 