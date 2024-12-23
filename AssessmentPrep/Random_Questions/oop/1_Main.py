from Person import Person

Person.domain_name = input("Enter domain name\n")

choice = "yes"
person_list = []

while choice == "yes":
    print("enter details of person")
    person_firstname = input("enter first name\n")
    person_lastname = input("enter last name\n")
    person_age = input("enter age\n")

    person_list.append(Person(person_firstname, person_lastname, person_age))

    choice = input("do you want to add the details of another person? type yes/no\n")


print("number of objects created \n", Person.counter)

print("list person details")
for person in person_list:
    print("Full name of the person is ", person.fullname())
    print(person)
    print("\n")

print("update person details")
name = input("enter the full name of the person whose details are to be updated\n")

for person in person_list:
    if person.fullname() == name:
        print("old age: ", person.age)
        age = input("enter age\n")
        person.age = age
        print("updated person details :")
        print(person)
        break

else:
    print("Person not found")