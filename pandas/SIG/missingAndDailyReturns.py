import pandas as pd

prices = pd.DataFrame({
    "date": [
        "2025-01-01", "2025-01-02", "2025-01-04",
        "2025-01-01", "2025-01-03", "2025-01-04",
    ],
    "symbol": ["AAPL", "AAPL", "AAPL", "MSFT", "MSFT", "MSFT"],
    "close": [100, 102, 104, 250, 252, 253],
})

weights = pd.DataFrame({
    "date": ["2025-01-01", "2025-01-01", "2025-01-03", "2025-01-03"],
    "symbol": ["AAPL", "MSFT", "AAPL", "MSFT"],
    "weight": [0.6, 0.4, 0.5, 0.5],
})

def compute_daily_returns(prices: pd.DataFrame, weights: pd.DataFrame) -> pd.DataFrame:
    prices["date"] = pd.to_datetime(prices["date"])
    weights["date"] = pd.to_datetime(weights["date"])

    dates = pd.DataFrame({
        "date": pd.date_range("2025-01-01", "2025-01-04", freq="D")
    })

    symbols = pd.DataFrame({
        "symbol": ["AAPL", "MSFT"]
    })

    grid = dates.merge(symbols, how="cross")

    price_panel = grid.merge(prices, on=["date", "symbol"], how="left")
    price_panel = price_panel.sort_values(["symbol", "date"])
    price_panel["close"] = price_panel.groupby("symbol")["close"].ffill() #important to ffil per symbol

    price_panel["return"] = (
        price_panel.groupby("symbol")["close"]
        .pct_change()
    )

    weight_panel = grid.merge(weights, on=["date", "symbol"], how="left")
    weight_panel = weight_panel.sort_values(["symbol", "date"])
    weight_panel["weight"] = weight_panel.groupby("symbol")["weight"].ffill().fillna(0) #important to ffil per symbol

    combined = price_panel.merge(
        weight_panel,
        on=["date", "symbol"], 
        how="left"
    )

    combined["weighted_return"] = combined["return"] * combined["weight"]
    portfolio = (
        combined.groupby("date")
        .agg(portfolio_return=("weighted_return", "sum"))
        .reset_index()
    )

    portfolio["cumulative_return"] = (
        (1 + portfolio["portfolio_return"]).cumprod() - 1
    )
    print(portfolio)

    return portfolio, combined

compute_daily_returns(prices, weights)

    

    