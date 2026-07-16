class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


    def introduce(self):
            print ("Hello")
            print ("My name is ", self.name)
            print ("I am ", self.age,"years old")
            print ("I study ", self.course)


student1 = Student("Ahmed", 30, "Machine Learning")
student2 = Student("Ali", 25, "Data Science")
student1.introduce()
student2.introduce()