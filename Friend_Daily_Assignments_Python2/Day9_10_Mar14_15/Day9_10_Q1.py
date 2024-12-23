"""1.	Create Employee class.
Maintain class level variable “empCount”  and write function “displayCount()” to
display the total empCount.
Define instance variables Name and salaray.
Also write instance method “displayEmployee() to display all employee details (Name and Salary)


Override __str__() and  __repr__() methods to display Employee details (Name and
Salary), instead of default string representation."""


class Employee:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

    def displayAll(self):
        print("Name: ", self.name)
        print("Salary: ", self.sal)

    def __str__(self):
        return ("Employee Name: {}\nEmployee Salary: {}".format(self.name, self.sal))

    __repr__ = __str__


obj1 = Employee("Sayani", 50000)
obj2 = Employee("Rohan", 100000)
obj1.displayAll()
print('------str-----------')
print(obj1)
print('----repr------------')
print(repr(obj2))
print("-----instanceMethod------")
obj2.displayAll()
