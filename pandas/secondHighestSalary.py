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

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    #edge cases - either only 0 or 1 people in df - return None
    #salaries aren't distinct. 100 salaries that are all the same. 
    #no clue what to do if there is 1 salary 50, then 4 salaries 50

    #at some points we will drop duplicates so it will be chill probably 

    #in order to slice for highest and lowest and if you want it to be a df, you need to do head and tail

    salaries = employee[["salary"]].drop_duplicates().sort_values(by="salary", ascending=False)
    if len(salaries) >= 2:
        return pd.DataFrame({"SecondHighestSalary": salaries.iloc[1]})
    else:
        return pd.DataFrame({"SecondHighestSalary": [None]})


data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})