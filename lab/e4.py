'''Count total_no of prime and not prime numbers in 1-100'''
for num in range(3,101):
    temp=1
    for i in range(2,num):
        if num%i ==0:
            temp=1
            print(f"{num} is not prime")
            break
        else:
            temp=0
    if temp==0:
        print(f"{num} is prime")




'''
1
1 2
1 2 3
1 2 3 4'''
num=int(input("enter your num"))
for i in range(num+1):
    #for j in range(i+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

 
'''
1 2 3 4
1 2 3
1 2
1'''
num=int(input("enter your num"))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

 
'''
1
2 2 
3 3 3
4 4 4 4'''
num=int(input("enter your num"))
for i in range(num+1):
     for j in range(i):
        print(i, end=" ")
     print()

 
'''
1 
3 3
5 5 5
7 7 7 7
9 9 9 9 9'''
num=int(input("enter your num"))
k=1
for i in range(num):
     for j in range(i+1):
        print(k, end=" ")
     k+=2
     print()



 