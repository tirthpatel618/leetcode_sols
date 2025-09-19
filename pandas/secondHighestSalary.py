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