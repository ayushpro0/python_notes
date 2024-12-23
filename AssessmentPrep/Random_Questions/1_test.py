student = int(input("Number of students:\n"))
team = int(input("Number of teams:\n"))

students_in_team = student // team

student_left_out = student % team

print("The number of student in each team is", students_in_team, "and left out is", student_left_out)
