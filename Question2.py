def stringInfo(strings):
    result = {}

    for s in strings:
        #Discovers the length of word
        length = len(s)

        #Determines wether the amount of letters in word are even or odd
        parity = "even" if length % 2 == 0 else "odd"

        #Sorting the two values into a dictionary
        result[s] = {
            "length": length,
            "parity": parity
        }

    return result

#Example usage
words = ["data", "science"]
print(stringInfo(words))