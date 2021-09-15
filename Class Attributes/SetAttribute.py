class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


stud1 = Student("xyz",78)

setattr(stud1,"salary","78000")

print(hasattr(stud1,"salary"))

print(stud1.salary)
