class Developer():
    def __init__(self, name = "NaN", salary = 0, languages = None):
        self.name = name
        self.salary = salary
        if languages is None:   #if we store a list inside of a variable then we should initialize like this one instead of default value
            languages = []
        self.languages = languages

    def addLanguage(self, newLanguage):
        self.languages.append(newLanguage)
    
    def printDeveloper(self):
        print("Developer's\n", "Name : {}\n".format(self.name), "Salary : {}\n".format(self.salary)
              ,"Languages : {}\n".format(self.languages))

    def setName(self, name):
        self.name = name

    def setSalary(self, salary):
        self.salary = salary

    def setLanguages(self, languages):
        self.languages = languages

    def raiseSalary(self, amount = 0):
        self.salary += amount

d1 = Developer("Ali Firat", 70000000, ["C", "C++", "Java", "Python"])
d1.printDeveloper()
d1.addLanguage("JavaScript")
d1.raiseSalary(897423)
d1.printDeveloper()
mylist = ["C++", "Java", "C", "Python", "JavaScript"]
d1.addLanguage("Rust")
# d1.setLanguages(mylist)     ##or d1.setLanguages(["C++", "Java", "C", "Python", "JavaScript"])
d1.printDeveloper()

d2 = Developer("d2")
d2.printDeveloper()
d2.addLanguage("Cpp")
d2.addLanguage("C")
d2.printDeveloper()

d3 = Developer("d3",salary = 2321)
d3.printDeveloper()

d4 = Developer("d4")
d4.printDeveloper()

class Manager(Developer):
    def __init__(self, name = "NaN", salary = 2000, languages = ["C"], PCRF = 5):   ##PCRF: Person Count Responsible For 
        super().__init__(name = name, salary = salary, languages = languages)
        self.PCRF = PCRF

    def printDeveloper(self):
        print("Manager's\n", "Name : {}\n".format(self.name), "Salary : {}\n".format(self.salary)
              ,"Languages : {}\n".format(self.languages), "PCRF : {}\n".format(self.PCRF))
        

manager1 = Manager("ali firat", 23522312342, ["C", "C++", "Java"], 523)
manager1.printDeveloper()
manager1.addLanguage("C#")
manager1.addLanguage("Go")

manager2 = Manager("m2")
manager2.printDeveloper()
manager2.raiseSalary(4554)

## polymorphism test field
print("\n\n-----test field-----\n\n")
developerList = [d1, d2, d3, d4, manager1, manager2]
for i in developerList:
    i.printDeveloper()

