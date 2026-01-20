'''Food Menu - (Menu driven program)'''
while True:
    print("========== FOOD MENU ==========")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Pizza selected - Rs.150")
        case 2:
            print("Burger selected - Rs.100")
        case 3:
            print("Sandwich selected - Rs.80")
        case 4:
            print("Fries selected - Rs.70")
        case 5:
            print("Thank you!")
            break
        case _:
            print("Invalid choice")