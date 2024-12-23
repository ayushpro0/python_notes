class Person:
    domain_name = ""
    counter = 0

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__email = f"{first_name}.{last_name}@{Person.domain_name}"
        Person.counter += 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def __str__(self):
        return f"{self.fullname()} is {self.__age} years old and her email id is {self.__email}"

    def fullname(self):
        return f"{self.__first_name} {self.__last_name}"