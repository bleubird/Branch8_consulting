# This code calculates the mean price for orders of a unique seller
# Use input table below tabulated with calc_revenue.py:
#all_order_items = pd.read_csv('/Users/blevins/Desktop/Branch8/tables/new_all_users_order_revenue_data.csv',sep=',')

import numpy as np

mean_price_list = []

def mean_price(all_order_items):
    unique_sellers = all_order_items['$userId'].unique()
    for i in np.arange(len(unique_sellers)):
        ut = all_order_items[all_order_items['$userId'] == all_order_items['$userId'][i]]
        mp = np.mean(ut['$price'])

        mean_price_list.append(mp)

    return mean_price_list
