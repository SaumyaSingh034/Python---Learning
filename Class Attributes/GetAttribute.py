class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


stud = Student("FARED",89)

print(getattr(stud,"age"))
