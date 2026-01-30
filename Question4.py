from random import random


values = [random() for i in range(20)]
x = random()


#Using the .sort() function to sort all values in the list from smallest to greatest
values.sort()

#Finding indices where values are greater than or equal to x
matchingIndices = []

for i in range(len(values)):
    if values[i] >= x:
        matchingIndices.append(i)

print("Sorted values:", values)
print("x:", x)

#Printing the first matching index if it exists
if matchingIndices:
    print("First matching index:", matchingIndices[0])
else:
    print("No values greater than or equal to x")