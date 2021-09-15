class Students:
    def __init__(self,name,age):
        self.name = name
        self.age= age

student = Students("Saumya",22)
stud = Students("Ashish",22)


print(stud.name)
print(hasattr(student,"age"))

print(hasattr(student,"salary"))

