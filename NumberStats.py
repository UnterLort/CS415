def number_stats():
    # This is defining the function

    print("Enter an integer:")
    text = int(input())
    # This asks the user for an integer

    print(f"+ Number entered: {text}")
    # This prints the integer that the user entered

    if (text % 2) == 0:
        print("+ Number is even: True")
    else:
        print("+ Number is even: False")
    # This prints if the integer entered is even or not

    if text > 50:
        print("+ Number is greater than 50: True")
    else:
        print("+ Number is greater than 50: False")
        # This prints if the integer is more than 50


# This runs the function
number_stats()
