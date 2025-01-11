import pandas as pd
"""
1. Series là dữ liệu 1 chiều, có thể hiểu như 1 cột trong dataFrame
"""

print(pd.DataFrame({'A': [1, 2, 3]}))
print('=========Tạo list, tạo 1 Series với labels mặc định')
data = [10, 20, 30, 40, 50]
mySeries = pd.Series(data)
print(mySeries)
print('=========Tạo list, tạo 1 Series với labels tự định nghĩa')
a = [1, 3, 5]
mySeries1 = pd.Series(a, index=["x", "y", "z"]) # index: gán nhãn cho các dòng dữ liệu
print(mySeries1)
print('=========Tạo Dictionary, tạo 1 Series với keys của dictionary là labels tự định nghĩa')
grades = {"Semester1": 3.25, "Semester2": 3.28, "Semester3": 3.75}
my_series = pd.Series(grades)
print(my_series)
print('=========Điều chỉnh những hàng dữ liệu được in ra => sử dụng index argument')
my_series = pd.Series(grades, index=["Semester1", "Semester2"])
print(my_series)
