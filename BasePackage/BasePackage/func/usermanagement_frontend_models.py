# pylint: disable=no-member, missing-docstring, unused-variable

"""
This Program Includes All Models Related User Authentication
"""

# Impoer All Necessary Packages

import os
import random
import string
import json
import csv
import requests
from flask import current_app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, FileField  # IntegerField, DateField,
from wtforms.validators import DataRequired

from flask_user.forms import RegisterForm
from flask_user.translation_utils import lazy_gettext as _
from flask_user import login_required, UserManager, UserMixin, roles_required, current_user



# from flask_user.forms import RegisterForm, StringField
# from wtforms.validators import DataRequired
# from os import urandom



# Import From Our Packages

from APP import db
from APP import app
# from APP.Notification.models import Message




#get root path
PATH = app.root_path

# Read Property file For Getting Data

with app.app_context():
    # API_URL = current_app.config['COMPANY_PROPERTY_DATA']['API_details']['api_url']
    API_URL_consumer = current_app.config['COMPANY_PROPERTY_DATA']['API_details']['api_url_consumer']
    API_URL_tenant = current_app.config['COMPANY_PROPERTY_DATA']['API_details']['api_url_tenant']




# Generate Random String
# randomStringDigits Function Generate Random String For User Id

# def create_user_id():
#         # Generate enquiry Id Dynamically
#     generate_user_id = requests.get('%s/API_bussiness/generate_user_id' % API_URL_consumer)

#     # Convert In Json
#     user_id = generate_user_id.json()
#     print(user_id)
#     return user_id


# Define the User document.
# NB: Make sure to add flask_user UserMixin
# User Is Act As Collection Object
# User Object Takes Two Arguments db.Document And UserMixin
# db.document Inherit The Class Documetnt In Mongoengine With User Class
# All Field If User Class Is Like A Parameters For Documents
# It Is Necessary To Add All Keys From User Collections To Class Variable Else It Gives Error

class User(db.Document, UserMixin):

    # user_id = db.StringField(default=create_user_id())
    user_id = db.StringField(default='user_1234')
    active = db.BooleanField(default=False)


    # User authentication information
    email = db.StringField(default='')
    email_confirmed_at = db.DateTimeField()
    username = db.StringField(default='')
    password = db.StringField()
    phone_number = db.StringField()

    # Add New Field As Company
    company = db.StringField()
    company_type = db.StringField()
    company_id = db.StringField()
    company_location = db.StringField()
    company_territory = db.StringField()
    company_region = db.StringField()
    branch_id = db.StringField()
    branch_name = db.StringField()
    department_id = db.StringField()
    department_name = db.StringField()

    # Relationships
    roles = db.ListField(db.StringField(), default=['company_admin']) #CSE

    # User information
    first_name = db.StringField(default='')
    last_name = db.StringField(default='')
    age = db.IntField(default=00)
    gender = db.StringField(default='')
    DoB = db.DateField()
    city = db.StringField(default='')
    state = db.StringField(default='')
    country = db.StringField(default='')
    postal_pin = db.IntField(default=000000)

    dms_Supervisor_Name = db.StringField(default='')
    dms_Designation = db.StringField(default='')
    dms_User_pic_Id = db.StringField(default='')
    dms_User_pic_link = db.StringField(default='')
    dms_WhatsApp_No = db.StringField(default='')
    menus = db.StringField(default='')

    # For Multi tenant solution
    tenant_id = db.StringField(default='')
    tenant_name = db.StringField(default='')
    tenant_active = db.BooleanField(default=False)


    # # # User Other Details
    # massage = db.ListField(db.ReferenceField(Message), default=[]



# Create Form Object For Company Field

class CompanyForm(FlaskForm):
    company = StringField('company', [validators.DataRequired()])
    logo = FileField('logo')


# # Database Objects For Menus And Roles
# class menu_and_roles(db.Document):
#     main_menu = db.StringField()
#     sub_menu = db.StringField()
#     sub_sub_menu = db.DictField()
#     link = db.StringField()
#     role = db.StringField()



# Reading From CSV File And Genratinf manu List For Diff Role

# def func_get_menu_by_roles(role):
#
#     # Get App Root Path
#     path = app.root_path
#
#     # Get File From Folder
#     file_path = os.path.join(path, 'Menus With Roles.csv')
#
#     # Open Csv File Using File Path
#     with open(file_path, 'rt') as file:
#
#         # Read CSV File Using CSV Library
#         data_obj = csv.reader(file)
#
#         # Extract Data Object
#         list_of_val_keys = []
#         for data in data_obj:
#             list_of_val_keys.append(data)
#
#         # close Csv File In Program
#         file.close()
#
#     # Creating Dict
#     list_of_dict = []
#     for da in list_of_val_keys[1:]:
#
#         if role in da:
#             dicts = dict(zip(list_of_val_keys[0], da))
#             # Make List Of Dict
#             list_of_dict.append(dicts)
#
#     return list_of_dict



