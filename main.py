#Python3

def student_check(data):
    pass


def student_add():
    print("Enter student credentials or 'back' to return:")
    user_input = input().strip()
    if user_input == "back":
        return False
    if student_check(user_input):
        return True


def command_list(command):
    while True:
        if command == "exit":
            print('Bye!')
            return
        elif not command:
            print('No input')
        elif command == "add students":
            count = 0
            while student_add():
                count += 1
            print(f'Total {count} students have been added.')
        else:
            print('Unknown command!')


def main():
    print("Learning progress tracker")
    command = input()
    command_list(command.strip())