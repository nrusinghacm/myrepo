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
def view_all_user(tenant_id, company_id, API_URL_consumer, API_URL_tenant):


    # # Getting Notification For Home Page By API
    # request_obj = requests.get('%s/API_bussiness/notification/read_user_messages/%s' %
    #                            (API_URL_consumer, current_user.user_id))
    # # Converting Response Object To JSON Data
    # data_obj = request_obj.json()

    # Getting Responce From Url
    all_user_data_object = requests.get('%s/API_bussiness/get_user_data'%API_URL_consumer)


    # Converting Response Data To Json
    all_user_data = all_user_data_object.json()

    return all_user_data

def user_create(tenant_id, company_id, API_URL_consumer, API_URL_tenant):
    # Generate enquiry Id Dynamically
    generate_user_id = requests.get('%s/API_bussiness/generate_user_id' % API_URL_consumer)

    # Convert In Json
    user_id1 = generate_user_id.json()



    # Get Today's Date
    StartDate = datetime.now()
    StartDate = StartDate.date()


    # All Companys Data For Dropdawn
    company_data_obj = requests.get('%s/API_bussiness/get_company_data_by_type' % API_URL_consumer)

    # Convert In Json
    company_data = company_data_obj.json()

    return user_id1, company_data

def save_user(tenant_id, company_id, API_URL_consumer, API_URL_tenant, user_id):

    # Getting data from Form
    user_id = user_id
    email = request.form['ui_email']
    email_confirmed_at = StartDate
    username = request.form['ui_username']
    password = request.form['ui_username']
    phone_number = request.form['ui_phone_number']

    first_name = request.form['ui_first_name']
    last_name = request.form['ui_last_name']
    age = request.form['ui_age']
    gender = request.form['ui_gender']
    DoB = request.form['ui_DoB']
    city = request.form['ui_city']
    state = request.form['ui_state']
    country = request.form['ui_country']
    postal_pin = request.form['ui_postal_pin']

    # company_id = request.form['ui_company']
    company = request.form['ui_company']
    # company_type = request.form['ui_company_type']
    # company_location = request.form['ui_company_location']
    # company_territory = request.form['ui_company_territory']
    # company_region = request.form['ui_company_region']
    branch_id = request.form['ui_branch_id']
    branch_name = request.form['ui_branch_name']
    department_id = request.form['ui_department_id']
    department_name = request.form['ui_department_name']


    dms_Supervisor_Name = request.form['ui_dms_Supervisor_Name']
    dms_Designation = request.form['ui_dms_Designation']
    dms_WhatsApp_No = request.form['ui_dms_WhatsApp_No']


    # Make Password Hash
    pass_hash = user_manager.hash_password(password)
    


    # Get Company Detail From Endpont
    company_data_obj = requests.get('%s/API_bussiness/get_company_data_by_type' % API_URL_consumer,
                                    params={'dms_cmp_id':company})

    # Convert In Json
    company_data = company_data_obj.json()

    # Get Company Details From company data
    company = company_data[0]['dms_cmp_name']
    company_type = company_data[0]['dms_cmp_type']
    company_location = company_data[0]['dms_cmp_location']
    company_territory = company_data[0]['dms_cmp_territory']
    company_region = company_data[0]['dms_cmp_region']
    company_id = company_data[0]['dms_cmp_id']

    # Get Tenant data
    tenant_id = current_user.tenant_id
    tenant_name = current_user.tenant_name




    # Create Default Menu For Default CSE Use
    list_of_menus, dict_of_submenus = func_get_menu1('CSE')

    default_menu = get_new_menus_structure(list_of_menus, dict_of_submenus)

    menus = json.dumps(default_menu)




    # Sent Post Request To Create Enquiry Endoint
    try:
        create_request_obj = requests.post('%s/API_bussiness/save_user_data' % API_URL_consumer,
                                           params={
                                               'user_id': user_id,
                                               'email': request.form['ui_email'],
                                               'email_confirmed_at': StartDate,
                                               'username': request.form['ui_username'],
                                               'password': user_manager.hash_password(request.form['ui_username']),
                                               'phone_number': request.form['ui_phone_number'],

                                               'first_name': request.form['ui_first_name'],
                                               'last_name': request.form['ui_last_name'],
                                               'age': request.form['ui_age'],
                                               'gender': gender,
                                               'DoB': DoB,
                                               'city': city,
                                               'state': state,
                                               'country': country,
                                               'postal_pin': postal_pin,

                                               'tenant_id': tenant_id,
                                               'tenant_name': tenant_name,
                                               'company': company,
                                               'company_type': company_type,
                                               'company_id': company_id,
                                               'company_location': company_location,
                                               'company_territory': company_territory,
                                               'company_region': company_region,
                                               'branch_id': branch_id,
                                               'branch_name': branch_name,
                                               'department_id': department_id,
                                               'department_name': department_name,

                                               'dms_Supervisor_Name': dms_Supervisor_Name,
                                               'dms_Designation': dms_Designation,
                                               'dms_WhatsApp_No': dms_WhatsApp_No,

                                               'menus':menus

                                           })

        flash('Your User Has Been Register SuccessFully', 'info')
    except Exception as e:
        print(e)
        flash('Your User Has Been Not Register SuccessFully', 'error')


    # Add Comment In NewsTransaction
    # Create Document In News Transaction
    create_transaction_document = requests.post('%s/API_bussiness/save_user_transaction_data' % API_URL_consumer,
                                                params={'user_id':user_id,
                                                        'user_name':user_name,
                                                        'dms_Response':'User Created Successfully',
                                                        'dms_response_Date':datetime.now(),
                                                        'dms_Status':'Created',
                                                        'dms_User_pic_link':None}
                                                )
    
    return

