class Person:

    def __init__(self, name):
        self.name = name


    def greet(self):
        print(f"Hello {self.name}!")

class Teacher(Person): #inherits from person

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


    def teach(self):
        print(f"{self.name} is teaching {self.subject}!")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying grade {self.grade}!")


t1 = Teacher("Ken", "ENGLISH")
t1.teach()
st1 = Student("James", 5)
st1.study()
