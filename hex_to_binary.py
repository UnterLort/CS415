# @Kyle Stewart @hex_to_binary.py CS 415 Quiz #3 version 1

def hex_to_binary(hex_string):
    binary_string = ""
    power_of_16 = 0
    # The syntax error is that this for loop is not closed
    for character in hex_string:
        # Get the decimal value of the digit
        if character.lower() == 'a':
            value = 10  # Values should have been decreased by 1
        elif character.lower() == 'b':
            value = 11
        elif character.lower() == 'c':
            value = 12
        elif character.lower() == 'd':
            value = 13
        elif character.lower() == 'e':
            value = 14
        elif character.lower() == 'f':
            value = 15
        else:  # character is a numeric digit (0-9)
            value = int(character)  # Converts the character to an integer

        # Add the binary version of the value to the string
        # Use zfill() to make extend any number with less than
        # 4 digits with leading zeros
        # Check out zfill! (www.w3schools.com/python/ref_string_zfill.asp)
        binary_string += f"{value:b}".zfill(4)

    # Return the string
    return binary_string


# Should print: 01000001
print(hex_to_binary('41'))

# Should print: 1000101011000101
print(hex_to_binary('8ac5'))

# Should print: 11011110101011011011111011101111
print(hex_to_binary('deadbeef'))
