# pylint: disable=missing-docstring

"""

In This Program Included All User Authentication Routes And Related Functions
This Program Is For Views Of All Login Related  And It Defines The App Login,Logout Routes

"""


# Import All Necessary Packages

import os
import ast
import random
import requests
import razorpay

razorpay_client = razorpay.Client(auth=("rzp_test_vXNpZ400THkdfq", "l2Thg4SobcLRWZW08vyJ3Syw"))

from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, current_app, make_response, session
from collections import Counter
from pprint import pprint
from datetime import datetime, timedelta, date



# # API URL assign
# API_URL_tenant = 'http://127.0.0.1:8001'
# API_URL_consumer = 'http://127.0.0.1:8000'


# function for home page
def send_message(tenant_id, company_id, API_URL_consumer, API_URL_tenant, user_id):


    
    return page_compnt_list1, product_data_list, cart_product_list, collection_data_list
