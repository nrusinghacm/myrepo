"""

This Models Contains All Models Related Tenant Management

"""

# Importing All Necessary Models

from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
import os
import json
import requests
# from flask_user import login_required, UserManager, UserMixin, roles_required, current_user
from flask import current_app



#import our libraries
from APP import app




# Get root path
PATH = app.root_path


# Read Property file For Getting Data
with app.app_context():
    # API_URL = current_app.config['COMPANY_PROPERTY_DATA']['API_details']['api_url']
    API_URL_consumer = current_app.config['COMPANY_PROPERTY_DATA']['API_details']['api_url_consumer']
    API_URL_tenant = current_app.config['COMPANY_PROPERTY_DATA']['API_details']['api_url_tenant']



# Get File Extension
def file_extension(file_name):

    # Split File
    file_split_obj = file_name.split('.')

    file_extension_ = file_split_obj[1]

    # Convert Extension To Lower Case
    file_extension = file_extension_.lower()

    return file_extension





# Save Profile Picture
def save_tenant_logo(file, tenant_id):

    for file in file:

        # Get File
        file = file

        # Get Path
        folder_path_for_image = 'static/assets/images/logo'


        #get new name for image with respect to user id
        image_name = tenant_id + '.png'


        # Join Full Path With Image Name And Folder Path
        full_path = os.path.join(PATH, folder_path_for_image, image_name)


        # Save Image In Save Folder
        file.save(full_path)


        # Get Image Path
        image_final_path = 'static/assets/images/logo' + '/' + image_name


    return image_final_path





# # Save Transaction data When Image Uploaded
# def func_save_tenant_txn_data(file, tenant_id, API_URL, tenant_name, dms_Response, dms_response_Date, dms_Status):
#
#     # save Image Using Above Function
#     # And Get Image Path
#     img_path = func_save_tenant_logo(file, user_id)
#
#
#     # Save TXN Data By API End Points
#     end_piont_object = requests.post('%s/API_bussiness/save_user_transaction_data'% API_URL,
#                                   params={'user_id':user_id,
#                                           'user_name':user_name,
#                                           'dms_Response':dms_Response,
#                                           'dms_response_Date':dms_response_Date,
#                                           'dms_Status':dms_Status,
#                                           'dms_User_pic_link':img_path})
#
#
#     return {'Response': 'Saved Sucessfully'}



# Get Tenant Data
def tenant_data(tenant_id):

    # Get Tenant Data By API
    tenant_list_request_obj = requests.get('%s/API_bussiness/get_existing_tenant_from_tenantcol'
                                           %API_URL,
                                           params={
                                               'tenant_id':tenant_id
                                           }
                                           )

    # Convert Tenant List Object Into Json
    tenant_list_data = tenant_list_request_obj.json()

    # Get Proper Format
    common_data_for_login = {'tenant_list_data':tenant_list_data}


    return common_data_for_login