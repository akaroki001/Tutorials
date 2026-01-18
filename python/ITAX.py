# Prompt the user for gross salary
gross_salary = float(input("Enter your gross salary: "))

# Determine the tax rate based on the brackets
if gross_salary > 500000:
    tax_rate = 0.40
elif gross_salary > 300000:
    tax_rate = 0.30
elif gross_salary > 200000:
    tax_rate = 0.20
elif gross_salary > 100000:
    tax_rate = 0.10
elif gross_salary < 50000:
    tax_rate = 0.00
else:
    # For 50,000 <= gross_salary <= 100,000
    tax_rate = 0.00

# Calculate tax and net pay
tax = gross_salary * tax_rate
net_pay = gross_salary - tax

# Display the results
print(f"Tax calculated: {tax:.2f}")
print(f"Net pay: {net_pay:.2f}")
