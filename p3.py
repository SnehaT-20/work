'''Find maximum number using ternary operator.'''
a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = int(input("enter your third number: "))
maximum = a if (a > b and a > c) else (b if b > c else c)
print(f"Maximum number is: {maximum}")
