#function without parameter

def greet():
    print("have good day")
greet()

# function with parameter

def greet(name):
    print("have a good day", name)
greet("sneha")

# function with 2 parameter + return value
def add(no1,no2):
    return no1+no2
ans=add(20,24)
print(f"sum is {ans}")