# Alexis Gomez
# M02 Lab
# This program will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll

while True:
    # Ask for and accept a student's last name
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    
    # Check if the last name is 'ZZZ' to quit processing student records
    if last_name == 'ZZZ':
        break
    
    # Ask for and accept the student's first name
    first_name = input("Enter the student's first name: ")
    
    # Ask for and accept the student's GPA as a float
    gpa = float(input("Enter the student's GPA: "))
    
    # Test if the student's GPA is 3.5 or greater and print a message for Dean's List eligibility
    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")
    
    # Test if the student's GPA is 3.25 or greater and print a message for Honor Roll eligibility
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")

    # Test if the studen't GPA is less than 3.25 and print a message
    elif gpa < 3.25:
        print(first_name, last_name, "has not made the Honor Roll or Dean's List.")