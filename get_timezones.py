# This code is not quite working yet!

import numpy as np


def get_timezones(active_user_list, all_user_order_list):

    index = np.where( all_user_order_list.userId == active_user_list['$company_id'])
    one_zone = active_user_list['$timezone'][index]

    return one_zone
    
