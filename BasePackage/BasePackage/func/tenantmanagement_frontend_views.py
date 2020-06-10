"""

This File Contains All Views Function Related To Tenant Management

"""

# Import All Necessary Packages
from functools import wraps
import json
import requests
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_user import current_user



# Import Our Modules
from APP import app
from APP.UserManagement.models import User, func_get_menu
from APP.TenantManagement.models import func_save_tenant_logo

# for tenant data from tenant collection
from APP.TenantManagement.models import get_tenant_data


# Creating Blueprints

TenantManagement = Blueprint(__name__, 'TenantManagement')


# Read Property file For Getting Data
with app.app_context():
    # API_URL = current_app.config['COMPANY_PROPERTY_DATA']['API_details']['api_url']
    API_URL_consumer = current_app.config['COMPANY_PROPERTY_DATA']['API_details']['api_url_consumer']
    API_URL_tenant = current_app.config['COMPANY_PROPERTY_DATA']['API_details']['api_url_tenant']


# Company Login Logic
# Decorator Function For Company Logic
# This Function Create Decorator company required
# This Decorator Works as If Company Field Available Then It Runs Function Else Redirect Home Page

def tenant_required(func):

    @wraps(func)
    def wrapper_func(*args, **kwargs):

        if current_user.tenant_id:
            return func(*args, **kwargs)

        else:
            return redirect(url_for('TenantManagement.func_add_tenant_page'))

    return wrapper_func




# Add Company Details
# This Function Create Route For Adding Company Details

@TenantManagement.route('/tenant_create_form', methods=['GET', 'POST'])
def func_add_tenant_page():

    # Getting Current User
    user_name = current_user.username
    email = current_user.email
    user_id = current_user.user_id
    roles = current_user.roles


    # Getting Notification For Home Page By API
    notification_request_obj = requests.get('%s/API_bussiness/notification/read_user_messages/%s'
                               % (API_URL, user_id))
    # Converting Response Object To JSON Data
    data_notification_data = notification_request_obj.json()
    # Getting No Of Unread Messages
    no_unread_of_notification = len(data_notification_data)

    # Get Tenant Data From tenant Collections
    tenant_data = get_tenant_data(current_user.tenant_id)


    # Getting List Of Submenus According TO Main Menu
    list_of_menus, dict_of_submenus = func_get_menu(current_user)


    return render_template('tenant_create_form.html', current_app=current_app,
                           tenant_data=tenant_data,
                           current_user=current_user,
                           list_of_menus=list_of_menus,
                           dict_of_submenus=dict_of_submenus,
                           data_obj=data_notification_data,
                           no_unread_of_notification=no_unread_of_notification,
                           )





# This Function Saves Company Data
@TenantManagement.route('/save_tenant', methods=['GET', 'POST'])
def save_tenant_details():

    # Get Creator Name And Id
    tenant_admin_id = current_user.user_id
    tenant_admin_name = current_user.first_name

    # Generate Tenant Id generate_tenant_id
    tenant_id_object = requests.get('%s/API_bussiness/generate_tenant_id'% API_URL)

    tenant_id = tenant_id_object.json()


    # Uploading Image In Folder
    # Check If Logo Present In Files
    # If Not Show Flash Messages
    # Else Save In Proper Folder
    # Check The No Of File User Uploading
    if 'ui_company_logo_url' not in request.files:
        flash('No File Part', 'error')
        print()
    else:
        # Else Get File List From Form
        files = request.files.getlist('ui_company_logo_url')
        print(files)

        # If File Not Selected Then list Is emty So Check
        if files[0].filename != '':
            # Save File
            save_txn = func_save_tenant_logo(files, tenant_id)
            flash('Logo Uploaded')





    # Get Data From Form
    tenant_name = request.form['ui_company_name']
    print(tenant_name)
    tenant_address = request.form['ui_company_address']
    tenant_city = request.form['ui_company_city']
    tenant_state = request.form['ui_company_state']
    tenant_country = request.form['ui_company_country']
    tenant_type = request.form['ui_company_type']
    tenant_description = request.form['ui_company_descriptions']
    tenant_logo_url = save_txn
    tenant_header_color = 'background: #0068b4'
    tenant_side_header_color = 'background-image: linear-gradient(to bottom, #0068b4,#0068b4,#0068b4,#0068b4,#0068b4,#0068b4, white);'





    # Saving Tenant Data In Database
    # Post Request API For Saving Data
    post_request_obj = requests.post('%s/API_bussiness/create_tenant'%API_URL,
                                     params={
                                         'tenant_id':tenant_id,
                                         'tenant_name':tenant_name,
                                         'tenant_address':tenant_address,
                                         'tenant_city':tenant_city,
                                         'tenant_state':tenant_state,
                                         'tenant_country':tenant_country,
                                         'tenant_type':tenant_type,
                                         'tenant_description':tenant_description,
                                         'tenant_logo_url':tenant_logo_url,
                                         'tenant_header_color':tenant_header_color,
                                         'tenant_side_header_color':tenant_side_header_color,
                                         'tenant_admin_id':tenant_admin_id,
                                         'tenant_admin_name':tenant_admin_name

                                     }
                                     )

    # Check The Status Of Saving Function
    response = post_request_obj.json()
    status = response['Status']
    print(response)

    if status == 'Success':

        # Is Tenant Details Save Successfully
        # Then Change The tenant_status Value To True in user Table
        User.objects(user_id=current_user.user_id).update_one(
            set__tenant_id=tenant_id,
            set__tenant_name=tenant_name,
            set__tenant_active=True,
        )


    return redirect(url_for('UserManagement.home_index'))





# View Function For
@TenantManagement.route('/view_all_tenant/<tenant_id>')
def func_get_tenant_list(tenant_id):

    # Get Current User Details


    # Get Tenant Data By API
    tenant_list_request_obj = requests.get('%s/API_bussiness/get_existing_tenant_from_tenantcol'
                                           %API_URL,
                                           params={
                                               'tenant_id':tenant_id
                                           }
                                           )

    # Convert Tenant List Object Into Json
    tenant_list_data = tenant_list_request_obj.json()

    return render_template('tenant_view.html', current_user=current_user, current_app=current_app,
                           tenant_list_data=tenant_list_data)
