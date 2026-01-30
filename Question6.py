#This function calculates cumulative percentages for each unique value
def distributionAnalysis(numbers):
    result = {}
    totalCount = len(numbers)

    #Loop through sorted unique values
    for value in sorted(set(numbers)):
        count = 0

        #Count how many numbers are less than or equal to the current value
        for n in numbers:
            if n <= value:
                count += 1

        #Store percentage in the dictionary
        result[value] = (count / totalCount) * 100

    return result


#Example usage
numbers = [3, 1, 2, 3, 4, 2]
print(distributionAnalysis(numbers))