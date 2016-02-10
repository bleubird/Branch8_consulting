import numpy as np
import pandas as pd
import re
import csv
import sys 

# Below are active user and all_user_order data sets
#a = pd.read_csv('/Users/blevins/Desktop/Branch8/tables/active_email_ids_last_login_9days.csv', sep=',') # this is active_user_list
#o = pd.read_csv('/Users/blevins/Desktop/Branch8/raw_MongoDB_data/orders_lite.csv',sep=',', low_memory=False) # this is all_user_order_list

# Compare short list of active user ids
# with a long list of all (active and inactive) user ids -
# return subset_of_all_users that is connected to their associated orders!

def find_active_user_orders(active_user_list, all_user_order_list):
    
    active_ids               = active_user_list['$company_id']
    is_active                = all_user_order_list.userId.apply(lambda x: x in active_ids.tolist())

    subset_of_all_users      = all_user_order_list.userId[is_active==True]
    subset_of_all_orderItems = all_user_order_list.orderItems[is_active==True]

    df = pd.DataFrame({'$company_id':subset_of_all_users, '$orderItems':subset_of_all_orderItems})
    df = df[["$company_id","$orderItems"]]

    df.to_csv('/Users/blevins/Desktop/Branch8/tables/active_user_orders.csv', header=True, cols=["$company_id","$orderItems"])


    
