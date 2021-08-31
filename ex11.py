# Inheritance

class Person():
    def __init__(self, name):
        # Constructor
        self.name = name

    def say_hello(self):
        print("Hello " + self.name)


class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        # Constructor
        self.school = school

    def sing_school_song(self):
        print("Old boy to " + self.school)        

    def say_hello(self):
        super().say_hello()
        print("Im rather tired")

    def __str__(self) -> str:
        return f"{self.name} attends {self.school}"

student = Student("Kofi", "Augustines")
print(student)

# student.say_hello()
# student.sing_school_song()


# Checks
# print(f"is this a student? {isinstance(student, Student)}")
# print(f"is this a person? {isinstance(student, Person)}")
# print(f"is Student a Person? {issubclass(Student, Person)}")