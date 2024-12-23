class NotEligibleException(Exception):
    pass

class Student:
    def __init__(self, marks):
        self.marks = marks


    def check_marks(self):
        if self.marks >= 90:
            return True
        else:
            raise NotEligibleException("Not Eligible")
try:
    marks = int(input())
    student1 = Student(marks)

    if student1.check_marks():
        print("eligible")

except NotEligibleException as e:
    print("inside except block : ", e)