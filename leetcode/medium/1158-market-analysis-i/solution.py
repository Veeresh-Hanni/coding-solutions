import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    # Filter orders from 2019
    orders_2019 = orders[
        orders['order_date'].dt.year == 2019
    ]

    # LEFT JOIN Users with filtered Orders
    result = users.merge(
        orders_2019,
        how='left',
        left_on='user_id',
        right_on='buyer_id'
    )

    # Group by user and count orders
    result = (
        result.groupby(['user_id', 'join_date'], as_index=False)
        .agg(orders_in_2019=('order_id', 'count'))
        .rename(columns={'user_id': 'buyer_id'})
    )

    return result