class Student:
    def __init__(self):
        self.total = None
        self.x = int(input("please enter the cat marks"))
        self.y = int(input("please enter the final marks"))
        print(f'cat: {self.x}  final_exam: {self.y}')

    def grades(self):
        self.total = self.x + self.y
        print(f'the total is : {self.total}')

    def qualify(self):
        if self.total > 40:
            print(f'Your total score is {self.total} Congratulations you have passed!')
        else:
            print("You have failed! ")


maureen = Student()
maureen.grades()
maureen.qualify()
alvin = Student()
alvin.grades()
alvin.qualify()
