# @Kyle Stewart @recursion.py version 1

def countdown(n):
    if n == 0:
        print("Blastoff!")  # Print the statement if n = 0
    else:
        return countdown(n - 1)  # Recursive calls with n - 1 as the argument


def counting_clovers(n):
    if n == 0:
        return 0  # Return 0 if n = 0
    else:
        return 4 + counting_clovers(n - 1)  # Recursive calls with n - 1 as the argument


def count_from_N_to_M(n, m):
    if n >= m:  # If n is greater or equal to m return
        return
    else:
        print(n)  # Print value of n
        count_from_N_to_M(n + 1, m)  # Recursive calls with n + 1 as the argument


# defines n and m along with running the functions
n = 10
print(countdown(n))
n = 0
counting_clovers(n)
n = 1
counting_clovers(n)
n = 10
counting_clovers(n)
n = 2
m = 4
count_from_N_to_M(n, m)
n = 6
m = 10
count_from_N_to_M(n, m)
