#welcome to python
#inputs, outputs and variables

#outputs
print("welcome to python")

# variables and outputs in python
name = input("please enter your name")
color = input("please enter your favourite color")
print("welcome" + name + "Your favourite color is " + color)
print("===================================================")

#converting strings in integers
y_o_b = input("please enter the year of birth")
Age = 2024 - int(y_o_b)
print(Age)

#============================================
#printing a multi line statements
Today = "'Monday','May','2024'"
print(Today)
verses = ''' Oh God of all creation
Let this be our land and nation
Justice be our shield and defender
May we dwell in unity peace and liberty
'''
print(verses)

#===========================================

#slicing strings in python
country="East Africa Community"
print(country[0])
print(country[:])
print(country[0:-1])
print(country[0:11])
print(country[1:13])

# using formatted strings
first = "Tom"
second = "Mboya"
message = f'my first name is {first}, my second name is {second}, welcome to [Nairobi] '
print(message)
