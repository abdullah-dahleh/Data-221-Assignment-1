#This function takes a value X to the power of Y
def power(x, y):
    return x ** y

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
results = []

#Looping through each pair using argument unpacking
for x, y in pairs:
    #Skipping pairs where the exponent (Y) is negative
    if y < 0:
        continue

    #Storing all valid results in a list
    results.append(power(x, y))

print(results)