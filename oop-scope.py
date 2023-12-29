# @Kyle Stewart @oop-scope.py version 1
from stack import Stack

stack = Stack()  # Makes the stack with an empty dictionary

# Prints welcome message and all commands
print("Welcome to the scope simulator. Available commands are:")
print("    quit - exit the simulator")
print("    set - set a variable in the current scope")
print("    get - get a variable from the current scope")
print("    enter - enter a new scope")
print("    exit - exit the current scope")
print("    print - print all the active scopes")
print("")
print(f"Entered global scope. There are {len(stack)} active scopes")
# Print the first message with the number of active scopes
while True:
    command = input(str("enter a command> "))

    if command == "print":
        # Print the index and contents of each scope in the stack
        for i, scope in reversed(list(enumerate(stack))):
            print(f"{i} {scope}")
    elif command == "set":
        setcomm = input("Enter a variable name> ")
        value = input("Enter value> ")
        stack.push({setcomm: value})
    elif command == "enter":
        # Add a new empty dictionary to the stack
        stack.push({})
        print(f"Entering new scope. There are {len(stack)} active scopes")
    elif command == "get":
        varname = input("Enter variable name> ")
        # Searches for the variable in the current scope and all scopes
        for scope in reversed(stack):
            if varname in scope:
                print(f"The value of {varname} is {scope[varname]}")
                break
            else:
                print(f"Variable {varname} is not defined")
                break
    elif command == "exit":
        if len(stack) > 1:
            # Removes the top of the stack for leaving the current scope
            stack.pop()
            print(f"Exiting scope. There are {len(stack)} active scopes")
        else:
            print("Cannot exit global scope")
    elif command == "quit":
        print("Quitting, goodbye")
        break
