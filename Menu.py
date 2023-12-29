# @Kyle Stewart @Menu.py version 2
# This starts the loop
while True:
    # Asks the user for an x and y input
    print("Please enter x and y:")
    x = int(input())
    y = int(input())
    # Asks the user for a command then an if statement is used
    print("Please enter a command:")
    command = str(input())
    # If the command is A or S the command variable will add or subtract the integers
    # then they will be printed for the user
    if command == "A":
        total = x + y
        print(f"{x} + {y} = {total}")
    elif command == "S":
        total = x - y
        print(f"{x} - {y} = {total}")
    # If the command is Q the loop will end
    elif command == "Q":
        print("Goodbye")
        break
    # If the user inputs none of the above an error will be printed
    else:
        print("Invalid command")
        continue
    # To continue will start the loop at the top
