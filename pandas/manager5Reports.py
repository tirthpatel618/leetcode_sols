import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    report_counts = employee["managerId"].value_counts()
    employee["reports"] = employee["id"].map(report_counts).fillna(0).astype(int)
    employee = employee.loc[employee["reports"] >= 5]
    return employee[["name"]]


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('managerId').size().reset_index(name="count")
    df = df[df['count'] >= 5]
    managers = pd.merge(df, employee, left_on="managerId", right_on="id", how="left")
    return managers[["name"]]