####################################################################################################
# Adding New Fileds In Registration Form

# Customize the Register form:
from flask_user.forms import RegisterForm
class CustomRegisterForm(RegisterForm):
    # Add a country field to the Register form
    company = StringField(_('Company'), validators=[DataRequired()])



# Customize Flask-User
class CustomUserManager(UserManager):

    def customize(self, app):

        # Configure customized forms
        self.RegisterFormClass = CustomRegisterForm


        # NB: assign:  xyz_form = XyzForm   -- the class!
        #   (and not:  xyz_form = XyzForm() -- the instance!)
#############################################################################################################


# Create Menu In Data In proper Format

# First loop The list of data
# check type is main menu
# then check for level
# based on that create list
# def func_generate_menu(role):
#
#     # Call Function TO Get list Of Dict Based On Role
#     list_of_dict = func_get_menu_by_roles(role)
#
#
#     #Create Final List Of Menus
#     final_menu_list = []
#
#     for menus in list_of_dict:
#
#         list_of_main_menus = []
#
#         # if Type is Main Menu then perform following operatons
#         if menus['Type'] == 'Main Menu':
#
#             list_of_main_menus.append(menus)
#
#             # Make list For sub Menus
#             list_of_sub_menus = []
#
#             # Find Sub Menu
#             for submenus in list_of_dict:
#                 sub_menu = []
#
#                 if submenus['Level'] == '2' and submenus['Parent']== menus['Name']:
#
#                     # Append submenus dict to sub_menu list
#                     sub_menu.append(submenus)
#
#                     sub_sub_menu = []
#                     # find sub sub menu
#                     for sub_submenu in list_of_dict:
#
#                         # Chake For Level 3
#                         if sub_submenu['Level'] == '3' and sub_submenu['Parent']== submenus['Name']:
#
#                             sub_sub_menu.append(sub_submenu)
#
#                     # append subsub menu in submenu list
#                     sub_menu.append(sub_sub_menu)
#
#                     # Append All Submenus In List
#                     list_of_sub_menus.append(sub_menu)
#
#             # Append Sub Menus List To Menus List
#             list_of_main_menus.append(list_of_sub_menus)
#
#             # append All list of main menus in final list
#             final_menu_list.append(list_of_main_menus)
#
#     return final_menu_list
#
# a = func_generate_menu('Dealer')
# print(a)

# a = func_generate_menu('CSE Admin')
# print(a)







# # Logic For Dynamic Menu Generation
# # This Function Create Menu Based On Roles
# def func_get_menus_based_on_roles(roles):
#
#     # List Of Menus Data
#     menu_data = []
#
#     # Find Menu Based on Role
#     for role in roles:
#         database_find_obj = menu_and_roles.objects(role=role)
#
#         # Extract Data From Database Find Obj
#         for data in database_find_obj:
#             data_dict = {}
#             data_dict['main_menu'] = data.main_menu
#             data_dict['sub_menu'] = data.sub_menu
#             data_dict['sub_sub_menu'] = data.sub_sub_menu
#             data_dict['link'] = data.link
#             data_dict['role'] = data.role
#
#             # For Avoiding Dublicates
#             if data_dict not in menu_data:
#                 menu_data.append(data_dict)
#
#     return menu_data
#
#
# data = func_get_menus_based_on_roles(['SKF Leader'])
# print(data)



# This Function Is For Managing Menu Elements Based On Roles
# First Store All Menu Elements In List
# Then Giving Permission To User Based On Role
# Expected Output Is Getting List Of Menus According To Roles Of User

