"""Q4. Write a Python program that does the following:
1. Asks for the number of hours worked by each baker last week.
2. Stores this information in separate variables.
3. Determines each baker's gross pay based on their respective pay rates and overtime rules. Consider the different thresholds for overtime pay.
4. Applies a 30% tax rate to each baker's gross pay.
5. Subtracts the calculated taxes from each baker's gross pay to determine their net pay.
6. Displays each baker's hours worked, gross pay, taxes, and net pay in a clear and organized format, using appropriate labels."""

# Constants for pay rates
RATE_BAKER1 = 15.00
RATE_BAKER2 = 16.25
RATE_BAKER3 = 17.75

# Constants for overtime thresholds
THRESHOLD_BAKER1 = 35
THRESHOLD_BAKER2 = 40
THRESHOLD_BAKER3_LOW = 41
THRESHOLD_BAKER3_HIGH = 45

# Tax rate
TAX_RATE = 0.30

# Function to calculate gross pay for Baker 1
def calculate_gross_pay_baker1(hours_worked):
    regular_hours = min(hours_worked, THRESHOLD_BAKER1)
    overtime_hours = max(0, hours_worked - THRESHOLD_BAKER1)
    return (regular_hours * RATE_BAKER1) + (overtime_hours * RATE_BAKER1 * 1.5)

# Function to calculate gross pay for Baker 2
def calculate_gross_pay_baker2(hours_worked):
    regular_hours = min(hours_worked, THRESHOLD_BAKER2)
    overtime_hours = max(0, hours_worked - THRESHOLD_BAKER2)
    return (regular_hours * RATE_BAKER2) + (overtime_hours * RATE_BAKER2 * 2)

# Function to calculate gross pay for Baker 3
def calculate_gross_pay_baker3(hours_worked):
    regular_hours = min(hours_worked, THRESHOLD_BAKER3_LOW)
    overtime_hours = min(max(0, hours_worked - THRESHOLD_BAKER3_LOW), THRESHOLD_BAKER3_HIGH - THRESHOLD_BAKER3_LOW)
    double_time_hours = max(0, hours_worked - THRESHOLD_BAKER3_HIGH)
    return (regular_hours * RATE_BAKER3) + (overtime_hours * RATE_BAKER3 * 1.5) + (double_time_hours * RATE_BAKER3 * 2)

# Function to calculate taxes
def calculate_taxes(gross_pay):
    return gross_pay * TAX_RATE

# Function to calculate net pay
def calculate_net_pay(gross_pay, taxes):
    return gross_pay - taxes

# Input hours worked for each baker
hours_baker1 = float(input("Enter hours worked by Baker 1: "))
hours_baker2 = float(input("Enter hours worked by Baker 2: "))
hours_baker3 = float(input("Enter hours worked by Baker 3: "))

# Calculate gross pay for each baker
gross_pay_baker1 = calculate_gross_pay_baker1(hours_baker1)
gross_pay_baker2 = calculate_gross_pay_baker2(hours_baker2)
gross_pay_baker3 = calculate_gross_pay_baker3(hours_baker3)

# Calculate taxes for each baker
taxes_baker1 = calculate_taxes(gross_pay_baker1)
taxes_baker2 = calculate_taxes(gross_pay_baker2)
taxes_baker3 = calculate_taxes(gross_pay_baker3)

# Calculate net pay for each baker
net_pay_baker1 = calculate_net_pay(gross_pay_baker1, taxes_baker1)
net_pay_baker2 = calculate_net_pay(gross_pay_baker2, taxes_baker2)
net_pay_baker3 = calculate_net_pay(gross_pay_baker3, taxes_baker3)

# Display results
print("\nPayroll Summary:")
print(f"\nBaker 1 - Hours Worked: {hours_baker1} | Gross Pay: ${gross_pay_baker1:.2f} | Taxes: ${taxes_baker1:.2f} | Net Pay: ${net_pay_baker1:.2f}")
print(f"\nBaker 2 - Hours Worked: {hours_baker2} | Gross Pay: ${gross_pay_baker2:.2f} | Taxes: ${taxes_baker2:.2f} | Net Pay: ${net_pay_baker2:.2f}")
print(f"\nBaker 3 - Hours Worked: {hours_baker3} | Gross Pay: ${gross_pay_baker3:.2f} | Taxes: ${taxes_baker3:.2f} | Net Pay: ${net_pay_baker3:.2f}")