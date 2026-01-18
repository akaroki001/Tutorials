#Create a list that can store different values
House = ['name', 3, 'nairobi', True]

#print items from a list / slice

print(House)
print(House[1:3])
print(House[0:-1])

#Loop through the list
for x in House:
    print(x)

#add item in the list
House.append("lease")
print(House)

#remove item from the list
House.remove(3)
print(House)
#assignment explore how to sort and join lists
