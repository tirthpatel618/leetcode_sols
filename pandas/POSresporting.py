'''
transaction_id, reciept time, item description, item_cost, item_quantity, order_tax, order_tip

Output - date, total_spend, highest_drossing_item

order tip can be missing. highest gross doesnt require tax or tip
'''

# first - how much money was spent on a restaurant on a given day.
# what was the highest grossing item that day

# tips and taxes also need to be grouped into one order

def roll_reciepts(df):
    # i want - transaction_id, item_total, tip, tax
    df["item_total"] = df["item_cost"] * df["item_quantity"]
    transactions = df.groupby("transaction_id").agg(
                                                reciept_time=("reciept_time", "first"),
                                                item_total=("item_total", "sum"),
                                                order_tax=("order_tax", "first"),
                                                order_tip=("order_tip", "first")
                                                ).reset_index()
    
    transactions["order_total"] = transactions["item_total"] + transactions["order_tip"].fillna(0) + transactions["order_tax"]
    #assume some sort of processing here is done so that reciept time is for that day
    daily_spend = transactions.groupby("reciept_time")["order_total"].sum().reset_index()


    #now do highest grossing
    #assume reciept_time is alr done per day
    items = df.groupby(["reciept_time", "item_description"])["item_total"].sum().reset_index()
    items = items.sort_values(["reciept_time", "item_total"], ascending=[True, False]).drop_duplicates("reciept_time", keep="first").rename(columns={"item_description": "highest_grossing_item"})[["reciept_time", "highest_grossing_item"]]
    daily_report = daily_spend.merge(items, on="reciept_time", how="inner")
    return daily_report

