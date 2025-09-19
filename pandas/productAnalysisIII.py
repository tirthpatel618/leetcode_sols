import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    min_years = sales.groupby("product_id")["year"].min().reset_index(name="first_year")
    df = sales.merge(min_years, on="product_id", how="left")
    df = df[df["first_year"] == df["year"]]
    return df[["product_id", "first_year", "quantity", "price"]]