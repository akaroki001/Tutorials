#creating a tuple
colors = ("red", "blue", "yellow", "green", "purple")

#printing a tuple
print(colors)
print(colors[-1])
print(colors[1:-2])

for x in colors:
    print(x)

#not immutable
colors.append("black")
print(colors)
