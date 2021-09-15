class Parent:
    def Func(self):
        print("Parent Class")



class Child(Parent):
    def Func(self):
        print("Child Class")


c = Child()
c.Func()
