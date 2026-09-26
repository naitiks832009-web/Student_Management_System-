def get_age():
     while True:
        try:
            age = int(input("Enter Student age: "))
            if age > 0:
                return age
                
            else:
                print("Age must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")

def get_marks():
    while True:
        try:
            Marks = int(input("Enter student marks: "))
            if 0 <= Marks <= 100:
                return Marks
                
            else:
                print("Marks should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for marks.")

