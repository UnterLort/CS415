# @Kyle Stewart @binary_conversion.py version 1 lab 19
# Function converts the user inputted number to a binary number
def decimal_to_binary(decimal):
    if decimal <= 0:  # If the number is less than or equal to 0, end program
        return []
    else:  # Split decimal number into binary
        return [decimal % 2] + decimal_to_binary(decimal // 2)


def main():
    num = int(input("enter decimal number> "))  # Prompt user for a number

    if num <= 0:  # If the number is less than or equal to 0, print goodbye and end program
        print("goodbye")
        return

    binary = decimal_to_binary(num)[::1]  # sorts the binary number in reverse order
    print(f"binary values = {binary}")  # Print the binary number
    main()  # Re-loop the code


# Print start message
print("A value less than or equal to zero will terminate the program.")
if __name__ == "__main__":
    main()  # Call the main code
