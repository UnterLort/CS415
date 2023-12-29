# @Kyle Stewart @q4.py version 1

def is_capitalized(word):
    # Checks if the first character of the word is a digit
    if word[0].isdigit():
        # Raises ValueError if the first character is a digit
        raise ValueError("Word must begin with a letter.")
    # Return True if the first character is uppercase else False
    return word[0].isupper()


def contains_4():
    try:
        # Opens the file with the given file_name in read mode
        with open(file_name, "r") as file:
            # Reads the file
            character = file.read()
            # Check if the character '4' is in the file
            if "4" in character:
                # Returns True if '4' is found
                return True
            else:
                # Returns False if '4' not found
                return False
    except FileNotFoundError:
        # Returns False if file not found
        return False


class Queue:
    def __init__(self):
        # Make an empty list to store queue items
        self.items = []

    def enqueue(self, item):
        # Add item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Check if the queue has any items
        if self.items:
            #  Remove and return the first item from the queue
            return self.items.pop(0)
        else:
            # Return None if no items
            return None


if __name__ == "__main__":
    # Ask the user to enter a file name
    file_name = input("Enter file name: ")
    try:
        # Check if the first letter of the file name is capitalized
        capitalized = is_capitalized(file_name)
        print(f"The first letter of '{file_name}' is not capitalized: {capitalized}")
    except ValueError as e:
        # Print the error message if the first letter is a digit
        print(e)

    # Check if the file contains '4'
    if contains_4():
        print(f"The file '{file_name}' contains the character '4'.")
    else:
        print(f"The file '{file_name}' doesn't contains the character '4'.")
