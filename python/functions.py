def welcome():
    print("welcome to the class")
    print("we shall be discussing functions")


print("===========")
welcome()
print("===========")


def welcome(name):
    print(f'{name} : welcome to the class')
    print("we shall be discussing functions")


print("===========")
welcome('austin')
print("===========")


# example grade system

def calculate_grade(x, y):
    total_marks = x + y
    return total_marks


def grader(z):
    if z >= 70:
        print(f'TOTAL_MARKS: {z} GRADE IS A')
    elif z >= 60:
        print(f'TOTAL_MARKS: {z} GRADE IS B')
    elif z >= 50:
        print(f'TOTAL_MARKS: {z} GRADE IS C')
    elif z >= 40:
        print(f'TOTAL_MARKS: {z} GRADE IS D')
    else:
        print(f' YOU HAVE FAILED TOTAL_MARKS: {z} GRADE IS E')




for numbers in range(10):
    cat = int(input("enter the cat marks"))
    final = int(input("enter the final marks"))
    grade = calculate_grade(cat, final)
    grader(grade)
