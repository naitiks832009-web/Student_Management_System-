# Student management system

## Problem Statement
This is an  Python project that can be used to manage student records from the terminal.

If  a managment want to mange student information  manually, it can become difficult to find a particular student or make changes to their details. This project provides basic operations such as adding, viewing, searching, updating and deleting student records.

The project also checks the age and marks entered by the user so that invalid values are not stored.

## Scope of the project
This project is mainly focused on student record managment using python 

The user can do this things :
Add a new student 
view all student
search for a particular student by their name or registration number 
update the student information by their name or registration number 
delete the student information if that is not required
check the grade of the student according to their marks 

The project is a  command-line application. Student records are stored using Python data structures while the program is running. There is currently no database or graphical user interface.

## Target users 

This project mainly target -
person who is learning  and for beginner in python
for teacher or for managment system who want an example of student managment system .
and also for for Anyone who wants to practice basic record management using the command line.

## High level feature 

### 1 Add student
The user can add a student by entering :
Name of the student 
Registration number 
Age 
Marks
Branch 

all this information is added to the students list 

### 2 View all students 
This option display all the student information that is stored in the program 
The information is about student cover his name , reg.no, age , marks and branch 

### 3 Search student 
The user can search a student by entering either his reg no. or his name 
if the matching student is found program will display his information , if does not match then the program show student not found 

### 4 Update student
The user can update a student information like -
User can update student name 
User can update student age
User can update student Marks 
User can update student branch 

there is also a option to go back to the main menu if the user does not want to update detail fron here 
Age and marks are checked using the validation functions before they are updated for making the program error free 

### Delete student 
The user can delete a student by entering their name or reg no. 
first it will display the information of the student than ask for the confirmation of you are sure or not to delete if the program get the answer   yes than it will delete the student  if answer came no than it will came backto the main menu without deleting the student details 

### Show grade 
The user can show the grade of student according to their marks , by entering  their name or reg no. 

the current grading system is lznike this - 
if student marks  90 to 100 than the grade is "A" 
if student marks  80  to 89 than the grade is "B"
if student marks  70 to 79 than the grade is "C"
if student marks  Below 70 than the program display student is failed 

### Input validation 
The project contain seprate function of validation for age and marks 
for age , program will accept only positive integer 
for marks , program wil accept integer in range of 0 to 100 

if the user input wrong value than the program ask the user again to enter the correct value instead of storing wrong values 

## Project module 

I divided the project into some different python file  and in this each file have their own responsibilty 

main.py - contain the menu and the control of the program 
data.py - contain the data of students 
operations.py - contain function for adding , viewing , searching , updating and deleting students 
display.py - contain the function use to display student detail
validation.py - contain function for validating age and marks 
grade.py - contain a function that will calculate the grade of a student 


THIS IS THE WHOLE STRUCTURE OF THIS PROGRAM . 
