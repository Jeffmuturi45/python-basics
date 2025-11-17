# class definition
class Student:

    # define constructor/initializer
    def __init__(self, name, score):
        self.name = name
        self.score = score

        # define method
    def display(self):
            print(f"Name:{self.name}, Score: {self.score}")

            # define method to check if student passes
    def check_pass(self):
            return self.score >= 50

            # create objects
student1= Student("KEN", 85)
student2 = Student("JAMES", 90)

            # use methods
student1.display()
print(f"passed status:{student1.check_pass()}")