import pandas as pd
import numpy as np
data = {
    'Temperature': [22, 25, 32, 28, 30],
    # 'Coffee_Sales': [158, 145, np.nan, np.nan, 140],
    'Ice_Cream_Sales': [105, 120, 135, 130, 125]
}
df = pd.DataFrame(data)
print(df.corr())

# calculate correlation between Temperature and Coffee_Sales
# correlation1 = df['Temperature'].corr(df['Coffee_Sales'])
# print("With NaN values")
# print(df)
# print(f'correlation = {correlation1}')
# print()

# remove missing values
# df.dropna(inplace=True)

# calculate correlation between Temperature and Coffee_Sales
# correlation2 = df['Temperature'].corr(df['Coffee_Sales'])
# print("Without NaN values")
# print(df)
# print(f'correlation = {correlation2}')
# print()

# calculate different correlation coefficients
pearson = df['Temperature'].corr(df['Ice_Cream_Sales'])
kendall = df['Temperature'].corr(df['Ice_Cream_Sales'], method='kendall')
spearman = df['Temperature'].corr(df['Ice_Cream_Sales'], method='spearman')

print(f"Pearson's Coefficient: {pearson}")
print(f"Kendall's Coefficient: {kendall}")
print(f"Spearman's Coefficient: {spearman}")