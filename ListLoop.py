# @Kyle Stewart @ListLoop.py version 2
import random
import statistics


# These both import needed modules for later


# This function figures out minimum, maximum, and if the list has numbers or not
def list_stats(number):
    if len(number) == 0:
        return None, None, None
        # This if statement is to make sure the list has integers and is not empty

    minvalue = number[0]
    # Sets the minimum value as the first integer in the list
    maxvalue = number[0]
    # Sets the maximum value as the first integer in the list
    total = 0
    # This sets the total said to what is specified

    for n in number:
        if n > maxvalue:
            maxvalue = n
            # This goes through to make sure the maximum value is the largest from the list
        if n < minvalue:
            minvalue = n
            # This goes through to make sure the minimum value is the smallest from the list
        total += n

    average = total / int(len(number))
    return minvalue, maxvalue, average
    # Returns the values


def check_work(number):
    minvalue = min(number)  # Gets the minimum value
    maxvalue = max(number)  # Gets the maximum value
    average = statistics.mean(number)  # Gets the average value
    return minvalue, maxvalue, average
    # Returns the values


# This makes an empty list
number = []

# Fills the list with 50 integers between 0 and 100
for n in range(50):
    number.append(random.randint(0, 100))

# This calls the first function
minvalue1, maxvalue1, average1 = list_stats(number)

# If None, None, None is returned then this will be printed if not the final function is called
if len(number) == 0:
    print("ERROR: Empty list provided.")
else:
    minvalue, maxvalue, average = check_work(number)
    if minvalue == minvalue1 and maxvalue == maxvalue1 and average == average1:
        # At the end all these will be printed
        print(f"Maximum value in array: {maxvalue}")
        print(f"Minimum value in array: {minvalue}")
        print(f"Average value of array: {average}")
        print("All statistics match!")

