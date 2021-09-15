class Parent:
    counter = 10
    def __init__(self):
        print("Parent class")

    def ParentFunc(self):
        print("Parent Function is being called")

    def setCounter(self,num):
        Parent.counter = num

    def showCounter(self):
        print(Parent.counter)



#Child Class Inherting Parent Class

class Child(Parent):
    def _init__(self):
        print("Child Class")

    def display(self):
        print("Child class is being invked")


c = Child()
c.display()
c.ParentFunc()
c.counter
c.setCounter(90)
c.showCounter()
