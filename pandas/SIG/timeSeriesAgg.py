import pandas as pd

trades = pd.DataFrame({
    "symbol": ["AAPL", "AAPL", "AAPL", "AAPL", "MSFT", "MSFT", "MSFT"],
    "timestamp": [
        "2025-01-01 09:30:00.100",
        "2025-01-01 09:30:20.500",
        "2025-01-01 09:31:05.000",
        "2025-01-01 09:31:45.000",
        "2025-01-01 09:30:10.000",
        "2025-01-01 09:30:50.000",
        "2025-01-01 09:32:00.000",
    ],
    "price": [100.00, 100.20, 100.50, 100.40, 250.00, 250.50, 251.00],
    "quantity": [10, 20, 15, 10, 5, 15, 20],
})

def minute_trade_summary(trades: pd.DataFrame) -> pd.DataFrame:
    trades["timestamp"] = pd.to_datetime(trades["timestamp"])
    trades["min"] = trades["timestamp"].dt.floor("min")

    summary = trades.groupby(["symbol", "min"]).agg(
        num_trades=("price", "count"), 
        total_volume=("quantity", "sum"),
        avg_price=("price", "mean")
    ).reset_index()

    summary["notional"] = summary["total_volume"] * summary["avg_price"]
    summary["vwap"] = summary["notional"] / summary["total_volume"]
    print(summary)
    return summary

minute_trade_summary(trades)

def make_ohlcv_bars(trades: pd.DataFrame) -> pd.DataFrame:
    trades["timestamp"] = pd.to_datetime(trades["timestamp"])
    trades["min"] = trades["timestamp"].dt.floor("min")



    trades = trades.sort_values(["symbol", "timestamp"])

    ohlcv = trades.groupby(["symbol", "min"]).agg(
        open=("price", "first"),
        high=("price", "max"),
        low=("price", "min"),
        close=("price", "last"),
        volume=("quantity", "sum")
    ).reset_index()

    print(ohlcv)
    return ohlcv

make_ohlcv_bars(trades)

