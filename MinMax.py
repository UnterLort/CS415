list1 = []
# Makes the empty list

# This loops this till the user ends it with the proper command
while True:

    # Starts off the loop asking the user for a command
    print("Enter a command.")
    userinput = str(input())

    # If the command is "a"
    # This will add a number to the list that the user inputs
    if userinput == "a":
        print("Enter the number to add.")
        number = int(input())
        list1.append(number)

    # If the command is "M"
    # This will display the largest number
    elif userinput == "M":
        if len(list1) == 0:
            print("No elements in list.")
        else:
            number = max(list1)
            print(f"The largest number is {number}")

    # If the command is "m"
    # This will display the smallest number
    elif userinput == "m":
        if len(list1) == 0:
            print("No elements in list.")
        else:
            number = min(list1)
            print(f"The smallest number is {number}")

    # If the command is "<"
    # This will list everything from the list greater than the user input
    elif userinput == "<":
        print("Enter the threshold for this search.")
        number = int(input())
        list2 = []
        if len(list1) == 0:
            print(list1)
        else:
            for a in list1:
                if a < number:
                    list2.append(a)
                    print(f"The numbers below this threshold are {list2}")

    # If the command is ">"
    # This will list everything from the list less than the user input
    elif userinput == ">":
        print("Enter the threshold for this search.")
        number = int(input())
        list3 = []
        if len(list1) == 0:
            print(list1)
        else:
            for a in list1:
                if a > number:
                    list3.append(a)
                    print(f"The numbers above this threshold are {list3}")

    # If the command is "d"
    # This will remove a number from the list that the user inputs
    elif userinput == "d":
        print("Enter the number to remove.")
        number = int(input())
        if len(list1) == number:
            print(f"{number} was not found in the list.")
        else:
            list1.remove(number)
            print(f"{number} was removed from the list.")

    # If the command is "q"
    # This will break the loop stopping the program
    elif userinput == "q":
        print("Goodbye")
        break

    # If the command is anything else this will print invalid and continue the loop
    else:
        print("Invalid command.")
        continue
