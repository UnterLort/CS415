# @Kyle Stewart @Patterns.py version 1

# Asks the user for a string pattern input
print("Enter pattern:")
pattern = str(input())

# Asks the user for an integer input
print("Enter a positive integer between 1 and 10 inclusive:")
number = int(input())

# This if statement will then run using what the user inputted fot the pattern

if pattern == "H":
    print("*", end="")
    # Prints "*" + number in a horizontal line

elif pattern == "V":
    for i in range(number):
        print("*")
        # Prints "*" + number in a vertical line

elif pattern == "S":
    for i in range(number):
        print("**********"[:number])
        # Prints "*" + number in both the vertical line and horizontal line

elif pattern == "T":
    for i in range(number):
        print("*" * (i + 1))
        # This prints "*" + 1 every line after the first

else:
    for i in range(number):
        print(i * ' ' + "*")
        # This prints 1 space + "*" every line after the first
