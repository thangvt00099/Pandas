import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'Marketing', 'Marketing', 'IT'],
    'Salary': [50000, 60000, 55000, 70000]
}
df = pd.DataFrame(data)
print("Original DataFrame: \n", df)
print("\n")

# use filter() method to select columns based on condition
# filtered_df = df.filter(items=['Name', 'Salary'])
# print("Filtered DataFrame: \n", filtered_df)

# use logical operators to filter
# filtered_df = df[df['Salary'] > 55000]
# print("Filtered DataFrame:\n", filtered_df)

# use isin() method
# departments = ['Marketing', 'IT']
# filtered_df = df[df['Department'].isin(departments)]
# print("Filtered DataFrame:\n", filtered_df)

# use str accessor
# filtered_df = df[df['Department'].str.contains("R", case=False)]
# print("Filtered DataFrame:\n", filtered_df)

# use query() method - method most flexible
filtered_df = df.query('Salary > 55000 and Department == "Marketing"')
print("Filtered DataFrame:\n", filtered_df)