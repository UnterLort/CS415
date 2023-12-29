# @Kyle Stewart @Bubblesort.py version 2

from punch_timer import punch_in, punch_out, punch_diff
import random


# This imports the needed modules from the already made python file
# Along with needed for random parts of the code


def bubble_sort(number):
    # Bubble sort sorts the list made below.
    n = len(number)
    for i in range(n):
        for j in range(n - i - 1):
            if number[j] > number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]
    return number


list1 = []
# This makes a new empty list

print("Enter the size of the list to sort: ")
userinput = int(input())
# Asks the user for a number for a random generator
for a in range(userinput):
    list1.append(random.randint(-100, 100))
# fills the list with the userinput amount of numbers between -100 and 100

if userinput < 20:
    print(f"Unsorted List: {list1}")
# prints the list if less then 20
times = punch_in()

sortedlist1 = bubble_sort(list1)

timee = punch_out()
# sorts the list and times how long thst takes

if userinput < 20:
    print(f"Sorted List: {sortedlist1}")
# prints sorted list

# gets the time it took in nanoseconds then prints it
timedif = punch_diff(times, timee)
print(f"This took {timedif} nanoseconds.")


# fills a new list with the userinput amount of numbers between -100 and 100
list2 = []
for c in range(userinput):
    list2.append(random.randint(-100, 100))

# If less then 20 print the list
if userinput < 20:
    print(f"Unsorted New List: {list2}")


# Sort the list along with timing it
times1 = punch_in()

list2.sort()

timee1 = punch_out()

# Calculating the time sorting took
timedif1 = punch_diff(times1, timee1)
# If less then 20 print new list then print how long the sorting took
if userinput < 20:
    print(f"Sorted New List: {list2}")
print(f"This took {timedif1} nanoseconds.")


# bubble_sort take much longer then the sort function already in python.
# Doing it manually takes a lot more time than just a sort function.
# bubble_sort takes about 20900 nanoseconds compared to the sort which only took 3200 nanoseconds