# def func_get_menu(roles):
#
#     # Storing All Menus In List
#     # list_of_menus = ['Dashboard','Load Management','Opportunity Management',
#     # 'Investment Management','Company Sentry','Super Admin','Complaint module',
#     # 'Primary Sales','Secondary Sales','Loyality','Dealer management','']
#
#     dict_of_submenus = {'Dashboard':[['Dashboard', '/super_admin_dashboard', ['Super Admin']],
#                                      ['Dealer Dashboard', '/dealer_dashboard', ['Super Admin']],
#                                      ['Sales Dashboard', '/aftermarket_sales_dashboard', ['SKF Leader']],
#                                      ['CSE Dashboard', '/cse_dashboard', ['CSM']],
#                                      ['CSH Dashboard', '/complaint_csh_dashboard', ['CSM']],
#                                      ['Dealer Dashboard',
#                                       '/dealer_dashboard', ['CSM']],
#                                      ['My Dashboard', '/dealer_dashboard', ['Dealer']]],
#                         'Primary Sales':[['Order Dashboard', '/primary_sales', ['SKF Leader']],
#                                          ['Order Dashboard', '/primary_sales', ['CSM']]],
#                         'Aftermarket Sales':[['Aftermarket Sales Dashboard', '/aftermarket_sales_dashboard',
#                                               ['SKF Leader']],
#                                              ['Aftermarket Sales Dashboard',
#                                               '/aftermarket_sales_dashboard',
#                                               ['CSM']],
#                                              ['Aftermarket Sales', '/secondary_sales_read',
#                                               ['SKF Leader']],
#                                              ['Aftermarket Sales', '/secondary_sales_read',
#                                               ['CSM']]
#                                              ],
#                         'Complaint Management':[['Complaints Dashboard', '/complaint_csh_dashboard',
#                                                  ['SKF Leader']],
#                                                 ['Complaints Dashboard', '/cse_dashboard',
#                                                  ['CSM']],
#                                                 ['Complaint Dashboard', '/complaint_dealer_dashboard',
#                                                  ['Dealer']],
#                                                 ['Complaints', '/complaint_data_by_type/0/50',
#                                                  ['SKF Leader']],
#                                                 ['Complaints', '/complaint_data_by_type/0/50',
#                                                  ['CSM']],
#                                                 ['My Complaints',
#                                                  '/complaint_data_by_type/0/50',
#                                                  ['Dealer']],
#
#                                                 ['Create Complaint', '/complaint_create_page',
#                                                  ['Dealer']]
#                                                 ],
#                         'Loyalty Management':[['Loyalty Dashboard', '/loyalty_dashboard', ['Dealer']],
#                                               ['Loyalty Dashboard', '/loyalty_dashboard', ['SKF Leader']],
#                                               ['My Loyalty', '/my_loyalty', ['Dealer']],
#                                               ['My Loyalty', '/my_loyalty', ['SKF Leader']],
#                                               ['Claim Loyalty', '/claim_loyalty', ['Dealer']],
#                                               ['Claim Loyalty', '/claim_loyalty', ['SKF Leader']],
#                                               ['My Payout Report', '/manage_target/skf_dealer_incentive_payout', ['Dealer']],
#                                               ['My Payout Report', '/manage_target/skf_dealer_incentive_payout', ['SKF Leader']],
#                                               ['Loyalty Dashboard', '/loyalty_dashboard', ['Millston']]],
#                         'Enquiry':[
#                                    ['Enquiry Dashboard', '/enquiry_csh_dashboard', ['SKF Leader']],
#                                    ['Enquiry Dashboard', '/enquiry_csh_dashboard', ['CSM']],
#
#                                    ['Enquiry Dashboard', '/enquiry_dealer_dashboard', ['Dealer']],
#                                    ['Enquiries', '/view_enquiry_data', ['SKF Leader']],
#                                    ['Enquiries', '/view_enquiry_data',
#                                     ['Dealer']],
#                                    ['Enquiries', '/view_enquiry_data', ['CSM']],
#
#                                    ['Create Enquiry', '/enquiry_create_page', ['SKF Leader']],
#                                    ['Create Enquiry', '/enquiry_create_page', ['CSM']],
#                                    ['Create Enquiry', '/enquiry_create_page', ['Dealer']]
#                                    ],
#                         'Sales':[['Customers', '/Customers', ['Dealer']],
#                                  ['Sales Engineers', '/sales_engineers', ['Dealer']],
#                                  ['Leads', '/lead', ['Dealer']],
#                                  ['Opportunity', '/opportunity', ['Dealer']],
#                                  ['Sales', '/view_primary_sales', ['Dealer']]],
#
#                         'Company Settings':[['Manage Activity',
#                                              '/comapany_settings_manage_activity', ['SKF Leader']],
#                                             ['Define Target', '/company_settings_define_target',
#                                              ['SKF Leader']],
#                                             ['Incentive Wizard', 'loyalty_process_page',
#                                              ['SKF Leader']],
#                                             ['Incentive Wizard', 'loyalty_process_page',
#                                              ['CSM']]
#                                             ],
#
#                         'Document':[['Documents',
#                                              'http://docs.confluex.me/knowledgebase.html',
#                                      ['Dealer']],
#
#
#
#                                      ['Documents','http://docs.confluex.me/knowledgebase.html', ['CSM']] ],
#
#
#
#
#
#                         'Incentive Management':[['Set Incentive', '/set_incentive_create_page',
#                                                  ['SKF Leader']],
#
#                                                 ['Set Target Details', '/set_target_detail',
#                                                  ['SKF Leader']],
#
#
#                                                 ['Manage Target', '/manage_target', ['SKF Leader']]],
#
#                         'Secondary Sales':[['Sales Dashboard', '/Secondary_sales', ['Dealer']],
#                                         ['Secondary Sales','/SecondarySales_list', ['Dealer']],
#                                         ['Create Secondary Sales','/SecondarySales_create', ['Dealer']],
#                                         ['Sales Dashboard', '/Secondary_sales', ['SKF Leader']],
#                                         ['Secondary Sales','/SecondarySales_list', ['SKF Leader']],
#                                         ['Create Secondary Sales','/SecondarySales_create', ['SKF Leader']]],
#
#                         'Master Management':[['Region','#', ['Dealer']],
#                         ['Territory','#', ['Dealer']],
#                         ['Country','#', ['Dealer']],
#                         ['State','#', ['Dealer']],
#                         ['Department','#', ['Dealer']],
#                         ['Account','#', ['Dealer']],
#                         ['Company','#', ['Dealer']],
#                         ['Branch','#', ['Dealer']],
#                         ['IPS','#', ['Dealer']],
#                         ['Salary','#', ['Dealer']],
#                         ['Platform','#', ['Dealer']],
#                         ['Bussiness Unit','#', ['Dealer']],
#                         ['QuoteLog Stats','#', ['Dealer']],
#                         ['Engineer Role','#', ['Dealer']]
#                         ],
#
#                         'Leader Insights': [['Dashboard', '/leader_bulletin',
#                                                  ['SKF Leader']]],
#                          'Sales Insights': [['Dashboard','/sales_bulletin_insight',['SKF Leader']]],
#
#                         'Opportunity Mangement': [['Opportunity Dashboard', '/opportunity_dashboard', ['Dealer']],
#                                                  ['My Opportunities', '/opty_list', ['Dealer']],
#                                                  ['Create Opportunity', '/opty_create', ['Dealer']],
#                                                  ['Opportunity Dashboard', '/opportunity_dashboard',  ['SKF Leader']],
#                                                  ['My Opportunity', '/opty_list',  ['SKF Leader']],
#                                                  ['Create Opportunity', '/opty_create',  ['SKF Leader']]],
#
#                          'Lead Management': [['Lead Dashboard', '/lead_dashboard', ['Dealer']],
#                                              ['My Leads', '/lead_list', ['Dealer']],
#                                              ['Create Lead', '/lead_create', ['Dealer']]],
#                          'Claims Management':[['Claims Dashboard', '/claims_dashboard', ['Dealer']],
#                                               ['Salary Claims', '/salaryclaim_list', ['Dealer']],
#                                               ['Other Claims', '/claims_list', ['Dealer']],
#                                              ['Create Claims', '/claims_create', ['Dealer']],
#                                              ['Claims Dashboard', '/claims_dashboard', ['SKF Leader']],
#                                               ['Other Claims', '/claims_list', ['SKF Leader']],
#                                                ['Salary Claims', '/salaryclaim_list', ['SKF Leader']],
#                                              ['Create Claims', '/claims_create', ['SKF Leader']]],
#                          'Customer Management':[['Customer Dashboard', '/customer_dashboard', ['SKF Leader']],
#                                               ['My Customers', '/customer_list', ['Dealer']],
#                                              ['Create Customer', '/customer_create', ['Dealer']]],
#                          'Employee Management':[['My Employees', '/emp_list', ['Dealer']],
#                                              ['Create Employee', '/emp_create', ['Dealer']]],
#                          'News Management' :[['My News', '/news_list', ['Dealer']],
#                                              ['Create News', '/news_create', ['Dealer']],
#                                              ['My News', '/news_list', ['SKF Leader']],
#                                              ['Create News', '/news_create', ['SKF Leader']]],
#
#                          'Order Management':[['Order Dashboard', '/order_dashboard', ['Dealer']],
#                                               ['My Orders', '/order_list', ['Dealer']],
#                                              ['Create Order', '/order_create', ['Dealer']]],
#
#                          'Sales Engineer':[['Sales Engineer Dashboard', '#', ['Dealer']],
#                                               ['My Sales Engineers', '/engineer_list', ['Dealer']],
#                                              ['Create Sales Engineer', '/engineer_create', ['Dealer']],
#                                              ['Sales Engineer Dashboard', '#', ['SKF Leader']],
#                                               ['My Sales Engineers', '/engineer_list', ['SKF Leader']],
#                                              ['Create Sales Engineer', '/engineer_create', ['SKF Leader']]],
#
#
#
#
#                         }
#
#
#
#     # [['Manage Loyalty Logic', '/manage_incentive_manage_loyalty_logic', ['SKF Leader']],
#     #  ['View Incentive', '/manage_incentive_view_incentive', ['SKF Leader']],
#     #  ['Set Incentive', '/manage_incentive_set_incentive', ['SKF Leader']],
#     #  ['Set TopUp Rewards', '/manage_incentive_set_topup_reward', ['SKF Leader']],
#     #  ['Set Consistent Award', '/manage_incentive_set_consistent_award', ['SKF Leader']],
#
#
#
#      # New List Of Menus
#     list_of_menus = ['Dashboard', 'Sales (SKF)', 'Sales (Dealer)', 'Aftermarket Sales','Leader Insights','Sales Insights',
#                      'Dealer Management', 'Complaint Management', 'Enquiry Management', 'Company Settings','Secondary Sales','Incentive Management','Sales Engineer','Opportunity Mangement','Lead Management','Claims Management','Customer Management','Order Management','Employee Management','News Management', 'Loyalty Management']
#
#
#
#
#     # Getting Roles Of User
#     roles = roles
#     print(roles)
#
#     # Selecting List Of Menus Base On Roles
#     for menu, sub_menu in dict_of_submenus.items():
#         if 'Super Admin' in roles:
#             list_of_menus = ['Dashboard']
#         elif 'SKF Leader' in roles:
#             list_of_menus = ['Dashboard', 'Complaint Management', 'Enquiry','Opportunity Mangement','Secondary Sales','Claims Management','Sales Engineer','News Management','Loyalty Management','Leader Insights','Sales Insights','Master Management','Document']
#         elif 'Dealer' in roles:
#             list_of_menus = ['Dashboard', 'Complaint Management', 'Enquiry','Opportunity Mangement','Secondary Sales','Claims Management','Loyalty Management','Sales Engineer','Document']
#         elif 'Dealer_branch' in roles:
#             list_of_menus = ['Dashboard', 'Complaint Management', 'Enquiry','Opportunity Mangement','Secondary Sales','Claims Management','Loyalty Management','Sales Engineer','Document']
#         elif 'CSE' in roles:
#             list_of_menus = ['Dashboard', 'Complaint Management', 'Enquiry','Opportunity Mangement','Secondary Sales','Claims Management','Loyalty Management','Sales Engineer','Document']
#         elif 'CSM' in roles:
#             list_of_menus = ['Dashboard', 'Complaint Management','Enquiry', 'Document']
#
#         elif 'skf_customer_support' in roles:
#             list_of_menus = ['Dashboard', 'Dealer Management', 'Complaint Management',
#                              'Enquiry ', 'Management']
#         elif 'skf_dealer_management' in roles:
#             list_of_menus = ['Dashboard', 'Sales (Dealer)', 'Complaint Management',
#                              'Enquiry ', 'Management']
#         elif 'skf_dealer_management - 2' in roles:
#             list_of_menus = ['Complaint Management', 'Enquiry Management']
#
#         else:
#             list_of_menus = ['Dashboard']
#
#     return list_of_menus, dict_of_submenus


