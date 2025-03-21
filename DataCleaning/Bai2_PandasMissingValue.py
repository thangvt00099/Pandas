import pandas as pd
import numpy as np
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, 5],
    'D': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)
print("OriginalDatataFrame:\n", df)

# remove rows with missing values by dropna() method
# df.dropna(inplace=True)
# print("\nDrop missing values by dropna() method:\n", df)

# replace missing values by fillna() method
# df.fillna(value=0, inplace=True)
# print("\nReplace missing values by fillna() method:\n", df)

# replace missing values with mean by fillna() method
# df['A'].fillna(value=df['A'].mean(), inplace=True)
df.fillna({'A': df['A'].mean()}, inplace=True) # phiên bản pandas 3.0 đổ lên

# replace missing values with median by fillna() method
# df['B'].fillna(value=df['B'].median(), inplace=True)
df.fillna({'B': df['B'].median()}, inplace=True)

# replace missing values with mode by fillna() method
# df['C'].fillna(value=df['C'].mode()[0], inplace=True)
df.fillna({'C': df['C'].mode()[1]}, inplace=True)

print(df)