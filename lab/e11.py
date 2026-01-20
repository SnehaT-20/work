'''  Menu driven program 
1. Add Data of Student 
2. Search Student
3. delete Student
4. View all the student
5. Exit 

1. 
Please enter Email address : helly@gmail.com
Please enter name :Helly
Please enter age : 20
Please enter C_No : 22222
Please enter Marks : 120

2. Please enter email to search  : Harmi@gmail.com
		Student is not available

2 Please enter email to search : Helly@gmail.com
	Helly
	20
	22222
	120'''
student_data ={
    "sneha@gmail.com":["Sneha",22,2345678,100],
    "mona@gmail.com":["Mona",28,455756,70],
    "mohnish@yahoo.com":["Mohnish",30,454354,90],
    "nitin@gmail.com":['Nitin',31,345345,90]
   }
while True:
    print("========== STUDENT MENU ==========")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Add the data of student")
            email=input("Enter student email")
            name=input("Enter student name")
            age=int(input("Enter student age"))
            c_no=int(input("Enter student contact number"))
            marks=int(input("Enter student marks"))
            student_data[email]=[name,age,c_no,marks]
           # student_data.update({[email]:[name,age,c_no,marks]})
            print("Student is successfully added")
            
        case 2:
            print("Search student")
            search=input("Please enter email ")
            for i,j in student_data.items():
                if search==i:
                    for i1 in j:
                        print(i1)
                    break
            else:
                print(f"{search} not found in student data")

        case 3:
            print(" a student")
            email=input("Please enter email ")
            if email in student_data:
                  # del student_data[email]
                  student_data.pop(email)
            print("delete successfully")
                
        case 4:
            print("View all the Student")
            for i,j in student_data.items():
                print(i)
                for i1 in j:
                    print("\t",i1)

        case 5:
            print("I hope you got your info")
            break
        case _:
            print("Invalid choice")