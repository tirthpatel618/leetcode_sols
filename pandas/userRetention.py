#schema - user_id, date, transaction_amount
#output first_purchase_month, months_since_first_purchase, retention


'''
1. find first month a user made a purchase
group cohorts of users by first month of purchase
initial purchase month is 0
'''
import pandas as pd
from pandas.testing import assert_frame_equal


df1 = pd.DataFrame({
    "user_id": [1,1,1,2,3],
    "date": pd.to_datetime([
        "2023-01-05","2023-01-20","2023-02-01","2023-01-10","2023-02-15"
    ]),
    "transaction_amount": [10,5,7,12,9]
})

df3 = pd.DataFrame({
    "user_id": [1,1,2,2,2,3,4],
    "date": pd.to_datetime([
        "2022-12-31","2023-01-01",  # user 1: first Dec 2022, returns in Jan (month1)
        "2023-01-15","2023-01-15","2023-03-01",  # user 2: dup day; first Jan; returns month2
        "2023-01-31",               # user 3: first Jan; no return
        "2023-03-15"                # user 4: first Mar
    ]),
    "transaction_amount": [5,5,7,7,9,3,2]
}).sample(frac=1, random_state=0)  # shuffle row order to ensure robustness

df2 = pd.DataFrame({
    "user_id": [10,10,10,11,11,12],
    "date": pd.to_datetime([
        "2023-05-05","2023-06-01","2023-07-01",  # user 10 first in May, returns in month1 & month2
        "2023-05-25","2023-07-03",               # user 11 first in May, returns month2
        "2023-06-15"                             # user 12 first in Jun, no returns
    ]),
    "transaction_amount": [1,1,1,1,1,1]
})

def _normalize(df):
    df = df.copy()
    df["first_purchase_month"] = pd.to_datetime(df["first_purchase_month"])
    df["retention"] = df["retention"].round(3)
    return df.sort_values(["first_purchase_month","months_since_first_purchase"]).reset_index(drop=True)

def run_case(df_in, df_expected):
    got = _normalize(user_retention(df_in))
    want = _normalize(df_expected)
    assert_frame_equal(got, want)

# build the expected DataFrames exactly as shown above
exp1 = pd.DataFrame({
    "first_purchase_month": pd.to_datetime(["2023-01-01","2023-01-01","2023-02-01"]),
    "months_since_first_purchase": [0,1,0],
    "retention": [1.000,0.500,1.000]
})

exp2 = pd.DataFrame({
    "first_purchase_month": pd.to_datetime(["2023-05-01","2023-05-01","2023-05-01","2023-06-01"]),
    "months_since_first_purchase": [0,1,2,0],
    "retention": [1.000,0.333,0.667,1.000]
})

exp3 = pd.DataFrame({
    "first_purchase_month": pd.to_datetime(["2022-12-01","2022-12-01","2023-01-01","2023-01-01","2023-03-01"]),
    "months_since_first_purchase": [0,1,0,2,0],
    "retention": [1.000,1.000,1.000,0.500,1.000]
})

def user_retention(df):
    df["tx_month"] = df["date"].values.astype("datetime64[M]").astype("datetime64[ns]")
    first = df.groupby("user_id")["tx_month"].min().rename("first_purchase_month")
    print(first)
    df = df.merge(first, on="user_id", how="left")
    # create a cohort sizes using groupby 
    # create a permonth using grpupby on both first_purchase_month, and months_after[user_id].nununique()
    #merge those left to get a retention df
    #calculate retention
    
    


def main():
    tests = False
    if tests: 
        run_case(df1, exp1)
        run_case(df2, exp2)
        run_case(df3, exp3)
        print("All tests passed")

    user_retention(df1)
