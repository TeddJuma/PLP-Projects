import pandas as pd

file = "C:\Programming\PLP Content\Python\Python\data set\Iris.csv" # replace with the path to your CSV file
df = pd.read_csv(file)
# print(df.describe())


row = df.loc[df['Id'] == 3]
print(row)

# row_index = df.loc[df['Id'] == 2].index[0]
# row_values = df.iloc[row_index]
# print(row_values)