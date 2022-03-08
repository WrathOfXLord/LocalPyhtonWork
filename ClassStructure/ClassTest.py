from cgi import test


class TestClass:

    def __init__(self, name = "None", age = 18) -> None:
        self.name = name
        self.age = age
        print("one arg constructor" , "Test name: " + self.name, "Age:", self.age)

    def getName(self):
        return self.name
    
    def setName(self, name) -> None:
        self.name = name

# operator overload for printing object
    def __str__(self) -> str:
        return "Name: {}, Age: {}.".format(self.name, self.age)
# operator overload for + operator
    def __add__(self, other):
        return TestClass(self.name + other.name, (self.age + other.age) / 2)
# operator overload for += operator
    def __iadd__(self, other):
        self.name += other.name
        self.age = (self.age + other.age) / 2
        return self
# operator overload for - operator
    def __sub__(self, other):
        return TestClass("Sub", self.age - other.age)

# Similar to __iadd__(), you have __isub__(), __imul__(), __idiv__() 
# and other special methods which define the behavior of -=, *=, /=, and others alike.


testObj = TestClass()
print("--------------------")
testObj = TestClass(age=23)

testObj.setName("Rex")
print("Name of object:", testObj.getName())
otherObj = testObj + TestClass()
print(otherObj)

x, y = 4, 5

testObj += otherObj

print("x:", testObj)
print(testObj - otherObj)
