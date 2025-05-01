# Class with Constructors
class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name}")

class Student(Person):
    def study(self):
        print("I study Python!")

student1 = Student("Alexio")
student1.speak()
student1.study()
