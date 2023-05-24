"""Python app that tracks students' grades
Usage:
    main.py
"""
# Python3
import re


def student_check(data):
    """checks if student credentials are correct

    Args:
        data (str): provided student credentials

    Returns:
        str, bool: returns student credentials if they are correct, otherwise returns False
    """
    if data == "":
        print("Incorrect credentials")
        return False
    double_symbol_name = False
    double_symbol_surname = False
    name_regex = r"^[A-Za-z][A-Za-z\-\']*[A-Za-z]$"
    surname_regex = r"^[A-Za-z][A-Za-z\-\']*[A-Za-z]$"
    email_regex = r"[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*"
    name = data.split()[0]
    surname = data.split()[1:-1]
    email = data.split()[-1]
    for index, letter in enumerate(name):
        if letter in ["-", "'"]:
            if name[index - 1] in ["-", "'"]:
                double_symbol_name = True
    for last_name in surname:
        for index, letter in enumerate(last_name):
            if letter in ["-", "'"]:
                if index == 0:
                    print("Incorrect last name")
                    return False
                if last_name[index - 1] in ["-", "'"]:
                    double_symbol_surname = True
    if len(data.split()) < 3:
        print("Incorrect credentials")
        return False
    if not re.match(name_regex, name) or double_symbol_name:
        print("Incorrect first name")
        return False
    if not all(re.match(surname_regex, s) for s in surname) or double_symbol_surname:
        print("Incorrect last name")
        return False
    if not re.match(email_regex, email):
        print("Incorrect email")
        return False
    return name, surname, email


def student_add(students, new_id = 10000):
    """takes user input for student credentials and adds them to students dictionary

    Args:
        students (dict): students dictionary
        new_id (int, optional): id of the new student. Defaults to 10000.

    Returns:
        int, dict: returns count of added students and updated students dictionary
    """
    if students:
        new_id = int(students[-1]["id"]) + 1
    count = 0
    updated_students = students
    print("Enter student credentials or 'back' to return:")
    user_input = input().strip()
    while user_input != "back":
        student = student_check(user_input)
        if student:
            if email_check(student[2], students):
                updated_students.append(
                    {"name": student[0], "surname": student[1],
                     "email": student[2], "id": new_id,
                     "py": 0, "dsa": 0 , "db": 0, "fl": 0} 
                )
            print("Student has been added.")
            count += 1
        user_input = input().strip()
    return count, updated_students


def grade_add(students):
    """takes user input for grade and adds it to student

    Args:
        students (dict): students dictionary
        
    Returns:
        dict: updated students dictionary
    """
    print("Enter an id and points or 'back' to return:")
    user_input = input().strip().split()
    student = id_check(user_input[0], students)
    if student:
        if len(user_input) == 5 and all(point < 0 for point in user_input[1:]):
            students[student]["py"] += int(user_input[1])
            students[student]["dsa"] += int(user_input[2])
            students[student]["db"] += int(user_input[3])
            students[student]["fl"] += int(user_input[4])
            print("Grade has been added.")
        else:
            print("Incorrect input")
    return students



def command_list(command):
    """takes user input and executes command if it exists

    Args:
        command (str): user input
    """
    students = {}
    while True:
        if command == "exit":
            print("Bye!")
            return
        if not command:
            print("No input")
        elif command == "add students":
            count, students = student_add(students)
            print(f"Total {count} students have been added.")
        elif command == "back":
            print("Enter 'exit' to exit the program")
        elif command == "list students":
            print("List of students:")
            for student in students:
                print(f"{student['name']} {student['surname']} {student['email']}")
        else:
            print("Unknown command!")
        command = input()



def id_check(student_id, students):
    """checks if student id exists and returns student if it does

    Args:
        student_id (int, str): id of the student 
        students (dict): students dictionary

    Returns:
        bool, dict: returns False if student is not found, otherwise returns student
    """
    for student in students:
        if student_id == student["id"]:
            return student["id"]
    print(f"No student is found for id={student_id}")
    return False


def email_check(email, students):
    """checks if email exists in students dictionary

    Args:
        email (str): email to check
        students (dict): students dictionary

    Returns:
        bool: returns False if email exists, otherwise returns True
    """
    for student in students:
        if email == student["email"]:
            print("Email already exists")
            return False
    return True

def main():
    """main function
    """
    print("Learning progress tracker")
    command = input()
    command_list(command.strip())


if __name__ == "__main__":
    main()
