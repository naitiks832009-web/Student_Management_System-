from data import students
from validation import get_age, get_marks
from display import display_student


#defining a function to add student details
def add_student():
    name = input("Enter Student Name: ")
    reg = input("Enter Student registration number: ")
    age = get_age()
    marks = get_marks()

    branch = input("Enter Student branch: ")
    student = {
        "Name":name,
        "Reg no.":reg,
        "age":age,
        "Marks":marks,
        "Branch":branch }
    students.append(student)
    print("Student added sucessfully")


#defining a function to view  all student details
def view_student():
    for student in students:
        display_student(student)


#defining a function to search student details by registration number or name
def search_student():
    Reg = input("ENTER REGISTRATION NUMBER OR NAME OF STUDENT ")
    for student in students:
        if Reg == student["Reg no."] or Reg == student["Name"]  :
            display_student(student)
            return
        
    print("student not found")

#defining a function to view update student details by registration number or name
def update_student():
    Reg = input("Enter registration number or name of student: ")

    for student in students:
        if Reg == student["Reg no."] or Reg == student["Name"]:

            display_student(student)
            print("What would you like to update?")

            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Marks")
            print("4. Update Branch")
            print("5. Exit")

            while True:
                try:
                    choice = int(input("Enter your choice (1-5): "))
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if choice == 1:
                    Newname = input("Enter new name: ")
                    student["Name"] = Newname
                    print("Student name updated")
                    break

                elif choice == 2:
                    
                    NEWAGE = get_age()
                    student["age"] = NEWAGE
                    print("Student age updated")
                    break

                elif choice == 3:
                    
                    newmarks = get_marks()

                    student["Marks"] = newmarks
                    print("Student marks updated")
                    break

                elif choice == 4:
                    Newbranch = input("Enter student branch: ")
                    student["Branch"] = Newbranch
                    print("Student branch updated")
                    break

                elif choice == 5:
                    print("Exiting update menu.")
                    return

                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

            return

    print("Student not found")


#defining a function to delete student details by registration number or name
def delete_student():
    Reg = input("Enter student registration number or name to delete: ")
    for student in students:
        if Reg == student["Reg no."] or Reg == student["Name"]: 
            display_student(student)

            confirm = input("Are you sure you want to delete this student? (yes/no): ")
            if confirm == "yes":
                students.remove(student)
                print("Student deleted successfully")
                return
            elif confirm == "no":
                print("Deletion cancelled")
                return
            else:
                print("please enter valid input")
                return

    print("Student not found")




    


