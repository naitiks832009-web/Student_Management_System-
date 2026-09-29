# Student managment system 

## project overview 
This is an  Python project that can be used to manage student records from the terminal.
the program allow user to add student , view student , search student , update student and delete student , it can also show the grade of a student according to their marks 
the program is divided into some different files in the each file have their own responsibilty 

## Features 
Add a new student 
View all student 
Search student by their name or registration number 
Update student informatioin 
Delete student record 
Show student Grade 
Validate age and marks 
Handle invalid input 

## Technologies Used
python 3 
python list and dictionaries
command line interface 
git and github 

## Requirements 
The project requires :
python 3.x
A terminal or a command prompt 

No external python libraries are required . 

## Setup

### Check Python Installation

Open a terminal and run:

```bash
python --version
```


2. clone the repository 
    git clone https://github.com/naitiks832009-web/Student_Management_System-
    


## Configuration

No additional configuration is required to run the project. 

## How to run 
open the terminal inside the project folder  and run :
python main.py

AFTER running this program menu of student managment system display 

## Main operation 
### 1 Add student 
The user can add a new student by entering this information -
Name of the student 
Reg no. 
age 
marks 
branch 

### View all student 
This option display all the student information that is stored in program 

### Search student 
user can search student by entering their name or registration number 
if matching is found , the program display the details of the student 

### Update student 
The user can update these information about the student 
Student name 
student age 
student marks 
student Branch 

### Delete student 
the user can delete a student by entering their name or registration number 

### Show grade 
user can show the grade of the student according to the marks of the student according to their marks by entering their name or registration no. 


## Input validation 
The project validate the student age and marks before storing or updating 

### Age validation 
The age must be a positive integer 
if a invaild input given the program will ask again to enter the age again 

### marks validation 
the marks will be in range Greater  or equal to  0 and less or equal to 100
if a invaild input given the program will ask again to enter the marks  again

The program also handles invalid  input, such as entering text instead of a number

## Grade system 
This program follow a grade system based on their marks and decide his grade 

The condition for grade system is - 
if student marks  90 to 100 than the grade is "A" 
if student marks  80  to 89 than the grade is "B"
if student marks  70 to 79 than the grade is "C"
if student marks  Below 70 than the program display student is failed 

## Testing

The project was manually tested through the command line.

The following operations were tested:

Adding a student with valid information
Entering invalid age values
Entering invalid marks
Viewing all students
Searching by student name
Searching by registration number
Searching for a student that does not exist
Updating student name
Updating student age
Updating student marks
Updating student branch
Entering an invalid update choice
Deleting a student
Cancelling a deletion
Showing student grades
Entering invalid main menu choices
Exiting the program

## Project Structure

```text
Student_Management_System/
│
├── main.py
├── data.py
├── operations.py
├── validation.py
├── display.py
├── grade.py
├── README.md
└── statement.md
```



## Data storage

Student records are stored in data.py using a Python list containing dictionaries.

The project does not currently use a database.

The data is available while the program is running. Changes made during execution are not permanently stored after the program is closed.

## Limitations

The current version of the project has some limitations:

Student records are not permanently stored
The project does not use a database
There is no graphical user interface
Student search currently requires the exact name or registration number
The project runs through the command line

## Future Improvements

Some possible improvements for the future are:

Store student records permanently using a database or file.
Add duplicate registration number checking.
Make student search case-insensitive.
Add more student information.
Add a graphical user interface.
Add more detailed student reports.
