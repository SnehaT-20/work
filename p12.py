'''Accept and print number until user enter 0 (use while)'''
num = int(input("Enter a number : "))
while num != 0:
    print(f"You number is : {num}")
    num = int(input("Enter a number : "))