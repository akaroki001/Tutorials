
student = {}
number_of_students = int(input("please enter number of students to record :"))
for a in range(number_of_students):
    Student_Number = input("please enter your student number :")
    Student_Name = input("please enter your name :")
    Total_cat = int(input("please enter the total cat marks :"))
    final_exam = int(input("please enter the final_exam:"))
    total_exam = Total_cat + final_exam
    student[Student_Number] = Student_Name, Total_cat, final_exam , total_exam
    print(student)
