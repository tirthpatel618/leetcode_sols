import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.sort_values(by="event_date", ascending=True)
    df = df.drop_duplicates(subset = "player_id", keep="first").sort_values(by="player_id")
    df = df.rename(columns={"event_date":"first_login"})
    return df[["player_id", "first_login"]]