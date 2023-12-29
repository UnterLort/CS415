# @Kyle Stewart @GPA.py version 1

# Print a message
print("GPA Calculator")

# Print and prompt the user for a int
total_classes = int(input("Enter total classes: "))

# Create an empty list
grades = []

# Iterate through each class using a for loop
for i in range(total_classes):
    # Use a while loop to ensure a valid grade is entered
    while True:
        # Prompt the user to enter the grade
        grade = input("Enter grade for class {}: ".format(i + 1))

        # Check if the entered grade is numeric
        if grade.isnumeric():
            # Convert the grade to an integer and add it to list
            grades.append(int(grade))
            break
        else:
            # Print an error message if a non-numeric is entered
            print("Percentage grades only please!")

# Calculate the total sum of all grades
total_grades = sum(grades)

# Average grade by dividing the total sum of grades / classes
avg_grade = total_grades / total_classes

# Calculate the GPA
gpa = (avg_grade / 20) - 1

# Print the calculated GPA to 2 decimal places
print("Your GPA: {:.2f}".format(max(0.0, gpa)))
