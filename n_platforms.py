
# This code calculates the number of platforms (marketplaces) of a unique seller.
# Use input table below tabulated with calc_revenue.py:
#all_order_items = pd.read_csv('/Users/blevins/Desktop/Branch8/tables/new_all_users_order_revenue_data.csv',sep=',')

import numpy as np

n_platform_list = []

def n_platforms(all_order_items):
    unique_sellers = all_order_items['$userId'].unique()
    for i in np.arange(len(unique_sellers)):
        ut = all_order_items[all_order_items['$userId'] == all_order_items['$userId'][i]]
        pl = len(ut['$platform'].unique())

        n_platform_list.append(pl)

    return n_platform_list
