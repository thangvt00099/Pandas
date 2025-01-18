import pandas as pd
data = [2, 4, 6, 8]
array1 = pd.array(data)
print(array1)
print("=========================")

int_array = pd.array([1, 2, 3, 4], dtype='int')
print(int_array)
print("=========================")

float_array = pd.array([1.1, 2.2, 3.3, 4.4], dtype='float')
print(float_array)
print("=========================")

string_array = pd.array(['apple', 'banana', 'cherry', 'date'], dtype='str')
print(string_array)
print("=========================")

bool_array = pd.array([True, False, True, False], dtype='bool')
print(bool_array)
print("=========================")

# Tạo series từ pandas
arr = pd.array([18, 20, 19, 21, 22])
arr_series = pd.Series(arr)
print(arr_series)