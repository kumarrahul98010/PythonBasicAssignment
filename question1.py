class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

# Creating an object of the Person class
p1 = Person("John", 36)
p2= Person("raju", 44)
p2= Person("mehul" ,22)

# Calling the method myfunc()
p1.myfunc()
p2.myfunc()