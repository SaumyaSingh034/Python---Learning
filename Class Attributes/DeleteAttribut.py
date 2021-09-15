class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


stud = Student("FARED",89)

delattr(stud,"age")

print(hasattr(stud,"age"))
