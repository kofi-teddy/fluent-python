# Conditons

# region = input("What region are you in? ")
# tax = 0

# if region == "Accra":
#     tax = 0.05
# elif region == "Central":
#     tax = 0.05
# elif region == "Volta":
#     tax = 0.07
# else:
#     tax = 0.15
# print(tax)

# # Using or
# if region == "Accra" or region == "Central":
#     tax = 0.05
# elif region == "Volta":
#     tax = 0.07
# else:
#     tax = 0.15
# print(tax)

# # Using in
# if region in ("Accra", "Central"):
#     tax = 0.05
# elif region == "Volta":
#     tax = 0.07
# else:
#     tax = 0.15
# print(tax)

# # Nested if statement
# country = input("What country are yo from? ")
# tax = 0

# if country.lower() == "ghana":
#     region = input("What region are you in? ")

#     if region in ("Accra", "Central"):
#         tax = 0.05
#     elif region == "Volta":
#         tax = 0.07
#     else:
#         tax = 0.15
# else:
#     tax = 0

# print(tax)


# # Complex conditions
# gpa = float(input("Input your grade point average: "))
# lowest_grade = float(input("Input your lowest grade: "))
# if gpa > .89:
#     if lowest_grade >= .70:
#         print("You made the honor roll")


# # Complex conditions using and
# gpa = float(input("Input your grade point average: "))
# lowest_grade = float(input("Input your lowest grade: "))
# if gpa > .89 and lowest_grade >= .70:
#     print("You made the honor roll")


# Complex conditions using and boolean values
gpa = float(input("Input your grade point average: "))
lowest_grade = float(input("Input your lowest grade: "))

if gpa > .89 and lowest_grade >= .70:
    honor_roll = True
else: 
    honor_roll = False

if honor_roll:
    print("You made the honor roll")
