# Dictionary
student = {
    "Student_Number": "ABMI/2034/2020",
    "Student_Name": "Mike mika",
    "Gender": "Male",
    "graduation_status": "Yes"
}

print(student)
print(student['Student_Name'])

for x in student:
    print(student[x])

student1 = {}
number_of_students = int(input("please enter number of student :"))
for a in range(number_of_students):
    Student_Number = input("please enter your student number :")
    Student_Name = input("please enter your name :")
    Gender = input("please enter your gender :")
    graduation_status = input("Have you graduated ? :")
    student1[Student_Number] = Student_Name, Gender, graduation_status
    print(student1)

