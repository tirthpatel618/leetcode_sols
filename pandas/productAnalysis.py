import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    quantities = sales.groupby("product_id")["quantity"].sum().reset_index()
    return quantities.rename(columns={"quantity":"total_quantity"})