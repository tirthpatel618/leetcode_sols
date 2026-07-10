import pandas as pd

trades = pd.DataFrame({
    "trade_id": [1, 2, 3, 4, 5],
    "symbol": ["AAPL", "AAPL", "MSFT", "TSLA", "MSFT"],
    "timestamp": [
        "2025-01-01 09:30:01",
        "2025-01-01 09:30:02",
        "2025-01-01 09:30:03",
        "2025-01-01 09:30:04",
        "2025-01-01 09:30:05",
    ],
    "price": [100, 101, 250, 700, 251],
    "quantity": [10, 20, 5, 2, 10],
})

metadata = pd.DataFrame({
    "symbol": ["AAPL", "MSFT"],
    "sector": ["Technology", "Technology"],
    "exchange": ["NASDAQ", "NASDAQ"],
})

def attach_metadata(trades: pd.DataFrame, metadata: pd.DataFrame) -> pd.DataFrame:
    out = trades.merge(metadata, on="symbol", how="left", validate="many_to_one")
    out["notional"] = out["price"] * out["quantity"]
    sector_summary = out.groupby("sector", dropna=False).agg(
        total_notional=("notional", "sum"),
    ).reset_index()

    return out, sector_summary
