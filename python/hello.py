import math

# variables and outputs in python

print("welcome to python")
name = input("please enter your name")
color = input("please enter your favourite color")
print("welcome" + name + "Your favourite color is " + color)
print("===================================================")
#converting strings in integers
d_o_b = input("please enter the date of birth")
Age = 2024 - int(d_o_b)
print(Age)

#begin
#printing a multi line statements
Today="'Monday','May','2024'"
print(Today)
verses =''' Oh God of all creation
Let this be our land and nation
Justice be our shield and defender
May we dwell in unity peace and liberty
'''
print(verses) 

#end

#slicing strings in python
country="East Africa Community"
print(country[0])
print(country[:])
print(country[0:-1])
print(country[0:5])
print(country[1:13])

# using formatted strings
first = "Tom"
second = "Mboya"
message = f'my first name is {first}, my second name is {second}, welcome to [Nairobi] '
print(message)

"""
#methods in strings
course = "bachelor of technology in business information technology"
print(len(course))
print(course.upper())
print(course.lower())
president = "Emilio Mwai Kibaki"
print(president.find('Mwai'))
print(president.replace('Emilio','Stanley'))
print('Mwai' in president)
"""
"""
#Integers arithmetic

print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)
print(5 % 3)

x = 20
x = 3 + x
print(x)

y = 50
y -= 50 + y
print(y)

# operator precedence
x = 5 + 7 * 4
print(x)
y = (5+7) * 4
print(y)

# maths built-in functions
x = 28.983
print(round(x,2))

#import math class to access more methods
x=25
z=7
print(math.sqrt(x))
print(math.pow(z,2))
"""
#decision making in python
#example rent rates
# pay rent per  year rent is ksh 40,000
# pay rent per 6 months rent is ksh 50,000
# pay rent per 3 months rent is ksh 60, 000
# pay rent per month rent is ksh 70,000
# program

x = input("indicate the duration you will pay rent in months")
if x == '12':
    print("Total rent :40000 ")
elif x == '6':
    print("Total rent :50000 ")
elif x == '3':
    print("Total rent :60000")
elif x == '1':
    print("Total rent :70000")

print("welcome to ark apartment")


