#Python3
import re
def student_check(data):
    if data == '':
        print("Incorrect credentials")
        return False
    name_regex = r"^[A-Za-z][A-Za-z\-\']*[A-Za-z]$"
    surname_regex = r"^[A-Za-z][A-Za-z\-\']*[A-Za-z]$"
    email_regex = r"[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*"
    name = data.split()[0]
    surname = data.split()[1:-1]
    email = data.split()[-1]
    if len(data.split()) < 3:
        print("Incorrect credentials")
        return False
    if not re.match(name_regex, name):
        print("Incorrect first name")
        return False
    if not all(re.match(surname_regex, s) for s in surname):
        print("Incorrect surname")
        return False
    if not re.match(email_regex, email):
        print("Incorrect email")
        return False
    return True


def student_add():
    count = 0
    print("Enter student credentials or 'back' to return:")
    user_input = input().strip()
    while user_input != "back":
        if student_check(user_input):
            print("Student has been added.")
            count += 1
        user_input = input().strip()
    return count


def command_list(command):
    while True:
        if command == "exit":
            print('Bye!')
            return
        if not command:
            print('No input')
        elif command == "add students":
            print(f'Total {student_add()} students have been added.')
        elif command == "back":
            print("Enter 'exit' to exit the program")
        else:
            print('Unknown command!')
        command = input()


def main():
    print("Learning progress tracker")
    command = input()
    command_list(command.strip())

if __name__ == '__main__':
    main()