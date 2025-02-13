# pip install openpyxl pandas

import pandas as pd

df = pd.read_excel("OrderHistory.xlsx")
df = df.sort_values(by='Order ID', ascending=True)

# Grouped oders
agg_functions = {
    'Sales Amount': 'sum',
    'Order Type'  : ', '.join,
}

grouped_df = df.groupby('Order ID').agg(agg_functions )
grouped_df.to_excel("grouped_Orderistory.xlsx")

# Only oders with multiple items
multiple_items_oders = grouped_df[grouped_df["Order Type"].str.contains(',')]
multiple_items_oders.to_excel('oders_with_multiple_items.xlsx')

