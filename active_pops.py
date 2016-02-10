# Use this code to read in MongoDB users collection data and
# generate a table containing timezones, emails, user_id, and company_id for ONLY
# sellers that have logged into their account within the input 'no_login_days'.
#
# First use code 'clean_user_ids.py' to format user_id array the same as company_id array.
#
# Example, in python session:
# > users = pd.read_csv('/path_to_exported_MongoDB_users_collection/users.csv', sep=',', low_memory=False)
# > %run clean_user_ids.py
# > clean_user_ids(users._id)
#
# > %run active_pops.py
# > active_pops(u.timezone, u.email, clean_ids, u.companyId, u.loginTimestamp, 7, datatype='mongodb')
#
# running this produces table in the specified directory named 'active_email_ids_last_login_7days.csv'.
# This works for MongoDB data, but not for Mixpanel yet - 01/25/2016, 21:45
#=================================================================================================================================

from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import clean_user_ids



def active_pops(email, precleaned_user_ids, precleaned_company_id, last_logintime_array, no_login_days, datatype='mongodb'):

    # DON'T FORGET TO EDIT THE PATH BELOW TO WHERE YOU WANT YOUR NEW TABLE STORED, AND UNCOMMENT OUT!
    #path_to_tables = '/Users/home_name/tables_folder/'

    active=[]
    inactive=[]

    active_email=[]
    inactive_email=[]

    active_id=[]
    active_company_id = []

    deltadays = []
        
    # Note: if today's date stays current according to datetime.now() but the login timestamp doesn't change, the number of users that have logged in within n-days will decrease everyday!
    today = datetime.now()
    
    for ii in np.arange(len(last_logintime_array)):
               
        if datatype is 'mixpanel':
            last_login = datetime.strptime(last_logintime_array[ii],'%Y-%m-%dT%H:%M:%S')
        
        if datatype is 'mongodb':
            last_login = datetime.fromtimestamp(last_logintime_array[ii])
        
        delta = (today - last_login)
        
        if (delta.days <= no_login_days):
            active_email.append(email[ii])
            active_id.append(precleaned_user_ids[ii])
            active_company_id.append(precleaned_company_id[ii])
        
            df1 = pd.DataFrame({'$email':active_email, '$user_id':active_id, '$company_id':active_company_id})
            df1 = df1[["$email","$user_id","$company_id"]]

            df1.to_csv(path_to_tables+'active_email_ids_last_login_'+str(no_login_days)+'days.csv', header=True, cols=["$email","$user_id","$company_id"])
            print email[ii], delta.days

        

        
