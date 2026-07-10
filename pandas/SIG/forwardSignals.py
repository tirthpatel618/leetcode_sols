import pandas as pd

signals = pd.DataFrame({
    "symbol": ["AAPL", "AAPL", "AAPL", "MSFT", "MSFT"],
    "signal_time": [
        "2025-01-01 09:30:30",
        "2025-01-01 09:31:45",
        "2025-01-01 09:34:30",
        "2025-01-01 09:30:15",
        "2025-01-01 09:33:00",
    ],
    "signal": [1, -1, 1, 1, -1],
})

prices = pd.DataFrame({
    "symbol": ["AAPL", "AAPL", "AAPL", "AAPL", "AAPL", "AAPL",
               "MSFT", "MSFT", "MSFT", "MSFT", "MSFT"],
    "time": [
        "2025-01-01 09:30:00",
        "2025-01-01 09:31:00",
        "2025-01-01 09:32:00",
        "2025-01-01 09:35:00",
        "2025-01-01 09:36:00",
        "2025-01-01 09:40:00",
        "2025-01-01 09:30:00",
        "2025-01-01 09:31:00",
        "2025-01-01 09:34:00",
        "2025-01-01 09:38:00",
        "2025-01-01 09:40:00",
    ],
    "price": [
        100.00, 100.50, 101.00, 102.00, 101.50, 103.00,
        250.00, 251.00, 252.00, 253.00, 254.00,
    ],
})

def compute_forward_returns(signals: pd.DataFrame, prices: pd.DataFrame) -> pd.DataFrame:
    signals["signal_time"] = pd.to_datetime(signals["signal_time"])
    prices["time"] = pd.to_datetime(prices["time"])

    # Sort by time before merge_asof
    signals = signals.sort_values("signal_time")
    prices = prices.sort_values("time")

    matched = pd.merge_asof(
        signals,
        prices,
        left_on="signal_time",
        right_on="time",
        by="symbol",
        direction="forward"
    )

    matched["target_time"] = matched["signal_time"] + pd.Timedelta(minutes=5)

    matched = pd.merge_asof(
        matched.sort_values("target_time"),
        prices.sort_values("time"),
        left_on="target_time",
        right_on="time",
        by="symbol",
        direction="forward"
    )

    matched.rename(columns={
        "price_x": "entry_price",
        "time_x": "entry_time",
        "price_y": "exit_price",
        "time_y": "exit_time"
    }, inplace=True)

    matched["forward_return"] = matched["exit_price"] / matched["entry_price"] - 1
    matched["signal_pnl"] = matched["signal"] * matched["forward_return"]
    return matched

out = compute_forward_returns(signals.copy(), prices.copy())

assert len(out) == len(signals)
assert out["entry_price"].notna().all()
assert out["exit_price"].notna().all()

row = out[
    (out["symbol"] == "AAPL") &
    (out["signal_time"] == pd.Timestamp("2025-01-01 09:30:30"))
].iloc[0]

assert row["entry_time"] == pd.Timestamp("2025-01-01 09:31:00")
assert row["entry_price"] == 100.50
assert row["exit_time"] == pd.Timestamp("2025-01-01 09:36:00")
assert row["exit_price"] == 101.50

expected_return = 101.50 / 100.50 - 1
assert abs(row["forward_return"] - expected_return) < 1e-9
assert abs(row["signal_pnl"] - expected_return) < 1e-9

row = out[
    (out["symbol"] == "AAPL") &
    (out["signal_time"] == pd.Timestamp("2025-01-01 09:31:45"))
].iloc[0]

expected_return = 103.00 / 101.00 - 1
expected_pnl = -1 * expected_return

assert abs(row["forward_return"] - expected_return) < 1e-9
assert abs(row["signal_pnl"] - expected_pnl) < 1e-9