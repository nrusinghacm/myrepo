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

# import requests
from flask import jsonify, request
from mongoengine.queryset.visitor import Q
# import dialogflow

# import json

# Importing From Our Models

# Importing From Our Models

from BasePackage.func.user_models import User, user_transaction
# from APP.UserManagement.queries.create_user_id import func_create_user_id
# from APP.UserManagement.queries.user_transaction import func_user_transaction_support

from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, current_app, make_response, session
from collections import Counter
from pprint import pprint
from datetime import datetime, timedelta, date



# # API URL assign
# API_URL_tenant = 'http://127.0.0.1:8001'
# API_URL_consumer = 'http://127.0.0.1:8000'


# function for home page
def create_user(user_id,
                     email,
                     active,
                     email_confirmed_at,
                     username,
                     password,
                     phone_number,

                     company,
                     company_type,
                     company_id,
                     company_location,
                     company_territory,
                     company_region,
                     branch_id,
                     branch_name,
                     department_id,
                     department_name,
roles,
                     first_name,
                     last_name,
                     age,
                     gender,
                     DoB,
                     city,
                     state,
                     country,
                     postal_pin,

                     dms_Supervisor_Name,
                     dms_Designation,
                     dms_User_pic_Id,
                     dms_User_pic_link,
                     dms_WhatsApp_No,

                     menus

                     ):



    create_object = User(user_id=user_id,
                         email=email,
                         active=active,
                         email_confirmed_at=email_confirmed_at,
                         username=username,
                         password=password,
                         phone_number=phone_number,

                         company=company,
                         company_type=company_type,
                         company_id=company_id,
                         company_location=company_location,
                         company_territory=company_territory,
                         company_region=company_region,
                         branch_id=branch_id,
                         branch_name=branch_name,
                         department_id=department_id,
                         department_name=department_name,
roles = roles,
                         first_name=first_name,
                         last_name=last_name,
                         age=age,
                         gender=gender,
                         DoB=DoB,
                         city=city,
                         state=state,
                         country=country,
                         postal_pin=postal_pin,

                         dms_Supervisor_Name=dms_Supervisor_Name,
                         dms_Designation=dms_Designation,
                         dms_User_pic_Id=dms_User_pic_Id,
                         dms_User_pic_link=dms_User_pic_link,
                         dms_WhatsApp_No=dms_WhatsApp_No,

                         menus=menus
                         )

    # Save Create Object data in Database

    create_object.save()
    response = {'Response': 'User Created Sucssesfully'}

    

    return response



# Update User Data
def update_user(user_id,
                          email,
                          active,
                          email_confirmed_at,
                          phone_number,

                          company,
                          company_type,
                          company_id,
                          company_location,
                          company_territory,
                          company_region,
                          branch_id,
                          branch_name,
                          department_id,
                          department_name,

                          first_name,
                          last_name,
                          age,
                          gender,
                          DoB,
                          city,
                          state,
                          country,
                          postal_pin,
roles,
                          dms_Supervisor_Name,
                          dms_Designation,
                          dms_User_pic_Id,
                          dms_User_pic_link,
                          dms_WhatsApp_No,

                          menus,

                          ):
    user_id = user_id
    # Update News With user_id

    User.objects(user_id=user_id).update_one(

        set__email=email,
        set__active=active,
        set__email_confirmed_at=email_confirmed_at,
        set__phone_number=phone_number,

        set__company=company,
        set__company_type=company_type,
        set__company_id=company_id,
        set__company_location=company_location,
        set__company_territory=company_territory,
        set__company_region=company_region,
        set__branch_id=branch_id,
        set__branch_name=branch_name,
        set__department_id=department_id,
        set__department_name=department_name,

        set__roles=roles,

        set__first_name=first_name,
        set__last_name=last_name,
        set__age=age,
        set__gender=gender,
        set__DoB=DoB,
        set__city=city,
        set__state=state,
        set__country=country,
        set__postal_pin=postal_pin,

        set__dms_Supervisor_Name=dms_Supervisor_Name,
        set__dms_Designation=dms_Designation,
        set__dms_User_pic_Id=dms_User_pic_Id,
        set__dms_User_pic_link=dms_User_pic_link,
        set__dms_WhatsApp_No=dms_WhatsApp_No,

        set__menus=menus,

    )

    response = {'Response': 'User Updated Sucssesfully'}

    return response


