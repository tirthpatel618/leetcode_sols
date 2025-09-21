'''
ticker, date, price (input)

ticker, date, return 

add a columnn 1-week forward
fill holes in the data. Add rows with no days with the previous days price
give em
add a column "wkfwd price" (how?? has to match the ticker and date)
    df["price_after] = df.groupby("ticker")["price].shift(-7)

compute return (wkfwd - price) / price




'''