# These are all the variables with the weight attached to each

participation = 0.15
tests = 0.45
projects = 0.40

# This will ask the user about what the student's participation grade
# The user will then be able to enter it

print("Enter student's participation grade.")
participation_grade = float(input())

# The user will do the same here but at the end give the user the average of the test grades

print("Enter student's first test grade.")
test_grade_1 = float(input())

print("Enter student's second test grade.")
test_grade_2 = float(input())

print("Enter student's third test grade.")
test_grade_3 = float(input())

test_average = (test_grade_1 + test_grade_2 + test_grade_3) / 3
print(f"Test average:{test_average:.2f}")

# The user will do the same here but at the end give the user the average of the project grades

print("Enter student's first project grade.")
project_grade_1 = float(input())

print("Enter student's second project grade.")
project_grade_2 = float(input())

project_average = (project_grade_1 + project_grade_2) / 2
print(f"Project average:{project_average:.2f}")

# This will finally add up all the grades into one final grade

student_grade = ((participation_grade * participation) + (test_average * tests) + (project_average * projects)) / 3

print(f"Student grade:{student_grade:.2f}")
