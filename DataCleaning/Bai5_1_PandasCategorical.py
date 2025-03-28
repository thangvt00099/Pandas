import pandas as pd
data = ['A', 'B', 'A', 'C', 'B']
cat_series = pd.Series(data, dtype='category')

# using .cat accessor
# print(cat_series.cat.categories)
# print(cat_series.cat.codes)

# create a dictionary for renaming categories
# categories_mapping = {
#     "A": "Category A",
#     "B": "Category B",
#     "C": "Category C"
# }

# rename categories using .rename_categories() and recreate the Series
# cat_series_renamed = cat_series.cat.rename_categories(categories_mapping)
# print(cat_series_renamed)
# print()

# add new categories and reassign the variable
# new_categories = ['D', 'E']
# cat_series = cat_series.cat.add_categories(new_categories)
# print(cat_series)

print("Original Series: ")
print(cat_series)

# remove specific categories
categories_to_remove = ['B', 'C']
cat_series_remove = cat_series.cat.remove_categories(categories_to_remove)

print("\nModified Series: ")
print(cat_series_remove)

