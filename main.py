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


def student_add(students, new_id=10000):
    """takes user input for student credentials and adds them to students dictionary

    Args:
        students (dict): students dictionary
        new_id (int, optional): id of the new student. Defaults to 10000.

    Returns:
        int, dict: returns count of added students and updated students dictionary
    """
    count = 0
    updated_students = students
    print("Enter student credentials or 'back' to return:")
    user_input = input().strip()
    while user_input != "back":
        new_id = len(updated_students) + 10000
        student = student_check(user_input)
        if student:
            if email_check(student[2], students):
                updated_students[student[0]] = {
                    "name": student[0],
                    "surname": student[1],
                    "email": student[2],
                    "id": new_id,
                    "py": 0,
                    "dsa": 0,
                    "db": 0,
                    "fl": 0,
                }
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
    user_input = input().strip()
    while user_input != "back":
        user_input = user_input.split()
        student = id_check(user_input[0], students)
        student_grades = user_input[3:]
        if student:
            if len(user_input) != 7 or any(
                not point.isdigit() for point in student_grades
            ):
                print("Incorrect points format.")
            elif any(point < "0" for point in student_grades):
                print("Incorrect points format.")
            else:
                students[user_input[0]]["py"] += int(student_grades[0])
                students[user_input[0]]["dsa"] += int(student_grades[1])
                students[user_input[0]]["db"] += int(student_grades[2])
                students[user_input[0]]["fl"] += int(student_grades[3])
                print("Points updated.")
        user_input = input().strip()
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
        elif command == "add points":
            students = grade_add(students)
        elif command == "find":
            print("Enter an id or 'back' to return:")
            check_student = input().strip()
            while check_student != "back":
                name = check_student.split()[0:1]
                if name:
                    student = id_check(name[0], students)
                else:
                    print("No student is found for id=")
                if student:
                    print(
                        f"{student['name']} {student['surname']} {student['email']} points: Python={student['py']} DSA={student['dsa']} Databases={student['db']} Flask={student['fl']}"
                    )
                check_student = input().strip()
        elif command == "list":
            print("List of students:")
            if not students:
                print("No students found.")
            else:
                for student in students:
                    print(
                        f"{students[student]['name']} {' '.join(students[student]['surname'])} {students[student]['email']}"
                    )
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
        if student_id == students[student]["name"]:
            return students[student]
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
        if email == students[student]["email"]:
            print("This email is already taken.")
            return False
    return True


def main():
    """main function"""
    print("Learning progress tracker")
    command = input()
    command_list(command.strip())


if __name__ == "__main__":
    main()
