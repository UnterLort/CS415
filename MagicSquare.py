# @Kyle Stewart @MagicSquare.py version 1
def print_square(list):
    # Takes the inputs from the user and sorts them in the proper list
    a, b, c = list[:3]
    d, e, f = list[3:6]
    g, h, i = list[6:]
    # Prints the square
    print(a, b, c)
    print(d, e, f)
    print(g, h, i)


def input_square():
    # Asks the user for a number for the square and then prompts the user to inputs one
    # This repeats till 9 numbers are collected
    print("Enter the top-left number of your square:")
    a = int(input())
    print("Enter the top-middle number of your square:")
    b = int(input())
    print("Enter the top-right number of your square:")
    c = int(input())
    print("Enter the middle-left number of your square:")
    d = int(input())
    print("Enter the center number of your square:")
    e = int(input())
    print("Enter the middle-right number of your square:")
    f = int(input())
    print("Enter the bottom-left number of your square:")
    g = int(input())
    print("Enter the bottom-middle number of your square:")
    h = int(input())
    print("Enter the bottom-right number of your square:")
    i = int(input())
    return [a, b, c, d, e, f, g, h, i]


def is_magic_square(list):
    # Sets all user inputs as list
    a, b, c, d, e, f, g, h, i = list
    # Adds up each column and row hopefully to 15
    aa = a + b + c
    bb = d + e + f
    cc = g + h + i
    dd = a + d + g
    ee = b + e + h
    ff = c + f + i
    # Adds up all the colum and row total together hopefully to 90. As 15 * 6 is 90
    total = aa + bb + cc + dd + ee + ff
    # If total is 90 print it is a magic square
    if total == 90:
        print("It is a magic square")
        # If not 90 print it is not a magic square
    else:
        print("It is not a magic square")


# Calls the functions in order
# Creating the argument list for the rest of the program
# Assigning the argument list to print_square and is_magic square
list = input_square()
print_square(list)
is_magic_square(list)
