import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    activity['day_before_event'] = activity["event_date"] - pd.Timedelta(days=1)

    df = activity.merge(first_login, on="player_id", suffixes=["_actual", "_first"])
    #find the rows where the actual event date matches the day after the first login date
    consecutive_login = df[df['day_before_event'] == df['event_date_first']]

    fraction = round(consecutive_login["player_id"].nunique() / activity['player_id'].nunique(), 2)

    output = pd.DataFrame({"fraction": [fraction]})

    return output
