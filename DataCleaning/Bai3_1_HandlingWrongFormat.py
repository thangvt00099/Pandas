import pandas as pd
data = {
    'Name': ['John', 'Michael', 'Tom', 'Alex', 'Ryan'],
    'Age': [8, 9, 7, 80, 100],
    'Gender': ['M', 'M', 'M', 'F', 'M'],
    'Standard': [3, 4, 12, 3, 5]
}
df = pd.DataFrame(data)

# replace F with M
df.loc[3, 'Gender'] = 'M'
print(df)
print()

# replace values based on conditions
for i in df.index:
    age_val = df.loc[i, 'Age']
    if (age_val > 14) and (age_val % 10 == 0):
        df.loc[i, 'Age'] = age_val // 10
print(df)
print()

# remove wrong values
for i in df.index:
    if df.loc[i, 'Standard'] > 8:
        df.drop(i, inplace=True)
print(df)