class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def displayStudent(self):
        return ("My name is " +self.name+ " and my age is "+ str(self.age))



Stu = Students("Ashish Yadav",23)


print(Stu.displayStudent())
