import pandas as pd
# data = pd.Series(['A', 'B', 'A', 'C', 'B'])
# dummies = pd.get_dummies(data)
# print(dummies)

data = {
    'Color': ['Red', 'Green', 'Blue', 'Green', 'Red']
}
df = pd.DataFrame(data)

# getting dummies and using prefix
dummies = pd.get_dummies(df['Color'], prefix='Color')
df_all = pd.concat([df, dummies], axis=1)
print("DataFrame with alll dummy columns: ")
print(df_all)
print()

# getting dummies and dropping the first category column ('Blue' in this case)
dummies = pd.get_dummies(df['Color'], drop_first=True)
df = pd.concat([df, dummies], axis=1)
print("DataFrame after dropping 'Blue': ")
print(df)