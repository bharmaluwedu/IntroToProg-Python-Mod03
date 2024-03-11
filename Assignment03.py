import csv
import sys

"""
 ------------------------------------------------------------------------------------------ #
 Title: Assignment03
 Desc: This assignment demonstrates using conditional logic and looping
 Change Log: Mohammad Ammar Bharmal, 02/11/2024, Created Script
 ------------------------------------------------------------------------------------------ #
"""

print("""
     Welcome to Assignment 03: Course Registration Program!
        This program demonstrates the use of while loop,
           programming menus, conditional logic, and
                using the PyCharm IDE in Python
      """
      )

# Define the Data
# defining data constant with datatype so that the constant value does not change throughout the program
MENU: str
MENU = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
"""


# Define the Data Variables
# defining data constant with datatype and setting it as empty string
student_first_name: str
student_last_name: str
csv_data: str
course_name: str
menu_choice: str

# defining data constant with datatype and setting it with the csv file name
FILE_NAME: str
FILE_NAME = "Enrollments.csv"  # assigning value to the constant

# assigning None to the constant
file_obj = None
coma = None

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("Enter a menu option (1-4): ")

    match menu_choice:
        case "1":
            # Input user data
            student_first_name = input("Enter student's first name: ")
            student_last_name = input("Enter student's last name: ")
            course_name = input("Enter the course name: ")

        case "2":
            # Present the current data
            csv_data = f"{student_first_name},{student_last_name},{course_name}"
            print("The current data is:\n", csv_data)

        case "3":
            # Save the data to a file
            with open(FILE_NAME, "w") as file_obj:
                file_obj.write("First name,Last name,Course Name\n")
                file_obj.write(csv_data)
            with open(FILE_NAME, "r") as coma:
                targetReader = csv.reader(coma, delimiter=',')
                for row in targetReader:
                    print(row)

        case "4":
            # Stop the loop
            print("Ending Program")
            sys.exit(0)

        case _:
            print("Invalid choice")