import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs = logs.sort_values("id")

    # Step 2: find consecutive streaks
    # Compare current num with shifted values
    cond = (logs["num"] == logs["num"].shift(1)) & (logs["num"] == logs["num"].shift(2))

    # Step 3: filter and get unique numbers
    result = logs.loc[cond, ["num"]].drop_duplicates()
    result = result.rename(columns={"num": "ConsecutiveNums"})
    return result
