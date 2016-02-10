
import numpy as np
import pandas as pd
import re
import csv
import sys
import json
import requests


# Below are the tables to be read for input to hte calc_revenue function:
# (I read already generated a list of orders for the active users only by running 'find_active_user_orders.py', read it in)
#all_orders_list = pd.read_csv('/Users/blevins/Desktop/Branch8/tables/all_user_orders_with_activity.csv', sep=',')


def calc_revenue(all_orders_list, currency='USD'):
    
    all_orderItems      = all_orders_list['$orderItems']
    all_order_companyId = all_orders_list['$company_id']
    all_order_activity  = all_orders_list['$is_active']
    all_order_timezone  = all_orders_list['$timezone']

    price_list         = []
    tax_list           = []
    discount_list      = []
    quantity_list      = []
    platform_list      = []
    orderId_list       = []
    orderItemId_list   = []
    userId_list        = []
    sku_list           = []
    priceCurrency_list = []
    timezone_list      = []

    active_list        = []

    for i in np.arange(len(all_orderItems)):

        test = json.loads(all_orderItems[i])
        
        for item in test:
            key = '$numberLong'

            try:
                price         = item['price']['$numberLong']
                price         = float(price)
                quantity      = item['quantity']
                platform      = item['platform']
                orderId       = item['orderId']
                orderItemId   = item['orderItemId']
                userId        = item['userId']
                sku           = item['sku']
                priceCurrency = item['priceCurrency']


                # The commented-out stuff below goes online and finds the current currency converstion rate
                # to convert currency to USD, RMB, CNY - PROBLEM IS THAT IT TAKES A LOOOOOOONG TIME TO RUN...
                #if currency == 'USD':
                #    url = ('https://currency-api.appspot.com/api/%s/%s.json') % (priceCurrency, 'USD')

                #if currency == 'RMB':
                #    url = ('https://currency-api.appspot.com/api/%s/%s.json') % (priceCurrency, 'RMB')

                #if currency == 'CNY':
                #    url = ('https://currency-api.appspot.com/api/%s/%s.json') % (priceCurrency, 'RMB')

                #r = requests.get(url)
                #conversion_rate = r.json()['rate']

                
                # So instead the conversion rate is hardcoded in - not ideal but saves 5 hours of CPU time!
                if priceCurrency == 'CLP':
                    conversion_rate = 0.0014

                if priceCurrency == 'CNY':
                    conversion_rate = 0.15

                if priceCurrency == 'RMB':
                    conversion_rate = 0.15

                if priceCurrency == 'COP':
                    conversion_rate = 0.00029

                if priceCurrency == 'IDR':
                    conversion_rate = 0.000073

                if priceCurrency == 'MXN':
                    conversion_rate = 0.054

                if priceCurrency == 'MYR':
                    conversion_rate = 0.24

                if priceCurrency == 'NGN':
                    conversion_rate = 0.0050   

                if priceCurrency == 'PAB':
                    conversion_rate = 1.0

                if priceCurrency == 'PEN':
                    conversion_rate = 0.29

                if priceCurrency == 'PHP':
                    conversion_rate = 0.021

                if priceCurrency == 'SGD':
                    conversion_rate = 0.70

                if priceCurrency == 'THB':
                    conversion_rate = 0.028

                if priceCurrency == 'VND':
                    conversion_rate = 0.000045

                if priceCurrency == 'USD':
                    conversion_rate = 1

                if priceCurrency == 'NaN':
                    conversion_rate = 1
                    

                price_usd = price*conversion_rate
            
                price_list.append(price_usd) 
                quantity_list.append(quantity)
                platform_list.append(platform)
                orderId_list.append(orderId)
                orderItemId_list.append(orderItemId)
                userId_list.append(userId)
                sku_list.append(sku)
                priceCurrency_list.append(priceCurrency)
                active_list.append(all_order_activity[i])
                timezone_list.append(all_order_timezone[i])

                revenue = price_usd*quantity
                revenue_list.append(revenue)

                print price, conversion_rate, price_usd
                
            except (RuntimeError, TypeError, NameError):
                pass
        

    all_users_order_revenue_data = pd.DataFrame({'$is_active':active_list, '$userId':userId_list,'$price':price_list, '$quantity':quantity_list, '$priceCurrency':priceCurrency_list, '$platform':platform_list})

    
    all_users_order_revenue_data.to_csv('/Users/blevins/Desktop/Branch8/tables/new_all_users_order_revenue_data.csv')
