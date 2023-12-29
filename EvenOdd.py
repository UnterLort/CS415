# @Kyle Stewart @EvenOdd.py version 1
# Makes even and odd both = 0
def count(number):
    even = 0
    odd = 0

    for i in number:
        if i % 2 == 0:  # Check if number is even
            even += 1  # Number is even
        else:
            odd += 1  # Number is odd
    if even > odd:  # If the count of even is greater than the count of odd
        return "E"  # Return E
    elif even < odd:  # If the count of even is less than the count of odd
        return "O"  # Return O
    else:  # If even count and odd count are equal
        return "="  # Return =


if __name__ == "__main__":
    numbers = []  # Make an empty list
    while True:
        number = input()  # Prompt user with an input
        if number == ";":  # Until ; is inputted the loop will not end
            break
        numbers.append(int(number))  # Add inputted integer to list

    result = count(numbers)  # Calls function
    print(result)
