import pandas as pd

trades = pd.DataFrame({
    "symbol": ["AAPL", "AAPL", "AAPL", "MSFT", "MSFT", "MSFT"],
    "time": [
        "2025-01-01 09:30:00.500",
        "2025-01-01 09:30:02.000",
        "2025-01-01 09:30:04.000",
        "2025-01-01 09:30:01.000",
        "2025-01-01 09:30:03.000",
        "2025-01-01 09:30:06.000",
    ],
    "trade_price": [100.10, 100.25, 100.40, 250.10, 250.30, 250.80],
    "quantity": [50, 100, 75, 40, 60, 100],
})

quotes = pd.DataFrame({
    "symbol": ["AAPL", "AAPL", "AAPL", "MSFT", "MSFT", "MSFT"],
    "time": [
        "2025-01-01 09:30:00.000",
        "2025-01-01 09:30:01.500",
        "2025-01-01 09:30:03.500",
        "2025-01-01 09:30:00.500",
        "2025-01-01 09:30:02.500",
        "2025-01-01 09:30:05.000",
    ],
    "bid": [100.00, 100.20, 100.35, 250.00, 250.20, 250.70],
    "ask": [100.20, 100.30, 100.45, 250.20, 250.40, 250.90],
})


def match_trades_to_quotes(trades: pd.DataFrame, quotes: pd.DataFrame):
    #convert time columsn to datetime
    trades["time"] = pd.to_datetime(trades["time"])
    quotes["time"] = pd.to_datetime(quotes["time"])

    # sort the columns by time before merge_asof
    trades = trades.sort_values("time")
    quotes = quotes.sort_values("time")

    matched = pd.merge_asof(
        trades,
        quotes, 
        on="time",
        by="symbol",
        direction="backward",
        tolerance=pd.Timedelta("1s")
    )

    matched["mid"] = (matched["bid"] + matched["ask"]) / 2
    matched["spread"] = matched["ask"] - matched["bid"]

    matched["effective_spread"] = abs(matched["trade_price"] - matched["mid"]) / matched["mid"]
    
    return matched

out = match_trades_to_quotes(trades.copy(), quotes.copy())

assert len(out) == len(trades)

assert out["bid"].notna().all()

assert out["ask"].notna().all()

# First AAPL trade should match first AAPL quote

first = out[(out["symbol"] == "AAPL") & (out["time"] == pd.Timestamp("2025-01-01 09:30:00.500"))].iloc[0]

assert first["bid"] == 100.00

assert first["ask"] == 100.20

# First MSFT trade should match first MSFT quote

msft_first = out[(out["symbol"] == "MSFT") & (out["time"] == pd.Timestamp("2025-01-01 09:30:01.000"))].iloc[0]

assert msft_first["bid"] == 250.00

assert msft_first["ask"] == 250.20


