threshold = 100
product = 1
currentNumber = 1

while product <= threshold:
    product *= currentNumber
    currentNumber += 1

#CurrentNumber - 1 caused the product to exceed the threshold
print("Final product:", product)
print("Integer that caused exceed:", currentNumber - 1)