# @Kyle Stewart @DMV.py version 2

# Function to validate the format of a New Hampshire license plate number
def validate_nh_license_plate(pnumber):
    if len(pnumber) != 7 or not pnumber.isdigit():
        return False
    return True


# Function to enter a new vehicle record
def enter_record():
    while True:
        pnumber = str(input("Enter the vehicle plate number."))
        if not validate_nh_license_plate(pnumber):
            print("Invalid plate number entered. Please enter a valid 7-digit plate number.")
            continue
        name = str(input("Enter the driver's full name: "))
        address = str(input("Enter the driver's street address: "))
        return pnumber, name, address


# Function to insert a vehicle record into the plate database
def insert_record(record, plate_db):
    name_address = (record[1], record[2])
    plate_db[record[0]] = name_address


# Function to look up a vehicle record in the plate database
def lookup_record(pnumber, plate_db):
    if pnumber in plate_db:
        return plate_db[pnumber]
    return None


# Empty database
plate_db = {}

# First message of the program
print("Welcome to the Department of Motor Vehicles!")

# The loop will keep running until the user ends it with the proper command
while True:
    # Prompts the user for a command
    command = str(input("Enter a command."))

    # If command is "a" then the user will be promoted to add a plate
    if command == "a":
        record = enter_record()
        insert_record(record, plate_db)
    # If command is "s" then the user will be promoted to input a plate
    # that has already been added to display it
    elif command == "s":
        pnumber = str(input("Enter the plate number to search for >"))
        if not validate_nh_license_plate(pnumber):
            print("Invalid plate number entered. Please enter a valid 7-digit plate number.")
            continue
        result = lookup_record(pnumber, plate_db)
        if result is None:
            print(f"No record of plate {pnumber} exists.")
        else:
            print(f"Information for plate {pnumber}:")
            print(f"----Name: {result[0]}")
            print(f"----Address: {result[1]}")
    # Prints all vehicle records if command is "p"
    elif command == "p":
        for pnumber in plate_db.keys():
            result = lookup_record(pnumber, plate_db)
            print(f"Information for plate {pnumber}:")
            print(f"----Name: {result[0]}")
            print(f"----Address: {result[1]}")
    # Quits the ends the while loop thus ends the program if "q"
    elif command == "q":
        print("Goodbye")
        break
    # If the user inputs anything not of a, s and p.
    # Will print Invalid command
    else:
        print("Invalid Command.")
