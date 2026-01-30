import math

#This function compares the areas of two circles
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # Validate that both inputs are positive integers
    if not isinstance(radiusOfCircle1, int) or not isinstance(radiusOfCircle2, int):
        return "Radii must be integers."
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Radii must be positive."

    #Calculate the areas of both circles
    area1 = math.pi * radiusOfCircle1 ** 2
    area2 = math.pi * radiusOfCircle2 ** 2

    #Determine smaller and larger areas
    smallerArea = min(area1, area2)
    largerArea = max(area1, area2)

    #Calculating the percentage coverage
    percentage = (smallerArea / largerArea) * 100
    return percentage


#Example usage
print(circleAreaCoverage(6, 20))