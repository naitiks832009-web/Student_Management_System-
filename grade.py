from data import students
from display import display_student

def show_grade():
    reg = input("Enter registration number or name of student to show grade: ")
    for student in students:
        if reg == student["Reg no."] or reg == student["Name"]:
            display_student(student)

            if student["Marks"]>=90:
                print("Grade = A")           
            elif student["Marks"]>=80:
                print("Grade = B")
            elif student["Marks"]>=70:
                print("Grade = C")
            else:
                print("RESULT IS FAILED")
            return    
        
    print("Student not found")