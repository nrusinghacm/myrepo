# pylint: disable=no-member, missing-docstring, unused-variable

"""

This File Is For Making Function For Receiving And Sending Data
Created UserManagement Blueprint


"""


# Import All Necessary Modules

import string
import random
from flask_mongoengine import MongoEngine
from flask import Blueprint




# Importing Our Models

from APP import application


# Setup Flask-MongoEngine
db = MongoEngine(application)



# Initialize Blueprint

# UserManagement = Blueprint('UserManagement', __name__)


# This Function Is For Genrating Random Digit For User_ID

def randomStringDigits(stringLength=9):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


# Define the User document.
# NB: Make sure to add flask_user UserMixin
# User Is Act As Collection Object
# User Object Takes Two Arguments db.Document And UserMixin
# db.document Inherit The Class Documetnt In Mongoengine With User Class
# All Field If User Class Is Like A Parameters For Documents
# It Is Necessary To Add All Keys From User Collections To Class Variable Else It Gives Error

class User(db.Document):
    user_id = db.StringField(default=randomStringDigits(stringLength=9))
    active = db.BooleanField(default=True)

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
    roles = db.ListField(db.StringField(), default=['CSE'])

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
    icons =db.StringField(default='')
    tenant_id=db.StringField(default='')
    tenant_name=db.StringField(default='')
    tenant_active = db.BooleanField(default=True)





# Creating Collection Object for User Transaction

class user_transaction(db.Document):
    user_id = db.StringField(default=' ')
    user_name = db.StringField(default=' ')
    dms_Response = db.StringField(default=' ')
    dms_response_Date = db.DateTimeField(default=' ')
    dms_Status = db.StringField(default=' ')
    dms_User_pic_link = db.StringField(default='')


# class User(db.Document):
#     user_id = db.StringField(default=randomStringDigits(stringLength=9))
#     active = db.BooleanField(default=True)
#
#     # User authentication information
#     email = db.StringField(default='')
#     email_confirmed_at = db.DateTimeField()
#
#     username = db.StringField(default='')
#     password = db.StringField()
#
#     phone_number = db.StringField()
#
#
#     # Add New Field As Company
#     company = db.StringField()
#     company_type = db.StringField()
#     company_id = db.StringField()
#     company_location = db.StringField()
#     company_territory = db.StringField()
#     company_region = db.StringField()
#     branch_id = db.StringField()
#     branch_name = db.StringField()
#     department_id = db.StringField()
#     department_name = db.StringField()
#
#
#     # Relationships
#     roles = db.ListField(db.StringField(), default=[])
#
#     # User information
#     first_name = db.StringField(default='')
#     last_name = db.StringField(default='')
#     age = db.IntField(default=00)
#     gender = db.StringField(default='')
#     DoB = db.DateField()
#     city = db.StringField(default='')
#     state = db.StringField(default='')
#     country = db.StringField(default='')
#     postal_pin = db.IntField(default=000000)
#
#     # # # User Other Details
#     # massage = db.ListField(db.ReferenceField(Message), default=[]

