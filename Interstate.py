def road_direction(integer):
    # This is the first function finds if the number is even or odd.
    if integer % 2 == 0:
        print("primary east-west.")
    else:
        print("primary north-south.")


def belt_or_spur(integer):
    # This turns the integer into a string, so it can be used by the following if statement.
    integer_string = str(integer)
    first_integer = int(integer_string[0])
    last_integer = int(integer_string[1:])

    # This function finds out with an if statement is the 3rd digit is even or odd.
    if first_integer % 2 == 0:
        print(f"beltway for I-{last_integer}")
    else:
        print(f"spur for I-{last_integer}")


# Once found out the print statements only print the first two integers.


# This is the start and makes sure the user inputted an integer that is from 1 to 99.
print("Enter an interstate highway integer:")
integer = int(input())

if 1 <= integer <= 99:
    road_direction(integer)
elif 100 <= integer <= 999:
    belt_or_spur(integer)
else:
    print("invalid")
# If it is the right integer it will run the whole process.
