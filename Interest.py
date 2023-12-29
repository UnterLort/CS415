# Constant months in a year
MONTHS_IN_A_YEAR = 12

# Assigning the investment value to principal
print("Enter the principal value")
principal = float(input())

# Assigning the interest rate
print("Enter the interest rate")
interest_rate = float(input())

# Calculating the interest
interest = principal * interest_rate

# Calculating the updated principal
principal = principal + interest

# The output of the calculated interest
print(f"The interest earned is ${interest}")

# The output of the updated principal value
print(f"The value of the investment after one year is ${principal:.2f}")

# The output that calculates the average interest paid per month
print(f"The average interest is ${interest / MONTHS_IN_A_YEAR:.2f}")
