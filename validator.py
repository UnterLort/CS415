# @Kyle Stewart @validator.py version 1

def validate_line(text):
    field = text.split(' ')  # Split the input text into field using a space as limiter
    num_field = len(field)  # Get the number of field in the line

    # Check number of field
    if num_field != 5:  # If the number of field is not 5 raise ValueError
        raise ValueError(f'wrong number of fields: {num_field}')

    # Check year
    try:
        year = int(field[0])  # Convert the year field to an int
        if year < 1900 or year > 2300:  # If the year is out of range raise ValueError
            raise ValueError(f'Year field of {year} is out of range')
    except ValueError:
        raise ValueError(f'year field value of "{field[0]}" is not an integer')
        # If the year value is not an int raise ValueError

    # Check month
    try:
        month = int(field[1])  # Convert the month field to an int
        if month < 1 or month > 12:  # If the month is out of range raise ValueError
            raise ValueError(f'Month field of {month} is out of range')
    except ValueError:
        raise ValueError(f'month field value of "{field[1]}" is not an integer')
        # If the month value is not an int raise ValueError

    # Check day
    try:
        day = int(field[2])  # Convert the day field to an int
        if day < 1 or day > 31:  # If the day is out of range raise ValueError
            raise ValueError(f'Day field of {day} is out of range')
    except ValueError:
        raise ValueError(f'day field value of "{field[2]}" is not an integer')
        # If the day value is not an int raise ValueError

    # Check magnitude
    try:
        mag = float(field[3])  # Convert the magnitude field to a float
        if mag < 0.0 or mag > 10.0:  # If the magnitude is out of range raise ValueError
            raise ValueError(f'Magnitude field of {mag} is out of range')
    except ValueError:
        raise ValueError(f'Magnitude field value of "{field[3]}" is not a number')
        # If the magnitude value is not a float raise ValueError

    # No errors then return
    return


def validate_file(filename):
    with open(filename, 'r') as file:  # Open the file in read mode
        line_number = 1  # Initialize the line number
        error_count = 0  # Initialize the error count
        for line in file:  # Iterate over each line in the file
            line = line.strip()  # Remove leading and trailing whitespace from the line
            try:
                validate_line(line)  # Validate the line using the validate_line function
            except ValueError as e:  # Catch the ValueError exception
                print(f'line {line_number:2}: {str(e)}')  # Print the error message along with the line number
                error_count += 1  # Increment the error count
            line_number += 1  # Increment the line number after each iteration

    print(f'processing complete: errors {error_count} lines {line_number - 1}')
    # Print the number of errors and total lines processed


validate_file('earthquake.txt')
