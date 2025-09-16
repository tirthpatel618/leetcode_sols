import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(["salary"])

    if len(employee["salary"].unique()) < 2:
        return pd.DataFrame({"SecondHighestSalary": [np.NaN]})
    
    employee = employee.sort_values("salary", ascending=False)

    employee.drop("id", axis=1, inplace=True)

    employee.rename({"salary": "SecondHighestSalary"}, axis=1, inplace=True)

    return employee.head(2).tail(1)

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    #only merge the employees who have managers. ManagerId as null will not be merged
    df = employee.merge(employee, left_on = 'managerId', right_on = 'id',
            suffixes = ['_e', '_m'], how = 'inner')
    
    df = df.loc[df['salary_e'] > df['salary_m'] , ['name_e']]
    return df.rename(columns = {'name_e':'Employee'})

data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})



import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    df = insurance.assign(
       tiv_2015_cnt = insurance.groupby('tiv_2015')['pid'].transform('count'), loc_cnt = insurance.groupby(['lat', 'lon'])['pid'].transform('count'))
    
    df = df[(df['tiv_2015_cnt'] > 1) & (df['loc_cnt'] == 1)]
    
    return df.agg(tiv_2016 = ('tiv_2016', 'sum')).round(2)
data = [[1, 10, 5, 10, 10], [2, 20, 20, 20, 20], [3, 10, 30, 20, 20], [4, 10, 40, 40, 40]]
insurance = pd.DataFrame(data, columns=['pid', 'tiv_2015', 'tiv_2016', 'lat', 'lon']).astype({'pid':'Int64', 'tiv_2015':'Float64', 'tiv_2016':'Float64', 'lat':'Float64', 'lon':'Float64'})

print(find_investments(insurance))