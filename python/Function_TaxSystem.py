def calculatetax(salary):
    if salary >= 500000:
        net_income = salary * 0.6
        tax = salary * 0.4
        print(f'net_salary:{net_income} tax is {tax}')
    elif (salary >= 300000) and (salary <= 499999):
        net_income = salary * 0.65
        tax = salary * 0.35
        print(f'net_salary:{net_income} tax is {tax}')
    elif (salary >= 100000) and (salary <= 299999):
        net_income = salary * 0.7
        tax = salary * 0.3
        print(f'net_salary:{net_income} tax is {tax}')
    elif (salary >= 50000) and (salary <= 99999):
        net_income = salary * 0.75
        tax = salary * 0.25
        print(f'net_salary:{net_income} tax is {tax}')
    elif (salary >= 10000) and (salary <= 49999):
        net_income = salary * 0.8
        tax = salary * 0.2
        print(f'net_salary:{net_income} tax is {tax}')
    else:
        net_income = salary
        tax = salary * 0
        print("no tax")
        print(f'net_salary:{net_income} tax is {tax}')

    return net_income


def loan(amount):
    if amount >= 300000:
        print("you qualify for a FULIZA LOAN not exceeding KSH 600000")
        loan_amount = int(input("please enter loan amount"))
        f_amount = (loan_amount * 0.2) + loan_amount
        print(f'loan approved is {loan_amount} total fuliza_repayment is  {f_amount}')
    elif amount >= 200000:
        print("you qualify for a FULIZA LOAN not exceeding KSH 400000")
        loan_amount = int(input("please enter loan amount"))
        f_amount = (loan_amount * 0.1) + loan_amount
        print(f'loan approved is {loan_amount} total fuliza_repayment is  {f_amount}')
    elif amount >= 100000:
        print("you qualify for a FULIZA LOAN not exceeding KSH 200000")
        loan_amount = int(input("please enter loan amount"))
        f_amount = (loan_amount * 0.05) + loan_amount
        print(f'loan approved is {loan_amount} total fuliza_repayment is  {f_amount}')
    else:
        print(f'{amount} does not qualify for a fuliza_loan')


for numbers in range(10):
    income = int(input("please enter your basic salary"))
    q_loan = calculatetax(income)
    loan(q_loan)



