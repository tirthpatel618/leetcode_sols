import pandas as pd

trades = pd.DataFrame({
    "trade_id": [1, 2, 3, 4, 5, 6],
    "symbol": ["AAPL", "AAPL", "MSFT", "MSFT", "TSLA", "TSLA"],
    "time": [
        "2025-01-01 09:30:00.500",
        "2025-01-01 09:30:02.500",
        "2025-01-01 09:30:01.000",
        "2025-01-01 09:30:04.000",
        "2025-01-01 09:30:03.000",
        "2025-01-01 09:30:08.000",
    ],
    "price": [100.1, 100.4, 250.2, 250.8, 700.0, 701.0],
    "quantity": [10, 20, 5, 10, 2, 3],
})

quotes = pd.DataFrame({
    "symbol": ["AAPL", "AAPL", "MSFT", "MSFT", "TSLA"],
    "time": [
        "2025-01-01 09:30:00.000",
        "2025-01-01 09:30:02.000",
        "2025-01-01 09:30:00.500",
        "2025-01-01 09:30:03.500",
        "2025-01-01 09:30:01.000",
    ],
    "bid": [100.0, 100.3, 250.0, 250.6, 699.0],
    "ask": [100.2, 100.5, 250.4, 251.0, 701.0],
})

metadata = pd.DataFrame({
    "symbol": ["AAPL", "MSFT", "TSLA"],
    "sector": ["Tech", "Tech", "Auto"],
})

def trade_quality_by_sector(trades, quotes, metadata):
    trades["time"] = pd.to_datetime(trades["time"])
    quotes["time"] = pd.to_datetime(trades["quotes"])

    trades = trades.sort_values("time")
    quotes = quotes.sort_values("time")

    matched = pd.merge_asof(
        trades, 
        quotes, 
        on="time",
        by="symbol",
        direction="backward",
        tolerance=pd.Timedelta("2s")
    )
    # Drop trades with no valid quote match
    matched = matched.dropna(subset=["bid", "ask"])

    # Derived quote/trade metrics
    matched["mid"] = (matched["bid"] + matched["ask"]) / 2
    matched["spread"] = matched["ask"] - matched["bid"]
    matched["effective_spread"] = abs(matched["price"] - matched["mid"]) / matched["mid"]
    matched["notional"] = matched["price"] * matched["quantity"]

    matched = matched.merge(
        metadata,
        on="symbol",
        how="left",
        validate="many_to_one"
    )
    matched["minute"] = matched["time"].dt.floor("min")
    result = (
        matched.groupby(["sector", "minute"], dropna=False)
        .agg(
            num_trades=("trade_id", "count"),
            total_volume=("quantity", "sum"),
            total_notional=("notional", "sum"),
            avg_effective_spread=("effective_spread", "mean"),
            avg_quoted_spread=("spread", "mean"),
        )
        .reset_index()
    )
    return result