def func_get_menu1(roles):
    # Storing All Menus In List
    # list_of_menus = ['Dashboard','Load Management','Opportunity Management',
    # 'Investment Management','Company Sentry','Super Admin','Complaint module',
    # 'Primary Sales','Secondary Sales','Loyality','Dealer management','']

    dict_of_submenus = {'Dashboard': [['Dashboard', '/super_admin_dashboard', ['Super Admin']],
                                      ['Dealer Dashboard', '/dealer_dashboard', ['Super Admin']],
                                      ['Sales Dashboard', '/aftermarket_sales_dashboard', ['SKF Leader']],
                                      ['CSE Dashboard', '/cse_dashboard', ['CSM']],
                                      ['CSH Dashboard', '/complaint_csh_dashboard', ['CSM']],
                                      ['Dealer Dashboard',
                                       '/dealer_dashboard', ['CSM']],
                                      ['My Dashboard', '/dealer_dashboard', ['Dealer']]],

                        'Primary Sales': [['Order Dashboard', '/primary_sales', ['SKF Leader']],
                                          ['Order Dashboard', '/primary_sales', ['CSM']]],

                        'Aftermarket Sales': [['Aftermarket Sales Dashboard', '/aftermarket_sales_dashboard',
                                               ['SKF Leader']],
                                              ['Aftermarket Sales Dashboard',
                                               '/aftermarket_sales_dashboard',
                                               ['CSM']],
                                              ['Aftermarket Sales', '/secondary_sales_read',
                                               ['SKF Leader']],
                                              ['Aftermarket Sales', '/secondary_sales_read',
                                               ['CSM']]
                                              ],
                        'Complaint Management': [['Complaints Dashboard', '/complaint_csh_dashboard',
                                                  ['SKF Leader']],
                                                 ['Complaints Dashboard', '/cse_dashboard',
                                                  ['CSM']],
                                                 ['Complaints Dashboard', '/cse_dashboard',
                                                  ['CSE']],

                                                 ['Complaint Dashboard', '/complaint_dealer_dashboard',
                                                  ['Dealer']],
                                                 ['Complaint Dashboard', '/complaint_dealer_dashboard',
                                                  ['Dealer_Branch']],
                                                 ['Complaints', '/complaint_data_by_type/0/50',
                                                  ['SKF Leader']],
                                                 ['Complaints', '/complaint_data_by_type/0/50',
                                                  ['CSM']],
                                                 ['Complaints', '/complaint_data_by_type/0/50',
                                                  ['CSE']],
                                                 ['My Complaints',
                                                  '/complaint_data_by_type/0/50',
                                                  ['Dealer']],
                                                 ['My Complaints',
                                                  '/complaint_data_by_type/0/50',
                                                  ['Dealer_Branch']],

                                                 ['Create Complaint', '/complaint_create_page',
                                                  ['Dealer']],
                                                 ['Create Complaint', '/complaint_create_page',
                                                  ['Dealer_Branch']],
                                                 ['Create Complaint', '/complaint_create_page',
                                                  ['CSE']]
                                                 ],
                        'Loyalty Management': [['Loyalty Dashboard', '/loyalty_dashboard', ['Dealer']],
                                               ['Loyalty Dashboard', '/loyalty_dashboard', ['Dealer_Branch']],

                                               ['Loyalty Dashboard', '/loyalty_dashboard', ['SKF Leader']],
                                               ['My Loyalties', '/my_loyalty', ['Dealer']],
                                               ['My Loyalties', '/my_loyalty', ['Dealer_Branch']],
                                               ['My Loyalties', '/my_loyalty', ['SKF Leader']],
                                               ['Claim Loyalty', '/claim_loyalty', ['Dealer']],
                                               ['Claim Loyalty', '/claim_loyalty', ['Dealer_Branch']],

                                               ['Claim Loyalty', '/claim_loyalty', ['SKF Leader']],
                                               ['My Payout Report', '/manage_target/skf_dealer_incentive_payout', ['Dealer']],
                                               ['My Payout Report', '/manage_target/skf_dealer_incentive_payout', ['Dealer']],
                                               ['My Payout Report', '/manage_target/skf_dealer_incentive_payout', ['SKF Leader']],
                                               ['Loyalty Dashboard', '/loyalty_dashboard', ['Millston']]],
                        'Enquiry': [
                            ['Enquiry Dashboard', '/enquiry_csh_dashboard', ['SKF Leader']],
                            ['Enquiry Dashboard', '/enquiry_csh_dashboard', ['CSM']],

                            ['Enquiry Dashboard', '/enquiry_dealer_dashboard', ['Dealer']],
                            ['Enquiry Dashboard', '/enquiry_dealer_dashboard', ['Dealer_Branch']],

                            ['Enquiry & General Enquiries', '/view_enquiry_data', ['SKF Leader']],
                            ['Enquiry & General Enquiries', '/view_enquiry_data', ['Dealer']],
                            ['Enquiry & General Enquiries', '/view_enquiry_data', ['CSM']],
                            ['Enquiry & General Enquiries', '/view_enquiry_data', ['CSE']],
                            ['Enquiry & General Enquiries', '/view_enquiry_data', ['Dealer_Branch']],

                            ['Order Enquiries', '/view_order_enquiry', ['SKF Leader']],
                            ['Order Enquiries', '/view_order_enquiry', ['Dealer']],
                            ['Order Enquiries', '/view_order_enquiry', ['Dealer_Branch']],
                            ['Order Enquiries', '/view_order_enquiry', ['CSM']],
                            ['Order Enquiries', '/view_order_enquiry', ['CSE']],

                            ['Create Enquiry', '/enquiry_create_page', ['SKF Leader']],
                            ['Create Enquiry', '/enquiry_create_page', ['CSM']],
                            ['Create Enquiry', '/enquiry_create_page', ['CSE']],
                            ['Create Enquiry', '/enquiry_create_page', ['Dealer']],
                            ['Create Enquiry', '/enquiry_create_page', ['Dealer_Branch']]

                        ],

                        'Sales': [['Customers', '/Customers', ['Dealer']],
                                  ['Sales Engineers', '/sales_engineers', ['Dealer']],
                                  ['Leads', '/lead', ['Dealer']],
                                  ['Opportunities', '/opportunity', ['Dealer']],
                                  ['Sales', '/view_primary_sales', ['Dealer']]],

                        'Company Settings': [['Manage Activities',
                                              '/comapany_settings_manage_activity', ['SKF Leader']],
                                             ['Define Target', '/company_settings_define_target',
                                              ['SKF Leader']],
                                             ['Incentive Wizard', 'loyalty_process_page',
                                              ['SKF Leader']],
                                             ['Incentive Wizard', 'loyalty_process_page',
                                              ['CSM']]
                                             ],

                        'Document': [['Documents',
                                      'http://docs.confluex.me/knowledgebase.html',
                                      ['Dealer']],
                                     ['Documents',
                                      'http://docs.confluex.me/knowledgebase.html',
                                      ['Dealer_Branch']],
                                     ['Documents',
                                      'http://docs.confluex.me/knowledgebase.html',
                                      ['CSE']],

                                     ['Documents', 'http://docs.confluex.me/knowledgebase.html', ['CSM']]],

                        'Incentive Management': [['Set Incentive', '/set_incentive_create_page',
                                                  ['SKF Leader']],

                                                 ['Set Target Details', '/set_target_detail',
                                                  ['SKF Leader']],

                                                 ['Manage Target', '/manage_target', ['SKF Leader']]],

                        'Secondary Sales': [['Sales Dashboard', '/Secondary_sales', ['Dealer']],
                                            ['Secondary Sales', '/SecondarySales_list', ['Dealer']],
                                            ['Create Secondary Sales', '/SecondarySales_create', ['Dealer']],
                                            ['Sales Dashboard', '/Secondary_sales', ['Dealer_Branch']],
                                            ['Secondary Sales', '/SecondarySales_list', ['Dealer_Branch']],
                                            ['Create Secondary Sales', '/SecondarySales_create', ['Dealer_Branch']],

                                            ['Sales Dashboard', '/Secondary_sales', ['SKF Leader']],
                                            ['Secondary Sales', '/SecondarySales_list', ['SKF Leader']],
                                            ['Create Secondary Sales', '/SecondarySales_create', ['SKF Leader']]],

                        'Master Management': [['Region', '#', ['Dealer']],
                                              ['Territory', '#', ['Dealer']],
                                              ['Country', '#', ['Dealer']],
                                              ['State', '#', ['Dealer']],
                                              ['Department', '#', ['Dealer']],
                                              ['Account', '#', ['Dealer']],
                                              ['Company', '#', ['Dealer']],
                                              ['Branch', '#', ['Dealer']],
                                              ['IPS', '#', ['Dealer']],
                                              ['Salary', '#', ['Dealer']],
                                              ['Platform', '#', ['Dealer']],
                                              ['Bussiness Unit', '#', ['Dealer']],
                                              ['QuoteLog Stats', '#', ['Dealer']],
                                              ['Engineer Role', '#', ['Dealer']]
                                              ],

                        'Leader Insights': [['Dashboard', '/leader_bulletin',
                                             ['SKF Leader']]],
                        'Sales Insights': [['Dashboard', '/sales_bulletin_insight', ['SKF Leader']]],

                        'Opportunity Mangement': [['Opportunity Dashboard', '/opportunity_dashboard', ['Dealer']],
                                                  ['My Opportunities', '/opty_list', ['Dealer']],
                                                  ['Create Opportunity', '/opty_create', ['Dealer']],

                                                  ['Opportunity Dashboard', '/opportunity_dashboard', ['Dealer_Branch']],
                                                  ['My Opportunities', '/opty_list', ['Dealer_Branch']],
                                                  ['Create Opportunity', '/opty_create', ['Dealer_Branch']],

                                                  ['Opportunity Dashboard', '/opportunity_dashboard', ['SKF Leader']],
                                                  ['My Opportunities', '/opty_list', ['SKF Leader']],

                                                  ['Create Opportunity', '/opty_create', ['SKF Leader']]],

                        'Lead Management': [['Lead Dashboard', '/lead_dashboard', ['Dealer']],
                                            ['My Leads', '/lead_list', ['Dealer']],
                                            ['Create Lead', '/lead_create', ['Dealer']]],

                        'Claims Management': [['Claims Dashboard', '/claims_dashboard', ['Dealer']],
                                              ['Salary Claims', '/salaryclaim_list', ['Dealer']],
                                              ['Other Claims', '/claims_list', ['Dealer']],
                                              ['Create Claims', '/claims_create', ['Dealer']],
                                              ['Create Salary Claims', '/salaryclaim_create', ['Dealer']],

                                              ['Claims Dashboard', '/claims_dashboard', ['Dealer_Branch']],
                                              ['Salary Claims', '/salaryclaim_list', ['Dealer_Branch']],
                                              ['Other Claims', '/claims_list', ['Dealer_Branch']],
                                              ['Create Claims', '/claims_create', ['Dealer_Branch']],
                                              ['Create Salary Claims', '/salaryclaim_create', ['Dealer_Branch']],

                                              ['Claims Dashboard', '/claims_dashboard', ['SKF Leader']],
                                              ['Other Claims', '/claims_list', ['SKF Leader']],
                                              ['Salary Claims', '/salaryclaim_list', ['SKF Leader']],
                                              ['Create Claims', '/claims_create', ['SKF Leader']],
                                              ['Create Salary Claims', '/salaryclaim_create', ['SKF Leader']]],
                        'Customer Management': [['Customer Dashboard', '/customer_dashboard', ['SKF Leader']],
                                                ['My Customers', '/customer_list', ['Dealer']],
                                                ['Create Customer', '/customer_create', ['Dealer']]],
                        'Employee Management': [['My Employees', '/emp_list', ['Dealer']],
                                                ['Create Employee', '/emp_create', ['Dealer']]],
                        'News Management': [['My News', '/news_list', ['Dealer']],
                                            ['Create News', '/news_create', ['Dealer']],
                                            ['My News', '/news_list', ['SKF Leader']],
                                            ['Create News', '/news_create', ['SKF Leader']]],

                        'Order Management': [['Order Dashboard', '/order_dashboard', ['Dealer']],
                                             ['My Orders', '/order_list', ['Dealer']],
                                             ['Create Order', '/order_create', ['Dealer']]],

                        'Sales Engineer': [['Sales Engineer Dashboard', '#', ['Dealer']],
                                           ['My Sales Engineers', '/engineer_list', ['Dealer']],
                                           ['Create Sales Engineer', '/engineer_create', ['Dealer']],
                                           ['Sales Engineer Dashboard', '#', ['Dealer_Branch']],
                                           ['My Sales Engineers', '/engineer_list', ['Dealer_Branch']],
                                           ['Create Sales Engineer', '/engineer_create', ['Dealer_Branch']],

                                           ['Sales Engineer Dashboard', '#', ['SKF Leader']],
                                           ['My Sales Engineers', '/engineer_list', ['SKF Leader']],
                                           ['Create Sales Engineer', '/engineer_create', ['SKF Leader']]],

                        }

    # [['Manage Loyalty Logic', '/manage_incentive_manage_loyalty_logic', ['SKF Leader']],
    #  ['View Incentive', '/manage_incentive_view_incentive', ['SKF Leader']],
    #  ['Set Incentive', '/manage_incentive_set_incentive', ['SKF Leader']],
    #  ['Set TopUp Rewards', '/manage_incentive_set_topup_reward', ['SKF Leader']],
    #  ['Set Consistent Award', '/manage_incentive_set_consistent_award', ['SKF Leader']],

    # New List Of Menus
    list_of_menus = ['Dashboard', 'Sales (SKF)', 'Sales (Dealer)', 'Aftermarket Sales', 'Leader Insights', 'Sales Insights',
                     'Dealer Management', 'Complaint Management', 'Enquiry Management', 'Company Settings', 'Secondary Sales', 'Incentive Management', 'Sales Engineer', 'Opportunity Mangement', 'Lead Management', 'Claims Management', 'Customer Management', 'Order Management', 'Employee Management',
                     'News Management', 'Loyalty Management']

    # Getting Roles Of User
    roles = roles
    print(roles)

    # Selecting List Of Menus Base On Roles
    for menu, sub_menu in dict_of_submenus.items():
        if 'Super Admin' in roles:
            list_of_menus = ['Dashboard']
        elif 'SKF Leader' in roles:
            list_of_menus = ['Dashboard', 'Complaint Management']
        elif 'Dealer' in roles:
            list_of_menus = ['Dashboard', 'Complaint Management', 'Enquiry', 'Opportunity Mangement', 'Secondary Sales', 'Claims Management', 'Loyalty Management', 'Sales Engineer', 'Document']
        elif 'CSM' in roles:
            list_of_menus = ['Dashboard', 'Complaint Management', 'Enquiry', 'Document']

        elif 'CSE' in roles:
            list_of_menus = ['Dashboard', 'Complaint Management', 'Enquiry', 'Document']
        elif 'Dealer_Branch' in roles:
            list_of_menus = ['Dashboard', 'Complaint Management', 'Enquiry', 'Opportunity Mangement', 'Secondary Sales', 'Claims Management', 'Loyalty Management', 'Sales Engineer', 'Document']
        elif 'skf_dealer_management - 2' in roles:
            list_of_menus = ['Complaint Management', 'Enquiry Management']

        else:
            list_of_menus = ['Dashboard']

    return list_of_menus, dict_of_submenus


