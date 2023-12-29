# @Kyle Stewart @Heatflowsim.py version 1
from itertools import count


def read_data():  # This asks the user for 5 inputs. 2 heater/cooler temps
    # Along with 2 initial temps by the user with a final stability input
    A = float(input("Heater/Cooler Temperature A: "))
    B = float(input("Heater/Cooler Temperature B: "))
    T1 = float(input("Initial Temperature #1 "))
    T2 = float(input("Initial Temperature #2 "))
    S = float(input("Stability Criteria: "))
    # Then returns the values as a tuple
    return A, B, T1, T2, S


def initialize_plate(T1, T2):
    rows, columns = 8, 6

    # This makes a plate
    # Creates a 2D list with 8 rows and 6 columns
    # Each element in the plate is set ti T1 and T2 based on quadrant_check
    plate = [[T1 if quadrant_check(i, j, rows, columns) else T2 for j in range(columns)] for i in range(rows)]
    return plate


def print_plate(plate, A, B):
    print(f"{A:^74.2f}")
    # This prints the plate with the heater/cooler temp A and B
    for i, row in enumerate(plate):
        print(" " * 16 + "".join(f"{temp:>8.2f}" for temp in row))

        if i == 3:
            print(f"{A:<16.2f}" + "-" * 48 + f"{B:>16.2f}")
        else:
            print(" " * 16 + "-" * 48)

    print(f" {B:^74.2f}")
    # Prints the plate with the separators between numbers


# This function makes a new plate with heater/cooler temp A and B
# Then calculates the temp for each cell in the new_plate
# based on the cell's neighbors using the calculate_cell_temperature() function.
def calculate_new_plate(current_plate, A, B):
    rows, columns = 8, 6

    plate_rows, plate_columns = rows + 2, columns + 2

    p_plate = [[0.0 for _ in range(plate_columns)] for _ in range(plate_rows)]

    for i in range(rows):
        for j in range(columns):
            p_plate[i + 1][j + 1] = current_plate[i][j]

    p_plate[0] = [A] * plate_columns
    p_plate[rows + 1] = [B] * plate_columns

    for i in range(1, rows + 1):
        p_plate[i][0] = A
        p_plate[i][columns + 1] = B

    new_plate = []
    for i in range(1, rows + 1):
        new_row = []
        for j in range(1, columns + 1):
            new_row.append(calculate_cell_temperature(i, j, p_plate))

        new_plate.append(new_row)

    return new_plate


# This function checks if the new_plate has reached a stable state based on the old_plate and the Stability Criteria S
# Compares each element in the old_plate and new_plate
def check_stable_state(old_plate, new_plate, S):
    for i in range(len(old_plate)):
        for j in range(len(old_plate[0])):
            old_temp = old_plate[i][j]
            new_temp = new_plate[i][j]

            # If the change in temp goes past the Stability Criteria, it returns False
            if old_temp == 0:
                if new_temp != 0:
                    return False

            change = abs(old_temp - new_temp) / old_temp
            if change > S:
                return False
    # If all elements remain the same or the change in temp is within the Stability Criteria, it returns True
    return True


def quadrant_check(i, j, rows, columns):
    return (i < rows // 2 and j < columns // 2) or (i >= rows // 2 and j >= columns // 2)


# This function checks if a cell is in the top-left or bottom-right quadrant of the plate
# It returns True if the cell is in either of these quadrants, False otherwise

def calculate_cell_temperature(i, j, plate):
    average = (sum((plate[i - 1][j], plate[i + 1][j], plate[i][j - 1], plate[i][j + 1])) / 4)

    return average


# This function calculates the average temp of a cell based on its neighbors
# It takes the average of the temps of the cell's top, bottom, left, and right neighbors

def run_simulation(A, B, T1, T2, S):
    plate = initialize_plate(T1, T2)

    print(f"### Initial Plate ###")
    print_plate(plate, A, B)

    for a in count(1):
        new_plate = calculate_new_plate(plate, A, B)

        print(f"### Plate#: {a} ###")
        print_plate(new_plate, A, B)

        if check_stable_state(plate, new_plate, S):
            break

        plate = new_plate

        # This function runs the simulation using the given parameters It initializes the plate using the
        # initialize_plate() function it then prints the initial plate using the print_plate() function
        # It enters a loop where it calculates the new plate using the calculate_new_plate() function and checks if
        # It has reached a stable state using the check_stable_state() function
        # It prints each new plate and breaks the loop when the plate reaches a stable state


if __name__ == "__main__":
    A, B, T1, T2, S = read_data()
    run_simulation(A, B, T1, T2, S)
    # This starts the program
    # Calling read_data() and then run_simulation with the imputed values
