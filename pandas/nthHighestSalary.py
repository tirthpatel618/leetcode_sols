import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # extract Nth highest salary, returning None when appropriate
    filtered = employee.sort_values(by='salary', ascending=False).drop_duplicates(subset='salary')
    val = None if len(filtered) < N or N < 1 else filtered.iloc[N-1]['salary']

    # synthesize new table
    data = {f'getNthHighestSalary({N})': [val]}
    return pd.DataFrame(data)