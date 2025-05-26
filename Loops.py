#Assignment on taxation system
i = 1
while i <= 5:
    # Assignment on taxation system

    salary = int(input("please enter your salary"))

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
        print("no tax")
        print(f'net_salary:{net_income} tax is {tax}')

    i = i + 1

print("Thank you for using the itax system")





