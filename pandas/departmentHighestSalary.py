import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department_salary = department.merge(employee, left_on="id",
                                        right_on="departmentId", 
                                        suffixes=["_d", "_e"])

    max_salary = department_salary.groupby("id_d")['salary'].transform('max')
    department_salary = department_salary[department_salary["salary"] == max_salary]
    columns_map = {'name_d':"Department", 'name_e':"Employee", 'salary': "Salary" }
    department_salary = department_salary.rename(columns=columns_map)
    return department_salary[["Department", "Employee", "Salary"]]