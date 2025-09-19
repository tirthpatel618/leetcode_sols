import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, how="left", on="product_id")
    return df[["product_name", "year", "price"]]