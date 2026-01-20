'''Print no of digits and letters in String.Accept String from user. E.g string="H1Visa" Digits = 1 and letters=5'''
username= input("Enter a string: ")
letters = 0
digits = 0
for char in username:
    if char.isalpha(): 
        letters += 1
    elif char.isdigit(): 
        digits += 1
print("Letters =", letters)
print("Digits =", digits)