def calculate(salary):
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
        f_amount = amount * 0.2
        print(f'you have qualified for a fuliza loan of {f_amount}')
    elif amount >= 200000:
        f_amount = amount * 0.1
        print(f'you have qualified for a fuliza loan of {f_amount}')
    elif amount >= 100000:
        f_amount = amount * 0.05
        print(f'you have qualified for a fuliza loan of {f_amount}')
    else:
        print(f'{amount} does not qualify for a fuliza')
          

for numbers in range(10):
    income = int(input("please enter your salary"))
    q_loan = calculate(income)
    loan(q_loan)



