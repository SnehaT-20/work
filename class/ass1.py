dr_dict={"dr. harmi" : {"10am":0,"11am":0},"dr. disha" : {"2pm":0,"3pm":0,"4pm":0}}
while True:
    
    print("--- Clinic Appointment System ---")
    print("1. Book Appointment")
    print("2. View Appointment")
    print("3. Cancel Appointment")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            name = input("Enter patient name: ")
            age = input("Enter age: ")
            mobile = input("Enter mobile number: ")
            print(dr_dict.keys(),end=" ")
            doctor = input("Enter preferred doctor name: ")

            print("Available Time Slots:")
            print(dr_dict[doctor],end=" ")
            sel_slot=input("enter select slot: ")
            print(f"current slot {dr_dict[doctor]}")

            print(f"{name} appointment is booked with {doctor} at {sel_slot}")

            dr_dict[doctor][sel_slot]+=1

            print(f"after booking slot {dr_dict[doctor]}")
        
        case 4:
            print("Thank you for using the system.")
            break

        case _ :
             print("Invalid choice! Please try again.")


       


 



