# pylint: disable=missing-docstring

"""

In This Program Included All User Authentication Routes And Related Functions
This Program Is For Views Of All Login Related  And It Defines The App Login,Logout Routes

"""


# # Import All Necessary Packages

# import os
# import ast
# import random
# import requests
# import razorpay

# razorpay_client = razorpay.Client(auth=("rzp_test_vXNpZ400THkdfq", "l2Thg4SobcLRWZW08vyJ3Syw"))

# from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, current_app, make_response, session
# from collections import Counter
# from pprint import pprint
# from datetime import datetime, timedelta, date



# # API URL assign
# API_URL_tenant = 'http://127.0.0.1:8001'
# API_URL_consumer = 'http://127.0.0.1:8000'


# function for home page
def home_page(Page_id, tenant_id, company_id, visit_id, API_URL_tenant, API_URL_consumer):


    pg_compnt_list1 = requests.get('%s/API_bussiness/get_och_page_component_data'
                                    % API_URL_consumer, params={'Page_id':Page_id})
    page_compnt_list1 = pg_compnt_list1.json()
    # print(page_compnt_list1[0])

    product_list = requests.get('%s/API_bussiness/get_pdt_data'
                            % API_URL_tenant, params={'tenant_id':tenant_id, 'company_id':company_id})
    product_data_list = product_list.json()
    # print("product_data_list:", product_data_list)

    cart_product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={'visit_id' :visit_id,'tenant_id' : tenant_id})
    
    cart_product_list = cart_product_list.json()

    collection_list = requests.get('%s/API_bussiness/get_prd_collection_master_data'
                            % API_URL_tenant, params={'tenant_id':tenant_id, 'company_id':company_id})
    collection_data_list = collection_list.json()
    return page_compnt_list1, product_data_list, cart_product_list, collection_data_list


def hello_word():
    print("hello world")