#  Route Function For Save user Transaction Data In Database
def save_user_transaction(user_id,
                                    user_name,

                                    dms_Response,
                                    dms_response_Date,
                                    dms_Status,

                                    dms_User_pic_link,
                                    ):
    #  Create Database Obj for Saving data
    data_obj = user_transaction(user_id=user_id,
                                user_name=user_name,

                                dms_Response=dms_Response,
                                dms_response_Date=dms_response_Date,
                                dms_Status=dms_Status,

                                dms_User_pic_link=dms_User_pic_link
                                )

    #  Save data In database Using data Obj
    data_obj.save()
    responses = {'Response': 'Data saved Successfully'}
    return responses


# Get All Transactions For Specific User

def get_user_transactions(user_id):

    # Call User Transaction Object To Get Transaction Data
    txn_data = user_transaction.objects(user_id=user_id)


    # Create List For Final Data
    list_of_txn_data = []


    # Loop The Txn data And Get Correct Format
    for data in txn_data:

        dic = {}

        dic['user_id'] = data['user_id']
        dic['user_name'] = data['user_name']
        dic['dms_Response'] = data['dms_Response']
        dic['dms_response_Date'] = data['dms_response_Date']
        dic['dms_Status'] = data['dms_Status']
        dic['dms_User_pic_link'] = data['dms_User_pic_link']


        # Append All Data In Final List
        list_of_txn_data.append(dic)


        # Sort List Based On Latest Response Date
        list_of_txn_data.sort(key=lambda r: r['dms_response_Date'], reverse = True)




    # Check If Thre Is No data Then Create Data not Available
    if len(list_of_txn_data)<1:
        dic = {}

        dic['user_id'] = "Data Not Available"
        dic['user_name'] = "Data Not Available"
        dic['dms_Response'] = "Data Not Available"
        dic['dms_response_Date'] = "Data Not Available"
        dic['dms_Status'] = "Data Not Available"
        dic['dms_User_pic_link'] = "Data Not Available"

        # Append All Data In Final List
        list_of_txn_data.append(dic)

    else:
        pass

    return list_of_txn_data


# This Function Getting All Data From Lead Master By Lead Types
# For Same User Superuser id And User Id Is Same Then This User Is A Super USer

def get_user_data(
        user_id,
        active,
        roles,

        company_id,
        department_id,
        branch_id,
        dms_Supervisor_Name,

        request_before_date,
        request_after_date,

):
    # Opprtunity
    if company_id != None:
        data_obj = User.objects(company_id=user_id)
    elif department_id != None:
        data_obj = User.objects(department_id=department_id)
    elif branch_id != None:
        data_obj = User.objects(branch_id=branch_id)
    elif user_id != None:
        data_obj = User.objects(user_id=user_id)
    elif user_id != None:
        data_obj = User.objects(user_id=user_id)
    elif dms_Supervisor_Name != None:
        data_obj = User.objects(dms_Supervisor_Name=dms_Supervisor_Name)


    elif request_before_date:
        request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')
        if request_after_date:
            request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
            data_obj = User.objects(Q(email_confirmed_at__gt=request_before_date_)
                                    & Q(email_confirmed_at__lt=request_after_date_))
        else:

            data_obj = User.objects
    else:
        data_obj = User.objects

    # Declaring List For Order Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic['user_id'] = i.user_id
        dic['active'] = i.active
        dic['email'] = i.email
        dic['email_confirmed_at'] = i.email_confirmed_at
        dic['username'] = i.username
        dic['password'] = i.password
        dic['phone_number'] = i.phone_number

        dic['company'] = i.company
        dic['company_type'] = i.company_type
        dic['company_id'] = i.company_id
        dic['company_location'] = i.company_location
        dic['company_territory'] = i.company_territory
        dic['company_region'] = i.company_region
        dic['branch_id'] = i.branch_id
        dic['branch_name'] = i.branch_name
        dic['department_id'] = i.department_id
        dic['department_name'] = i.department_name

        dic['roles'] = i.roles
        dic['first_name'] = i.first_name
        dic['last_name'] = i.last_name
        dic['age'] = i.age
        dic['gender'] = i.gender
        dic['DoB'] = i.DoB
        dic['city'] = i.city
        dic['state'] = i.state
        dic['country'] = i.country
        dic['postal_pin'] = i.postal_pin

        dic['dms_Supervisor_Name'] = i.dms_Supervisor_Name
        dic['dms_Designation'] = i.dms_Designation
        dic['dms_User_pic_Id'] = i.dms_User_pic_Id
        dic['dms_User_pic_link'] = i.dms_User_pic_link
        dic['dms_WhatsApp_No'] = i.dms_WhatsApp_No

        list_of_data.append(dic)

        # Sort List By Dates
        # list_of_data.sort(key=lambda r: r['dms_Lead_Date'], reverse)


    # There Is No Data For Perticular Query

    if len(list_of_data) < 1:
        dic = {}
        dic['user_id'] = "Data Not Available"
        dic['active'] = "Data Not Available"
        dic['email'] = "Data Not Available"
        dic['email_confirmed_at'] = "Data Not Available"
        dic['username'] = "Data Not Available"
        dic['password'] = "Data Not Available"
        dic['phone_number'] = "Data Not Available"

        dic['company'] = "Data Not Available"
        dic['company_type'] = "Data Not Available"
        dic['company_id'] = "Data Not Available"
        dic['company_location'] = "Data Not Available"
        dic['company_territory'] = "Data Not Available"
        dic['company_region'] = "Data Not Available"
        dic['branch_id'] = "Data Not Available"
        dic['branch_name'] = "Data Not Available"
        dic['department_id'] = "Data Not Available"
        dic['department_name'] = "Data Not Available"

        dic['roles'] = ["Data Not Available"]
        dic['first_name'] = "Data Not Available"
        dic['last_name'] = "Data Not Available"
        dic['age'] = "Data Not Available"
        dic['gender'] = "Data Not Available"
        dic['DoB'] = "Data Not Available"
        dic['city'] = "Data Not Available"
        dic['state'] = "Data Not Available"
        dic['country'] = "Data Not Available"
        dic['postal_pin'] = "Data Not Available"

        dic['dms_Department'] = "Data Not Available"
        dic['dms_Supervisor_Name'] = "Data Not Available"
        dic['dms_Designation'] = "Data Not Available"
        dic['dms_User_pic_Id'] = "Data Not Available"
        dic['dms_User_pic_link'] = "Data Not Available"
        dic['dms_WhatsApp_No'] = "Data Not Available"

        list_of_data.append(dic)

    return list_of_data


