import pandas as pd

def detect_volume_spikes(trades):

    trades = trades.copy()
    trades["timestamp"] = pd.to_datetime(trades["timestamp"])
    trades["minute"] = trades["timestamp"].dt.floor("min")

    minute_vol = trades.groupby(["symbol", "minute"]).agg(
        volume=("quantity", "sum")
    ).reset_index()

    minute_vol = minute_vol.sort_values(["symbol", "minute"])

    #rolling avg of past 3 mins
    minute_vol["rolling_avg_prev_3_mins"] = (
        minute_vol.groupby("symbol")["volume"]
        .transform(lambda x: x.shift(1).rolling(3).mean())
    )
    # Spike flag

    minute_vol["is_spike"] = (
        minute_vol["volume"] > 2 * minute_vol["rolling_avg_prev_3_mins"]
    )
    return minute_vol