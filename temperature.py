# @Kyle Stewart @temperature.py version 1

# Ask the user to enter temperature in Celsius
print("Enter temperature in Celsius:")
C = float(input())

# Convert temperature from Celsius to Fahrenheit
F = (C * 9/5) + 32

# Print the converted temperature and Celsius
print(f"{C:.1f} C = {F:.1f} F")
