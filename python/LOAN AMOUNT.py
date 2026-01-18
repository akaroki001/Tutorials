# Program to determine if a client can get a loan
# Condition: minimum balance should be above 10000
# Loan attracts 15% interest

# Get user inputs
balance = float(input("Enter the client's account balance: "))
loan_amount = float(input("Enter the desired loan amount: "))

# Check eligibility
if balance > 10000:
    interest_rate = 0.15  # 15%
    interest_amount = loan_amount * interest_rate
    total_payable = loan_amount + interest_amount

    print("\nThe client is ELIGIBLE for the loan.")
    print(f"Loan amount: {loan_amount:.2f}")
    print(f"Interest amount (15%): {interest_amount:.2f}")
    print(f"Total payable amount: {total_payable:.2f}")
else:
    print("\nThe client is NOT eligible for the loan because the balance is not above 10,000.")
