import pandas as pd
continent = ['Asia', 'Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Europe',
             'North America', 'North America', 'North America']
country = ['China', 'India', 'Japan', 'Nepal', 'France', 'Germany', 'United Kingdom',
           'Canada', 'Mexico', 'United States']
population = [1439323776, 1380004385, 126476461, 29136808, 65273511, 83783942, 67886011,
              37742154, 128932753, 331002651]

index_array = [continent, country]

# tạo multiindex từ array
multi_index = pd.MultiIndex.from_arrays(index_array, names=['Continent', 'Country'])

# tạo dataframe sử dụng multiindex
df = pd.DataFrame({'Population': population}, index=multi_index)
print(df)