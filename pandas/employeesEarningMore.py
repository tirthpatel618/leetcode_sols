import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee,
                         left_on = 'managerId', 
                        right_on = 'id', 
                        suffixes = ['_e', '_m'], 
                        how = 'inner')
    df = df.loc[df['salary_e'] > df['salary_m'], ["name_e"]]
    return df.rename(columns = {'name_e':'Employee'})