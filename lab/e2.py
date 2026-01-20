'''Enter Month name from user and display days accoudingly(match case).'''
month = input("Enter month: ") 
match month:
    case "january":
        print("31 days")
    case "february":
        print("28/29 days")
    case "march":
        print("31 days")
    case "april":
        print("30 days")
    case "may":
        print("31 days")
    case "june":
        print("30 days")
    case "july":
        print("31 days")
    case "august":
        print("31 days")
    case "september":
        print("30 days")
    case "october":
        print("31 days")
    case "november":
        print("30 days")
    case "december":
        print("31 days")
    case _:
        print("Invalid month")

'''Ask user about the start ,end and increment value and print accourdingly
start : 100
end : 500
increment : 5'''

start=int(input("enter your starting: "))
end=int(input("enter your ending number: "))
increment=int(input("enter your increment number: "))
for i in range(start,end,increment):
    print(i)