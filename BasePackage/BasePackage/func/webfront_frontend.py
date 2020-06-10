"""

This Program Is For Getting All View Related To

"""

# Importing All Necessary Modules

import os
import random
import requests
import json
import datetime
from datetime import datetime, timedelta

# from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, make_response, session
from flask_user import current_user





######################################################## My Profile ############################################################
# Function for view profile
# @WebFront.route('/my_profile/<user_ID>', methods=['GET', 'POST'])
def func_view_profile(Page_id, tenant_id, company_id, API_URL_consumer, API_URL_tenant, user_ID):

    # Getting Current User Profile Detail
    # Getting Current User
    first_name = current_user.first_name
    last_name = current_user.last_name
    user_id = current_user.user_id
    user_name = current_user.username
    company = current_user.company
    email = current_user.email
    roles = current_user.roles
    company_id = current_user.company_id
 
    
    # Get Response Through API
    data = requests.get('%s/API_bussiness/get_f_application_response_master_data'
                       % API_URL_consumer, params={'user_id':user_ID})
    f_application_response_data = data.json()
    # print(f_application_response_data)
    
    pg_compnt_list1 = requests.get('%s/API_bussiness/get_webfront_page_component_data'
                            % API_URL_consumer, params={'Page_id':Page_id})
    page_compnt_list1 = pg_compnt_list1.json()

    

    user_request = requests.get('%s/API_bussiness/get_user_data'
                                % API_URL_consumer, params={'user_id':user_ID})
    user_data = user_request.json()
    
    return f_application_response_data, page_compnt_list1, user_data



#This function for update profile of user
# @WebFront.route('/profile_update/<user_ID>', methods=['GET', 'POST'])
def func_update_user_profile(Page_id, tenant_id, company_id, API_URL_consumer, API_URL_tenant, user_ID):
    

    user_request = requests.get('%s/API_bussiness/get_user_data'
                                % API_URL_consumer, params={'user_id':user_ID})
    user_data = user_request.json()
    # print('user_data::', user_data)

    pg_compnt_list1 = requests.get('%s/API_bussiness/get_webfront_page_component_data'
                            % API_URL_consumer, params={'Page_id':Page_id})
    page_compnt_list1 = pg_compnt_list1.json()

   

    return user_data, page_compnt_list1

# function for save updated data of user
# @WebFront.route('/update_save_user/<user_ID>', methods=['GET', 'POST'])
def func_update_save_user_data(Page_id, tenant_id, company_id, API_URL_consumer,
                                API_URL_tenant, user_ID, phone_number, first_name, last_name, city, state, file_path1):
    # Getting Current User Profile Detail
    # Getting Current User
    first_name = current_user.first_name
    user_id = current_user.user_id
    user_name = current_user.username
    email = current_user.email
    roles = current_user.roles
    company = current_user.company
    company_type = current_user.company_type
    company_id = current_user.company_id



    user_request = requests.get('%s/API_bussiness/get_user_data'
                                % API_URL_consumer, params={'user_id':user_ID})
    user_data = user_request.json()
    # print('user_data::', user_data)
    
   
    
   
    for i in user_data:
        user_Img = i['dms_User_pic_Id']
        
        
    if file_path1 == 'NA':
        file_path1 = user_Img
   
    dms_User_pic_Id = file_path1
    

    

    
    # try:
    data = requests.put('%s/API_bussiness/update_save_user'
                        % API_URL_consumer, params={'user_id':user_ID,
                                                            'email':current_user.email,
                                                            'active':current_user.active,
                                                            'email_confirmed_at':current_user.email_confirmed_at,
                                                            'username':current_user.username,
                                                            'password':current_user.password,
                                                            'phone_number':phone_number,
                                                            'company':current_user.company,
                                                            'company_type':current_user.company_type,
                                                            'company_id':current_user.company_id,
                                                            'company_location':current_user.company_location,
                                                            'company_territory':current_user.company_territory,
                                                            'roles':current_user.roles,
                                                            'first_name':first_name,
                                                            'last_name':last_name,
                                                            'age':current_user.age,
                                                            'gender':current_user.gender,
                                                            'DoB':current_user.DoB,
                                                            'city':city,
                                                            'state':state,
                                                            'country':current_user.country,
                                                            'postal_pin':current_user.postal_pin,
                                                            'department_name':current_user.department_name,
                                                            'dms_Supervisor_Name':current_user.dms_Supervisor_Name,
                                                            'dms_Designation':current_user.dms_Designation,
                                                            'dms_User_pic_Id': dms_User_pic_Id,
                                                            'dms_User_pic_link':current_user.dms_User_pic_link,
                                                            'dms_WhatsApp_No':current_user.dms_WhatsApp_No,
                                            })
    

    return "success"











##############################################################################################################################################
# News list Function
# @WebFront.route('/news_list', methods=['GET', 'POST'])
def func_news_list(Page_id, tenant_id, company_id, API_URL_consumer, API_URL_tenant):

   
    pg_compnt_list1 = requests.get('%s/API_bussiness/get_webfront_page_component_data'
                            % API_URL_consumer, params={'Page_id':'PG_2018'})
    page_compnt_list1 = pg_compnt_list1.json()

    # news list data

    news_list_request = requests.get('%s/API_bussiness/get_news_data_by_type'
                                                % API_URL_tenant, params={'dms_News_Category':'News',
                                                                        'tenant_id':tenant_id })
    news_request_data = news_list_request.json()
    
    return page_compnt_list1, news_request_data







## Blog list function
# @WebFront.route('/blog_list', methods=['GET', 'POST'])
def func_blog_list(Page_id, tenant_id, company_id, API_URL_consumer, API_URL_tenant):

    pg_compnt_list1 = requests.get('%s/API_bussiness/get_webfront_page_component_data'
                            % API_URL_consumer, params={'Page_id':Page_id})
    page_compnt_list1 = pg_compnt_list1.json()

    # news list data

    news_list_request = requests.get('%s/API_bussiness/get_news_data_by_type'
                                      % API_URL_tenant, params={'dms_News_Category':'Blogs',
                                                                'tenant_id':tenant_id })
    news_request_data = news_list_request.json()
    
    return page_compnt_list1, news_request_data












# news details function
# @WebFront.route('/details/<news_id>', methods=['GET', 'POST'])
def func_news_details(Page_id, tenant_id, company_id, API_URL_consumer, API_URL_tenant, news_id):

    
    pg_compnt_list1 = requests.get('%s/API_bussiness/get_webfront_page_component_data'
                            % API_URL_consumer, params={'Page_id':Page_id})
    page_compnt_list1 = pg_compnt_list1.json()

    

    #news_detail
    news_detail_request = requests.get('%s/API_bussiness/get_news_data_by_type'
                                               % API_URL_tenant, params={'dms_News_Id':news_id})
     
    news_data =news_detail_request.json()

    
    return page_compnt_list1, news_data