# Get User Data For Team View
# First Find All User For There Supervisor
# Then Loop It Base On Role Find There Reporties
def get_data_for_team_view(user_id):


    # Create List Of Role Who Can Have Reporties
    list_of_roles = ['SKF Leader','teamlead','teammember']

    # declair Final Dict
    final_data_dict = {}


    # Get Supervisor Id
    supervisor_id = user_id


    # Find First User Who Logged in
    supervisor_data = func_get_user_data_by_type(user_id=supervisor_id)


    # Get All Reporties For This Supervisor Id
    # Call Func
    list_of_reporties = func_get_user_data_by_type(dms_Supervisor_Name=supervisor_id)

    # make level2 list
    list_of_level_2 = []

    # find reporties
    if (len(list_of_reporties)>0) and (supervisor_data[0]['roles'][0] in list_of_roles) and (list_of_reporties[0]['user_id'] != 'Data Not Available'):



        print("Hi I Am In")

        # Loop The List And Find there reportees
        for user in list_of_reporties:

            # Create Dict
            temp_dict = {}


            # Find User Reportees
            # Call Func
            list_of_reporties_level_2 = func_get_user_data_by_type(dms_Supervisor_Name = user['user_id'])

            print(list_of_reporties_level_2)


            # if
            # find reporties
            if (len(list_of_reporties_level_2) > 0) and (user['roles'][0] in list_of_roles) and (list_of_reporties[0]['user_id'] != 'Data Not Available'):

                # Make List Of Level3
                list_of_level_3 = []

                # Loop The List And Find there reportees
                for user1 in list_of_reporties_level_2:
                    # Create Dict
                    temp_dict2 = {}

                    # Find User Reportees
                    # Call Func
                    list_of_reporties_level_3 = func_get_user_data_by_type(dms_Supervisor_Name=user1['user_id'])





                    # Check Data Is There Or Not
                    if user1['user_id'] != 'Data Not Available':

                        # Append Same Supervisor In Same List
                        list_of_level_3.append(user1)


                        # append level2 data in dict
                        temp_dict2[user1['user_id']] = list_of_reporties_level_3


                        # Append Level 3 Data in list

                        list_of_level_3.append(temp_dict2)

                    else:
                        pass



            else:
                pass



            # Append Supervisor Also In Same List
            list_of_reporties_level_2.append(user)


            # append data in temp list for level 2
            temp_dict[user['user_id']] = list_of_reporties_level_2



            # Append Data In

            list_of_level_2.append(temp_dict)

    else:
        pass


    # Create Dict For Supervisor data
    dic_temp3 = {}
    dic_temp3[supervisor_data[0]['username']] = supervisor_data[0]

    # Append First Supervisor In List
    list_of_level_2.append(dic_temp3)

    # Create final Dict

    final_data_dict[supervisor_data[0]['username']] = list_of_level_2


    return final_data_dict



