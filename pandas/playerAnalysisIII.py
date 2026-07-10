import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    #self join to get the previous games
    df = activity.merge(activity, on='player_id', suffixes=("", "_other"))
    # only want historical data until the current date
    df = df[df["event_date_other"] <= df["event_date"]]
    res = (
        df
        .groupby(["player_id", "event_date"])
        .agg(games_played_so_far=("games_played_other", "sum"))
        .reset_index()
    )
    return res

def gameplay_analysis2(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(["player_id", "event_date"])
    activity["games_played_so_far"] = (
        activity.groupby("player_id")["games_played"].cumsum()
    )
    return activity[["player_id", "event_date", "games_played_so_far"]]
    
