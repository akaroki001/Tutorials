# Program to determine if a client can get a loan
# Conditions:
#   1. Minimum balance should be above 10000
#   2. Age should be between 30 and 50 (inclusive)
# Loan attracts 15% interest
# Get user inputs
balance = float(input("Enter the client's account balance: "))
age = int(input("Enter the client's age: "))
loan_amount = float(input("Enter the desired loan amount: "))

# Check eligibility
if balance > 10000 and 30 <= age <= 50:
    interest_rate = 0.15  # 15%
    interest_amount = loan_amount * interest_rate
    total_payable = loan_amount + interest_amount

    print("\nThe client is ELIGIBLE for the loan.")
    print(f"Loan amount: {loan_amount:.2f}")
    print(f"Interest amount (15%): {interest_amount:.2f}")
    print(f"Total payable amount: {total_payable:.2f}")
else:
    print("\nThe client is NOT eligible for the loan.")
    print("Reason: Balance must be above 10,000 and age must be between 30 and 50.")
