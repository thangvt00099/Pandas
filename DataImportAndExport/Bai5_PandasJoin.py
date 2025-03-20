import pandas as pd
data1 = {
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
}
df1 = pd.DataFrame(data1, index=['K0', 'K1', 'K2', 'K3'])

data2 = {
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}
df2 = pd.DataFrame(data2, index=['K0', 'K1', 'K2', 'K3'])

# join dataframes
df_join = df1.join(df2)
print("DataFrame 1: \n", df1)
print("\nDataFrame 2: \n", df2)
print("\nJoined DataFrame: \n", df_join)
print("========================================================")

data3 = {
    'EmployeeID': ['E001', 'E002', 'E003', 'E004', 'E005'],
    'Name': ['John Doe', 'Jane Smith', 'Peter Brown', 'Tom Johnson', 'Rita Patel'],
    'DeptID': ['D001', 'D003', 'D001', 'D002', 'D006'],
    'DeptName': ['Sales1', 'Admin1', 'Sales1', 'HR1', 'N/A']
}
employees = pd.DataFrame(data3)

data4 = {
    'DeptID': ['D001', 'D002', 'D003', 'D004'],
    'DeptName': ['Sales2', 'HR2', 'Admin2', 'Marketing2']
}
departments = pd.DataFrame(data4)
# set DeptID as index because join method can only join 2 DataFrame by index
departments = departments.set_index('DeptID')

df_join1 = employees.join(departments, on='DeptID', lsuffix='_left', rsuffix='_right')
print(df_join1)
