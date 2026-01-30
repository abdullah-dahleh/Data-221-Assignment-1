import pandas as pd

#Creating the initial data dictionary
data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

#Creating the DataFrame
df = pd.DataFrame(data)

#Add a new column derived from existing columns
df["D"] = df["A"] * df["C"]

#Print the final DataFrame
print(df)