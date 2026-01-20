''' control statement:
break- breake a loop based on the condition
continue- skip current iteration and execute the next iteration
pass- pass/nothing/placeholder'''

'''match case'''

day= int(input("enter your day(1-7)"))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid day")

        
'''enter month name from user and display days accordingly
if user enter janueary then answer has to enter 31 days'''