# @Kyle Stewart @try_except.py version 1
def build_number_list():
    # Create an empty list
    list = []
    while True:
        # Prompt the user to enter a number
        userinput = input("Enter a number to add to the list: ")
        if userinput == "DONE":
            # If the user enters "DONE", end the loop and return the list
            return list
        else:
            try:
                # Try to cast the user input as an integer
                nlist = int(userinput)
                # If successful, add the integer to the list
                list.append(nlist)
            except ValueError:
                # If casting to integer raises an exception, try casting as a float
                try:
                    nlist = float(userinput)
                    # If successful, add the float to the list
                    list.append(nlist)
                except ValueError:
                    # If casting to float also raises an exception, print an error message
                    print("ERROR: Non-numeric input provided.")


def raising_arizona(string):
    # Check if the string is equal to "Arizona"
    if string.lower() == "arizona":
        # If yes, raise a ValueError with the message "There is no Arizona!"
        raise ValueError("There is no Arizona!")
    else:
        # If not "Arizona", simply return the string passed as an argument
        return string


if __name__ == "__main__":
    print(build_number_list())
    try:
        # First call: passing "New Mexico"
        print(raising_arizona("New Mexico"))
    except ValueError as a:
        print(str(a))

    try:
        # Second call: passing "arizonA"
        print(raising_arizona("arizonA"))
    except ValueError as a:
        print(str(a))
