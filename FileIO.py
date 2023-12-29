# @Kyle Stewart @FileIO.py version 1
# Gets the first 3 tokens from a file
def get_tokens_from_file(file_name):
    with open(file_name) as f:
        text = f.read()
    tokens = text.split()
    return tokens[0:3]


# This prints the ASCII values and characters from a file
def get_characters_from_file(file_name):
    with open(file_name) as f:
        text = f.read()
    # This creates over each character in the text
    for character in text:
        # Calculate the ASCII value of the character
        ascii_value = ord(character)
        # Print the ASCII value and the character itself
        print(f"{ascii_value} {character}")


# This prints the integers from a file and calculate their sum
def get_ints_from_file_and_sum(file_name):
    with open(file_name) as f:
        text = f.read()
    tokens = text.split()

    total_sum = 0
    # Adds over each token in the text
    for token in tokens:
        # Checks if the token is a digit
        if token.isdigit():
            # Converts the token to an integer
            num = int(token)
            # Prints the integer
            print(num)
            # Adds the integer to the total sum
            total_sum += num
    # Prints the total sum of the integers
    print(total_sum)


# Starts the whole program
def main():
    # Gets the tokens from the file "test.txt"
    tokens = get_tokens_from_file("test.txt")
    # Prints each token
    for token in tokens:
        print(token)
    # Prints the ASCII values and characters from the file "test.txt"
    get_characters_from_file("test.txt")
    # Prints the integers from the file "integers.txt" and calculate their sum
    get_ints_from_file_and_sum("integers.txt")


# Starts the main function
if __name__ == "__main__":
    main()