def update_user(tenant_id, company_id, API_URL_consumer, API_URL_tenant, user_id):

    # Getting Data From Ui For Specific User
    user_data_request_obj = requests.get('%s/API_bussiness/get_user_data' %API_URL_consumer,
                               params={'user_id':user_id})

    # Creating Response Objects Into JSON Object
    user_data = user_data_request_obj.json()



    # Get Specific news Transaction
    transaction_request_obj = requests.get('%s/API_bussiness/get_user_transaction_data'
                                           % API_URL_consumer, params={'user_id': user_id})

    # Convert responce obj to json
    transaction_data = transaction_request_obj.json()
    # print("transaction_data", transaction_data)


    # All Companys Data For Dropdawn
    company_data_obj = requests.get('%s/API_bussiness/get_company_data_by_type' % API_URL_consumer)

    # Convert In Json
    company_data = company_data_obj.json()

    return user_data, transaction_data, company_data

def update_user_save(tenant_id, company_id, API_URL_consumer, API_URL_tenant, user_id):
     # Getting data from Form
    user_id = user_id
    email = request.form['ui_email']
    email_confirmed_at = StartDate
    phone_number = request.form['ui_phone_number']

    first_name = request.form['ui_first_name']
    last_name = request.form['ui_last_name']
    age = request.form['ui_age']
    gender = request.form['ui_gender']
    DoB = request.form['ui_DoB']
    city = request.form['ui_city']
    state = request.form['ui_state']
    country = request.form['ui_country']
    postal_pin = request.form['ui_postal_pin']

    company_id = request.form['ui_company']
    company = request.form['ui_company']
    company_type = request.form['ui_company_type']
    company_location = request.form['ui_company_location']
    company_territory = request.form['ui_company_territory']
    company_region = request.form['ui_company_region']
    branch_id = request.form['ui_branch_id']
    branch_name = request.form['ui_branch_name']
    department_id = request.form['ui_department_id']
    department_name = request.form['ui_department_name']


    dms_Supervisor_Name = request.form['ui_dms_Supervisor_Name']
    dms_Designation = request.form['ui_dms_Designation']
    dms_WhatsApp_No = request.form['ui_dms_WhatsApp_No']




    # Sent Post Request To Create Enquiry Endoint
    try:
        create_request_obj = requests.put('%s/API_bussiness/update_user_data' % API_URL_consumer,
                                           params={
                                               'user_id': user_id,
                                               'email': email,
                                               'email_confirmed_at': email_confirmed_at,
                                               'phone_number': phone_number,

                                               'first_name': first_name,
                                               'last_name': last_name,
                                               'age': age,
                                               'gender': gender,
                                               'DoB': DoB,
                                               'city': city,
                                               'state': state,
                                               'country': country,
                                               'postal_pin': postal_pin,

                                               'tenant_id': current_user.tenant_id,
                                               'tenant_name': current_user.tenant_name,
                                               'company': company,
                                               'company_type': company_type,
                                               'company_id': company_id,
                                               'company_location': company_location,
                                               'company_territory': company_territory,
                                               'company_region': company_region,
                                               'branch_id': branch_id,
                                               'branch_name': branch_name,
                                               'department_id': department_id,
                                               'department_name': department_name,

                                               'dms_Supervisor_Name': dms_Supervisor_Name,
                                               'dms_Designation': dms_Designation,
                                               'dms_WhatsApp_No': dms_WhatsApp_No

                                           })

        flash('User Data Updated SuccessFully', 'info')
    except Exception as e:
        print(e)
        flash('User Data Not Updated SuccessFully', 'error')



    # Add Comment In User TXN
    # Create Document In UserTransaction
    create_transaction_document = requests.post('%s/API_bussiness/save_user_transaction_data' % API_URL_consumer,
                                                params={'user_id':user_id,
                                                        'user_name':user_name,
                                                        'dms_Response':'User Data Is Updated',
                                                        'dms_response_Date':datetime.now(),
                                                        'dms_Status':'Updated',
                                                        'dms_User_pic_link':None}
                                                )

    return

def profile_page(tenant_id, company_id, API_URL_consumer, API_URL_tenant, user_id):

    # Getting Data From Ui For Specific User
    user_data_request_obj = requests.get('%s/API_bussiness/get_user_data' %API_URL_consumer,
                               params={'user_id':user_id})

    # Creating Response Objects Into JSON Object
    user_data = user_data_request_obj.json()




    # GEt User Transaction Data
    user_txn_data_obj = requests.get('%s/API_bussiness/get_user_transaction_data' %API_URL_consumer,
                               params={'user_id':user_id})

    # Convert Response Object into Json Data
    user_txn_data = user_txn_data_obj.json()

    return user_data, user_txn_data