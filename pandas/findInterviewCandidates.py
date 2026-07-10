import pandas as pd

def find_interview_candidates(contests: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    gold_medalists = contests.groupby("gold_medal").size().reset_index()
    gold_medalists.columns = ["user", "gold_medals"]
    gold_medalists = gold_medalists[gold_medalists["gold_medals"] >= 3]
    print(gold_medalists)

    all_medals = pd.concat([
    contests[["contest_id", "gold_medal"]].rename(columns={"gold_medal": "user_id"}),
    contests[["contest_id", "silver_medal"]].rename(columns={"silver_medal": "user_id"}),
    contests[["contest_id", "bronze_medal"]].rename(columns={"bronze_medal": "user_id"}),
    ])
    all_medals = all_medals.sort_values(["user_id", "contest_id"])
    all_medals["prev1"] = all_medals.groupby("user_id")["contest_id"].shift(1)
    all_medals["prev2"] = all_medals.groupby("user_id")["contest_id"].shift(2)
    consecutive = all_medals[
    (all_medals["contest_id"] - all_medals["prev1"] == 1) &
    (all_medals["prev1"] - all_medals["prev2"] == 1)]
    condition1 = set(consecutive["user_id"])
    condition2 = set(gold_medalists["user"])
    eligible = condition1 | condition2
    users = users[users["user_id"].isin(eligible)]
    return users[["name", "mail"]]


    
