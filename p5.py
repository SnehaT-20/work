'''Find Compond Interest. Amount = P(1 + R/100) t  Compound Interest = A - P'''
p=int(input("enter your principle amount: "))
t=int(input("enter your time period: "))
r=int(input("enter your rate of interest per year(%): "))
Amount = p*(1 + r/100)**t
print(f"your amount is: {Amount}")
compound_interest=Amount-p
print(f"your compound interest is = {compound_interest}")