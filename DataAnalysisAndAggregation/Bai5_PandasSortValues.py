import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'John'],
    'Age': [28, 22, 25, 30, 25],
    'Score': [85, 90, 75, 80, 92]
}
df = pd.DataFrame(data)

# sort DataFrame by Age in ascending order
# sorted_df = df.sort_values(by='Age')
# print(sorted_df.to_string(index=False))

# 1. Sort DataFrame by 'Age' and then by 'Score' (ascending order)
df1 = df.sort_values(by=['Age', 'Score'])
print("Sorting by 'Age' (ascending) and then by 'Score' (ascending):\n", df1.to_string(index=False))
print()

# 2. Sort DataFrame by 'Age' in ascending order, and then by 'Score' in descending order
df2 = df.sort_values(by=['Age', 'Score'], ascending=[True, False])
print("Sorting by 'Age' (ascending) and then by 'Score' (descending):\n", df2.to_string(index=False))
print()

ages = pd.Series([28, 22, 25], name='Age')
# sort Series in ascending order
sorted_ages = ages.sort_values()
print(sorted_ages.to_string(index=False))