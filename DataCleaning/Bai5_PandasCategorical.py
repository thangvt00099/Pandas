import pandas as pd
data = ['red', 'blue', 'green', 'red', 'blue']

# create a categorical column by Categorical method
# categorical_data = pd.Categorical(data)
# print(categorical_data)

series1 = pd.Series(data)
# convert Pandas Series to Categorical Series by using astype() method
categorical_s = series1.astype('category')
print(categorical_s)
print()

# convert Pandas Series to Categorical Series by dtype parameter inside Series()
cat_series = pd.Series(data, dtype='category')
print(cat_series)