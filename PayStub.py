# This is the Reading Input.
# This will prompt the user with many print statements to fill out.

print("Enter your Fullname:")
Name = str(input())

print("Enter your Anniversary Month(1-12):")
Month = int(input())

print("Enter your Anniversary Year:")
Year = int(input())

print("Enter your hours worked this pay period(0-350):")
Hours = int(input())

print("Enter your Job Title:")
Title = str(input())

print("Enter your pay rate:")
Pay = float(input())

# This is the Calculations part.

# This is defining the Pay Period Month and Year.
Pay_Year = int(2023)
Pay_Month = int(9)

# This is finding the Total Months worked with the help of year variables.
Year_Tot = (Pay_Year - Year) * 12
Worked = Year_Tot + Month - Pay_Month

# This calculates the Vacation Time.
Vaca = Worked * 8.25

# This calculates the Gross Pay Rate.
Gross = Hours * Pay

# This calculates the Retirement Withholding.
Ret = Gross * .052

# This calculates the Tax Withholding.
Tax = (Gross - Ret) * .28

# This calculates the Net Payment.
Net = Gross - Ret - Tax

# This is the Displaying Output.
# This will print all parts of the Gekko & Co. Line by line.
# Some lines will have f strings and those will have variables inputted into the correct places.

print("=" * 42)
print("      Gekko & Co.")
print("")
print("          \"$\"")
print("          ~~~")
print("         /   \ `.")
print("        /     \  /")
print("       /_ _ _  \/")
print("")
print("-" * 42)
print(f"Pay Period:      {Pay_Month}/{Pay_Year}")
print(f"Name:            {Name}")
print(f"Title:           {Title}")
print(f"Hire Date:       {Month}/{Year}")
print(f"Months Worked:   {Worked} months")
print(f"Vacation hours: {Vaca: .2f}")
print("-" * 42)
print(f"Gross Pay:       $ {Gross: .2f}")
print(f"Retirement:      $ {Ret: .2f}")
print(f"Tax:             $ {Tax: .2f}")
print("-" * 24)
print(f"Net Pay:         $ {Net: .2f}")
print("=" * 42)
