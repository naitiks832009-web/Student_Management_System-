from operations import add_student, search_student,update_student,delete_student,view_student
from grade import show_grade 

def main():
    while True:
        print("==============================")
        print("  STUDENT MANAGEMENT SYSTEM  ")
        print("==============================")


        print("1 ADD STUDENT ")           
        print("2 VIEW ALL STUDENT ")           
        print("3 SEARCH STUDENT ")           
        print("4 UPDATE STUDENT ")           
        print("5 DELETE STUDENT ")           
        print("6 SHOW GRADE  ")
        print("7 EXIT ") 

        try:
            choose = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


        if choose == 1:
            add_student() 
        elif choose == 2:
            view_student()
        elif choose == 3:
            search_student()
        elif choose == 4:
            update_student()
        elif choose == 5:
            delete_student()
        elif choose == 6:
            show_grade()
        elif choose == 7:
            print("Exiting...")
            print("Thank you for using the Student Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

main()            