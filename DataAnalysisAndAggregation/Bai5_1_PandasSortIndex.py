import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'John'],
    'Age': [28, 22, 25, 30, 24]
}
df = pd.DataFrame(data, index=[2, 0, 1, 4, 3])
print("Original DataFrame:\n", df.to_string(index=True))
print()

# sort DataFrame by index in ascending order
sorted_df = df.sort_index()
print("Sorted DataFrame by index:\n", sorted_df.to_string(index=True))
