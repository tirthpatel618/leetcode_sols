import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.sort_values(by="event_date", ascending=True)
    df = df.drop_duplicates(subset=["player_id"], keep="first")
    return df[["player_id", "device_id"]].sort_values(by="player_id")