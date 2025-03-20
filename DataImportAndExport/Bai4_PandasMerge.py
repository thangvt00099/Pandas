import pandas as pd
data1 = {
    'EmployeeID': ['E001', 'E002', 'E003', 'E004', 'E005'],
    'Name': ['John Doe', 'Jane Smith', 'Peter Brown', 'Tom Johnson', 'Rita Patel'],
    'DeptID1': ['D001', 'D003', 'D001', 'D002', 'D006']
}
employees = pd.DataFrame(data1)

data2 = {
    'DeptID2': ['D001', 'D002', 'D003', 'D004'],
    'DeptName': ['Sales', 'HR', 'Admin', 'Marketing']
}
departments = pd.DataFrame(data2)
# Merge DataFrames Employees and Departments
df_merge = pd.merge(employees, departments, left_on='DeptID1', right_on='DeptID2', sort=True)
print(df_merge)