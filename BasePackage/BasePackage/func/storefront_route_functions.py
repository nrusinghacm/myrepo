# pylint: disable=missing-docstring, no-member, unused-variable

"""

This Program Is For SKF All Function For Routes Related To SKF Modules Defined Here

"""

# Import All Neccessary Modules
import os
import ast
import random
import requests

from datetime import datetime, timedelta
import json
from flask import Blueprint, jsonify
from mongoengine.queryset.visitor import Q


# Importing Our modules
from BasePackage.func.storefront_models import och_page_master,och_page_component_master




from BasePackage.func.user_models import User, user_transaction
# from APP.UserManagement.queries.create_user_id import func_create_user_id
# from APP.UserManagement.queries.user_transaction import func_user_transaction_support

from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, current_app, make_response, session
from collections import Counter
from pprint import pprint
from datetime import datetime, timedelta, date


# Creating Blueprint

StoreFront = Blueprint(__name__, 'StoreFront')



# All Route Functions


def get_page_component_data(start_data_no,
                                Page_id,
                                company_id,
                                ):

    
    if Page_id:
        data_obj = och_page_component_master.objects(Page_id=Page_id)
    
    
    # Declaring List For Order Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic['Page_id'] = i.Page_id
        dic['Page_Name'] = i.Page_Name
        dic['Page_URL'] = i.Page_URL
        dic['Company_Id'] = i.Company_Id
        dic['FrameArray'] = i.FrameArray
        dic['Component_Id'] = i.Component_Id
        dic['Component_Name'] = i.Component_Name
        dic['Component_Category'] = i.Component_Category
        dic['Sequence'] = i.Sequence
        dic['Element_Id'] = i.Element_Id
        dic['Element_Name'] = i.Element_Name
        dic['partial_file_path'] = i.partial_file_path
        dic['component_heading'] = i.component_heading
        dic['element_heading'] = i.element_heading
        dic['sub_heading'] = i.sub_heading
        dic['description'] = i.description
        dic['prd_collection_name'] = i.prd_collection_name
        dic['link_name'] = i.link_name
        dic['link_url'] = i.link_url
        dic['button_name'] = i.button_name
        dic['button_link'] = i.button_link
        dic['image_url'] = i.image_url
        dic['video_url'] = i.video_url
        dic['dropdown_name'] = i.dropdown_name
        dic['dropdown_data'] = i.dropdown_data
        dic['dropdown_url'] = i.dropdown_url
        dic['font_color'] = i.font_color
        dic['hover_color'] = i.hover_color
        dic['bg_color'] = i.bg_color
        dic['hover_bg_color'] = i.hover_bg_color
        dic['select_color'] = i.select_color
        dic['padding'] = i.padding
        dic['margin'] = i.margin
        dic['height'] = i.height
        dic['width'] = i.width
        dic['border_color'] = i.border_color
        dic['border_hover_color'] = i.border_hover_color



        list_of_data.append(dic)

        # Sort List By Dates
        # list_of_data.sort(key=lambda r: r['cart_Entry_Date'], reverse=True)
    return list_of_data


def func_get_page_component_element(
                        page_id,
                        company_id,
                        ):

    
    if company_id:
        data_obj = page_component_element_master.objects(company_id=company_id)
   
    
    # Declaring List For Order Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic['pgem_id'] = i.pgem_id
        dic['Component_Category'] = i.Component_Category
        dic['Component_Name'] = i.Component_Name
        dic['Sequence'] = i.Sequence
        dic['element'] = i.element

        dic['Link_Name'] = i.Link_Name
        dic['Link_Url'] = i.Link_Url
        dic['Font_Color'] = i.Font_Color
        dic['Hover_Color'] = i.Hover_Color
        dic['bg_Color'] = i.bg_Color

        dic['Select_Color'] = i.Select_Color
        dic['Dropdown_Name'] = i.Dropdown_Name
        dic['Dropdown_Data'] = i.Dropdown_Data
        dic['Collection_Name'] = i.Collection_Name
        dic['Image'] = i.Image

        dic['Button_Link'] = i.Button_Link
        dic['Description'] = i.Description
        dic['company_id'] = i.company_id

        list_of_data.append(dic)

        # Sort List By Dates
        # list_of_data.sort(key=lambda r: r['cart_Entry_Date'], reverse=True)
    return list_of_data

