# @Kyle Stewart @Waterfall.py version 1
def waterfall(number):
    total_backslashes = 0
    total_forwardslashes = 0
    # Makes both forward and backslash = 0

    for i in range(number, 0, -1):  # From user inputted number down to 1
        if i % 2 == 0:  # check if i is dividable by 2
            backslash = "\\" * i  # Create string of backslashes
            print(backslash)  # Print string of backslashes
            total_backslashes += i  # Add total backslashes
        else:
            forwardslash = "/" * i  # Create string of forward slashes
            print(forwardslash)  # Print string of forward slashes
            total_forwardslashes += i  # Add total forward slashes

    print("Total \\:", total_backslashes)  # Print total amount of backslashes
    print("Total /:", total_forwardslashes)  # Print total amount of forward slashes


# Accepts user input
number = int(input)  # The user will enter a positive integer
waterfall(number)  # Calls the waterfall function with the user inputted number
