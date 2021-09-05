# Function

from datetime import datetime

# Function to print current date and time
# def print_time(task_name):
#     print("time completed")
#     print(datetime.now())
#     print(task_name)

# first_name = "Kofi"
# print_time("Printed first name")


# for x in range(0, 10):
#     print(x)
# print_time("printed for loop")


# # Get initials
# def get_initials(name):
#     initial = name[0:1].upper()
#     return initial

# # Ask name and return initials
# first_name = input("Enter you first name: ")
# first_name_initial = get_initials(first_name)

# middle_name = input("Enter you middle name: ")
# middle_name_initial = get_initials(middle_name)

# last_name = input("Enter you last name: ")
# last_name_initial = get_initials(last_name)

# print(f"Your initials are {last_name_initial}{first_name_initial}{middle_name_initial}")


# Get initials
def get_initials(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

# Ask name and return initials
first_name = input("Enter you first name: ")

# Name notations
first_name_initial = get_initials(name=first_name, force_uppercase=False)


print(f"Your initials is: {first_name_initial}")