# list_of_menus, dict_of_submenus = func_get_menu1(['Dealer'])
# print(func_get_menu)




# Create Menu list of dict in database format form above menu dict
def get_new_menus_structure(roles, main_menus, submenus):

    # Create Final List
    list_of_final_menu = []


    # loop Through Main Menu List
    for main in main_menus:

        # get submenu data for main menu
        list_of_sub_menus = submenus[main]


        # loop throught submenu list
        for sub in list_of_sub_menus:


            # Map With Roles
            if roles[0] in sub[2]:

                # Create Tmp Dict
                dic = {}

                dic['main_menu'] = main
                dic['sub_menu'] = sub[0]
                dic['sub_sub_menu'] = []
                dic['link'] = sub[1]

                print(dic)

                list_of_final_menu.append(dic)

    return list_of_final_menu




# Save Current User Menu In Database
def save_menu_in_database(user_id, roles):

    # print(user_id)
    # print(roles)


    # Get MEnu form Old Struct
    list_of_menus, dict_of_submenus = func_get_menu1(roles)
    # print(list_of_menus)
    # print(dict_of_submenus)

    # Call Function For Getting Menu For Current User With Argument Of List Of Menu Amd Submenus
    menu_struct = get_new_menus_structure(roles, list_of_menus, dict_of_submenus)
    # print(menu_struct)

    # Convert Menu Struct Into String
    menus = json.dumps(menu_struct)


    # Update User Menu
    User.objects(user_id=user_id).update_one(
        set__menus=menus
    )

    return 'Success'





#  get current user menu based

def func_get_menu(usr):

    # Get Current User
    user = usr

    # Get Menu For Current User
    menus = user.menus

    #Convert Menus String TO Python Object
    menus_object = json.loads(menus)

    # Get distinct Main Menus For menus_object
    list_of_main_menu = []

    for i in menus_object:

        if i['main_menu'] not in list_of_main_menu:

            list_of_main_menu.append(i['main_menu'])


    return list_of_main_menu, menus_object



