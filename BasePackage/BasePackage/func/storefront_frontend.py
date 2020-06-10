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



# API_URL_tenant = 'http://127.0.0.1:8001'
# API_URL_consumer = 'http://127.0.0.1:8000'




# home page function
def home_page(Page_id, tenant_id, company_id, visit_id, API_URL_consumer, API_URL_tenant):
# def home():

    pg_compnt_list1 = requests.get('%s/API_bussiness/get_och_page_component_data'
                        % API_URL_consumer, params={'Page_id':'PG_1001'})
                        # % API_URL_consumer, params={'Page_id':Page_id})
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

# function for add to cart 
def add_to_cart1(Page_id, tenant_id, company_id, visit_id,API_URL_consumer, API_URL_tenant):
    # Get Today's Date
    StartDate = datetime.now()

    # Generate cart Id Dynamically
    generate_cart_id = requests.get('%s/API_bussiness/generate_add_to_cart_id' % API_URL_consumer)

    # Convert In Json
    cart_id = generate_cart_id.json()

    try:
        print("try Part")
        print('visit_id:',visit_id)
        if visit_id:
            product_list = requests.get('%s/API_bussiness/get_cart_data'
                                % API_URL_tenant, params={'visit_id' :visit_id})
        else:
            product_list = requests.get('%s/API_bussiness/get_cart_data'
                                % API_URL_tenant, params={'user_id':user_id})
        prod_list = product_list.json()
        key_counts = Counter(d['prd_SKU_ID'] for d in prod_list)
        
        if len(prod_list) == 0:
            # Sent Post Request To Create add_to_cart Endoint
            # try:
            create_request_obj = requests.post('%s/API_bussiness/save_add_to_cart_data'
                                                    %API_URL_tenant, params={
                                                            'cart_id' : cart_id,
                                                            'user_entered_qty' : 1,
                                                            'prd_SKU_ID' : request.form['ui_prd_SKU_ID'],
                                                            'prd_Product_Title' : request.form['ui_prd_Product_Title'],
                                                            'prd_MRP' : float(request.form['ui_prd_MRP']),
                                                            'prd_Standard_Price' : float(request.form['ui_prd_Standard_Price']),
                                                            'prd_Qty' : request.form['ui_prd_Qty'],
                                                            'prd_Main_View_Image' : request.form['ui_prd_Main_View_Image'],
                                                            # 'user_id' : user_id,
                                                            'cart_Entry_Date' : StartDate,
                                                            'visit_id' : visit_id,
                                                            'status' : "New",
                                                            'tenant_id' : tenant_id,
                                                            'company_id' : company_id,
                                                            })

            #     flash('Your cart Has Been done SuccessFully', 'info')
            # except Exception as e :
            #     # print(e)
            #     flash('Your cart Has Been Not done SuccessFully', 'error')
        else:
            for i in prod_list:
                SKU_ID = i['prd_SKU_ID']
                entered_qty = i['user_entered_qty']

            prd_id = request.form['ui_prd_SKU_ID']
            
            for d in prod_list:
               
                if key_counts[prd_id] >= 1:
                    
                    # Sent Post Request To Create add_to_cart Endoint 
                    # try:
                    create_request_obj = requests.put('%s/API_bussiness/update_add_to_cart_data'
                                                            %API_URL_tenant, params={
                                                                    'cart_id' : cart_id,
                                                                    'user_entered_qty' : int(entered_qty)+1,
                                                                    'prd_SKU_ID' : request.form['ui_prd_SKU_ID'],
                                                                    # 'prd_Product_Title' : request.form['ui_prd_Product_Title'],
                                                                    # 'prd_MRP' : float(request.form['ui_prd_MRP']),
                                                                    # 'prd_Standard_Price' : float(request.form['ui_prd_Standard_Price']),
                                                                    # 'prd_Qty' : request.form['ui_prd_Qty'],
                                                                    # 'prd_Main_View_Image' : request.form['ui_prd_Main_View_Image'],
                                                                    # 'user_id' : user_id,
                                                                    # 'cart_Entry_Date' : StartDate,
                                                                    'visit_id' : visit_id,
                                                                    'status' : "New"
                                                                    })
                    # print('if create_request_obj ::', create_request_obj.json())
                    if create_request_obj.json()['Response'] == 'product Updated to cart Sucssesfully':
                        break
                    
                    #     flash('Your cart Has Been done SuccessFully', 'info')
                    # except Exception as e :
                    #     # print(e)
                    #     flash('Your cart Has Been Not done SuccessFully', 'error')
                else:
                    
                    # Sent Post Request To Create add_to_cart Endoint
                    # try:
                    create_request_obj = requests.post('%s/API_bussiness/save_add_to_cart_data'
                                                            %API_URL_tenant, params={
                                                                    'cart_id' : cart_id,
                                                                    'user_entered_qty' : 1,
                                                                    'prd_SKU_ID' : request.form['ui_prd_SKU_ID'],
                                                                    'prd_Product_Title' : request.form['ui_prd_Product_Title'],
                                                                    'prd_MRP' : float(request.form['ui_prd_MRP']),
                                                                    'prd_Standard_Price' : float(request.form['ui_prd_Standard_Price']),
                                                                    'prd_Qty' : request.form['ui_prd_Qty'],
                                                                    'prd_Main_View_Image' : request.form['ui_prd_Main_View_Image'],
                                                                    # 'user_id' : user_id,
                                                                    'cart_Entry_Date' : StartDate,
                                                                    'visit_id' : visit_id,
                                                                    'status' : "New",
                                                                    'tenant_id' : tenant_id,
                                                                    'company_id' : company_id,
                                                                    })
                    # print('else create_request_obj ::', create_request_obj.json())
                    if create_request_obj.json()['Response'] == 'One product added to cart Sucssesfully':
                        break
                    #     flash('Your cart Has Been done SuccessFully', 'info')
                    # except Exception as e :
                    #     # print(e)
                    #     flash('Your cart Has Been Not done SuccessFully', 'error')


    except:
        print("except part")
       

    if visit_id:
        product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={'visit_id' :visit_id,
                                                        'tenant_id' : tenant_id})
    else:
        product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={'user_id':user_id})
    prod_list = product_list.json()

    return prod_list


def cart(Page_id, tenant_id, company_id, visit_id, API_URL_consumer, API_URL_tenant):
    if visit_id:
        product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={'visit_id' :visit_id,
                                                        'tenant_id' : tenant_id })
    else:
        product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={ 'user_id':user_id })
    prod_list = product_list.json()
    
    return prod_list



def cart_transaction(Page_id, tenant_id, company_id, visit_id, API_URL_consumer, API_URL_tenant):
    dropdown_data = []
    try:
        if visit_id:
            product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={'visit_id' :visit_id,
                                                        'tenant_id' : tenant_id })
        else:
            product_list = requests.get('%s/API_bussiness/get_cart_data'
                                % API_URL_tenant, params={ 'user_id':user_id })
        prod_list = product_list.json()
        # print('prod_list::',prod_list)
        id_list = []
        for i in prod_list:
            id_list.append(i['prd_SKU_ID'])
        # print('id_list::', id_list)

        row_data = ast.literal_eval(request.form['rowdata'])
        print('row_data::',row_data)

        final_list = [] 
        for id in id_list: 
            for data in row_data:
                # print("data['prd_SKU_ID']::", data['prd_SKU_ID'])
                if id not in data['prd_SKU_ID']: 
                    final_list.append(id)

        # print("final_list::", final_list)

        for prd_id in final_list:
            create_request_obj = requests.put('%s/API_bussiness/update_add_to_cart_data'
                                                %API_URL_tenant, params={
                                                                'cart_id': "",
                                                                'prd_SKU_ID' : prd_id,
                                                                'status' : "Deleted",
                                                                'user_entered_qty':0
                                                                })
            

        bad_chars = [';', ':', '!', "*"] 
        total = 0
        for data in row_data:

            mrp = data['prd_MRP'][2:]
            quantity = data['user_entered_qty']
            sub_total = data['prd_SubTotal'][2:]
            mrp = mrp.replace(" ", "")
            mrp = mrp.strip()
            sub_total = sub_total.strip()
            mrp = int(float(mrp))
            sub_total = int(float(sub_total))
            total = total+sub_total
        
        # Get Today's Date
        StartDate = datetime.now()

        # Sent Post Request To Create checkout_to_cart Endoint
        # try:
        create_request_obj = requests.post('%s/API_bussiness/save_checkout_to_cart_data'
                                            %API_URL_tenant, params={
                                                        'checkout_to_cart_id' : '',
                                                        'checkout_to_cart_row_data' : request.form['rowdata'],
                                                        'sub_total' :  total,
                                                        'cart_Entry_Date' : StartDate,
                                                        'user_id' : "USER_1234",
                                                        'visit_id' : visit_id,
                                                        'tenant_id' : tenant_id,
                                                        'company_id' : company_id,                                                   
                                                        })

        #     flash('Your cart Has Been done SuccessFully', 'info')
        # except Exception as e :
        #     # print(e)
        #     flash('Your cart Has Been Not done SuccessFully', 'error')
        # if visit_id:
        #     address_list = requests.get('%s/API_bussiness/get_address'
        #                         % API_URL_tenant, params={'visit_id' :visit_id })
        # else:
        address_list = requests.get('%s/API_bussiness/get_address'
                            % API_URL_tenant, params={ 'user_id':'USER_1234' })
        
        address = address_list.json()

        # cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
        #                     % API_URL_tenant, params={ 'user_id':'USER_1234' })
        cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
                                    %API_URL_tenant, params={ 'visit_id':visit_id ,'tenant_id' : tenant_id})
        cart_data = cart_list.json()

        for data in cart_data:
            dropdown_data = ast.literal_eval(data['checkout_to_cart_row_data'])
            
        amount = int(data['sub_total'])*100

    except:
        
        # if visit_id:
        #     address_list = requests.get('%s/API_bussiness/get_address'
        #                         % API_URL_tenant, params={'visit_id' :visit_id })
        # else:
        address_list = requests.get('%s/API_bussiness/get_address'
                            % API_URL_tenant, params={ 'user_id':'USER_1234' })
        
        address = address_list.json()

        # cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
        #                     % API_URL_tenant, params={ 'user_id':'USER_1234' })
        cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
                            % API_URL_tenant, params={ 'visit_id':visit_id ,'tenant_id' : tenant_id})
        cart_data = cart_list.json()
        # print('cart_data@@@@', cart_data)
        for data in cart_data:
            dropdown_data = ast.literal_eval(data['checkout_to_cart_row_data'])
    # print('dropdown_data', dropdown_data)
    sub_total1 = 0.0
    total_tax = 0.0
    for i in dropdown_data:
        # print(i['prd_SKU_ID'])
        # print(i['user_entered_qty'])
        data = requests.get('%s/API_bussiness/get_pdt_data'
                                % API_URL_tenant, params={'dms_SKU_ID':i['prd_SKU_ID']})
        json_data = data.json()
        # print(json_data)
        for k in json_data:
            # print(k['prd_GST_applicable'])
            # print(k['prd_Standard_Price'])
            tax_request = requests.get('%s/API_bussiness/get_calculated_tax'
                                % API_URL_tenant, params={'product_price' : k['dms_Standard_Price'],
                                                    'percentage_of_tax' : k['dms_GST_applicable'],
                                                    'user_entered_qty' : i['user_entered_qty']
                                                    })
            # print(tax_request.json())
            total_tax += float(tax_request.json())
            sub_total1 += (float(k['dms_Standard_Price']) * float(i['user_entered_qty']))+float(tax_request.json())
    # print('sub_total1', sub_total1)
    # print('total_tax', total_tax)
    # for data in cart_data:
    #     sub_total = data['sub_total']
    #     tax = int(sub_total) * 0.18
    total_amount = sub_total1 + 100.0
    amount = int(total_amount)*100


    if visit_id:
        product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={'visit_id' :visit_id ,'tenant_id' : tenant_id})
    else:
        product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={ 'user_id':user_id })
    prod_list = product_list.json()

    return address, dropdown_data, total_amount,amount, prod_list, total_tax




def checkout_save(Page_id, tenant_id, company_id, visit_id, API_URL_consumer, API_URL_tenant):

    # Get Today's Date
    StartDate = datetime.now()
    StartDate = StartDate.date()

    # Today's date
    todays_date = date.today()

    #unpost date calculation
    delivery_date = str(todays_date + timedelta(days=7))
    dropdown_data = []
    billing_address = []
    shipping_address = []
    payment_method = ''
    try:
      
        billing_address = ast.literal_eval(request.form['ui_billing_address'])
        shipping_address = ast.literal_eval(request.form['ui_shipping_address'])
        payment_method = request.form['ui_chkot_shipping_method']

        address_list = requests.get('%s/API_bussiness/get_address'
                            % API_URL, params={ 'user_id':'USER_1234' })
        
        address = address_list.json()

        # cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
        #                     % API_URL, params={ 'user_id':'USER_1234' })
        cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
                            % API_URL_tenant, params={ 'visit_id':visit_id ,'tenant_id' : tenant_id})
        cart_data = cart_list.json()
        # print('cart_data@@@@', cart_data)
        for data in cart_data:
            dropdown_data = ast.literal_eval(data['checkout_to_cart_row_data'])
        print('dropdown_data::', dropdown_data)

        # sub_total = data['sub_total']
        # tax = int(sub_total) * 0.18
        # total_amount = int(sub_total)+ int(tax) + 100
        # amount = int(total_amount)*100

        create_request_obj = requests.post('%s/API_bussiness/save_checkout_data'
                                            %API_URL_tenant, params={
                                                            'chkot_billing_address' : str(billing_address),
                                                            'chkot_shipping_address' : str(shipping_address),
                                                            'chkot_payment_method' : payment_method,
                                                            'chkot_date' : StartDate,
                                                            'visit_id' : visit_id,
                                                            'user_id' : '',
                                                            'tenant_id' : tenant_id,
                                                            'company_id' : company_id,
                                                                })
        if visit_id:
            product_list = requests.get('%s/API_bussiness/get_cart_data'
                                        % API_URL_tenant, params={'visit_id' :visit_id ,'tenant_id' : tenant_id})
        else:
            product_list = requests.get('%s/API_bussiness/get_cart_data'
                                         % API_URL_tenant, params={ 'user_id':user_id })
        prod_list = product_list.json()

    except:
        address_list = requests.get('%s/API_bussiness/get_address'
                                     % API_URL_tenant, params={ 'user_id':'USER_1234' })
        
        address = address_list.json()

        # cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
        #                     % API_URL, params={ 'user_id':'USER_1234' })
        cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
                                  % API_URL_tenant, params={ 'visit_id':visit_id ,'tenant_id' : tenant_id})
        cart_data = cart_list.json()
        # print('cart_data@@@@', cart_data)
        for data in cart_data:
            dropdown_data = ast.literal_eval(data['checkout_to_cart_row_data'])

        print('dropdown_data::', dropdown_data)
        # sub_total = data['sub_total']
        # tax = int(sub_total) * 0.18
        # total_amount = int(sub_total)+ int(tax) + 100
        # amount = int(total_amount)*100

        create_request_obj = requests.post('%s/API_bussiness/save_checkout_data'
                                            %API_URL_tenant, params={
                                                            'chkot_billing_address' : str(billing_address),
                                                            'chkot_shipping_address' : str(shipping_address),
                                                            'chkot_payment_method' : payment_method,
                                                            'chkot_date' : StartDate,
                                                            'visit_id' : visit_id,
                                                            'user_id' : '',
                                                            'tenant_id' : tenant_id,
                                                            'company_id' : company_id,
                                                                })
        if visit_id:
            product_list = requests.get('%s/API_bussiness/get_cart_data'
                                % API_URL_tenant, params={'visit_id' :visit_id ,'tenant_id' : tenant_id})
        else:
            product_list = requests.get('%s/API_bussiness/get_cart_data'
                                % API_URL_tenant, params={ 'user_id':user_id })
        prod_list = product_list.json()
    
    sub_total1 = 0.0
    total_tax = 0.0
    for i in dropdown_data:
        # print(i['prd_SKU_ID'])
        # print(i['user_entered_qty'])
        data = requests.get('%s/API_bussiness/get_pdt_data'
                                % API_URL_tenant, params={'dms_SKU_ID':i['prd_SKU_ID']})
        json_data = data.json()
        # print(json_data)
        for k in json_data:
            # print(k['prd_GST_applicable'])
            # print(k['prd_Standard_Price'])
            tax_request = requests.get('%s/API_bussiness/get_calculated_tax'
                                % API_URL_tenant, params={'product_price' : k['dms_Standard_Price'],
                                                    'percentage_of_tax' : k['dms_GST_applicable'],
                                                    'user_entered_qty' : i['user_entered_qty']
                                                    })
            # print(tax_request.json())
            total_tax += float(tax_request.json())
            sub_total1 += (float(k['dms_Standard_Price']) * float(i['user_entered_qty']))+float(tax_request.json())
    # print('sub_total1', sub_total1)
    # print('total_tax', total_tax)
    # for data in cart_data:
    #     sub_total = data['sub_total']
    #     tax = int(sub_total) * 0.18
    total_amount = sub_total1 + 100.0
    amount = int(total_amount)*100

    return address, dropdown_data, total_amount, amount,billing_address, prod_list, total_tax, shipping_address, payment_method, delivery_date


def online_payment(Page_id, tenant_id, company_id, visit_id, API_URL_consumer, API_URL_tenant):
     # Generate Order Id Dynamically
    generate_order_id = requests.get('%s/API_bussiness/generate_order_id' % API_URL_tenant)

    # Convert In Json
    order_id_json = generate_order_id.json()

    order_id = order_id_json
    # print(order_id)
    
    # Get Today's Date
    StartDate = datetime.now()

    # Today's date
    todays_date = date.today()

    #delivery date calculation
    delivery_date = str(todays_date + timedelta(days=7))

    cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
                        % API_URL_tenant, params={ 'user_id':'USER_1234' })
    cart_data = cart_list.json()
    for data in cart_data:
        dropdown_data = ast.literal_eval(data['checkout_to_cart_row_data'])
   
    payment_method = 'Online Payment'
    payment_id = request.form['shopping_order_id_test']

    sub_total = data['sub_total']
    tax = int(sub_total) * 0.18
    total_amount = int(sub_total)+ int(tax) + 100
    amount = int(total_amount)*100

    if visit_id:
            product_list = requests.get('%s/API_bussiness/get_cart_data'
                                % API_URL_tenant, params={'visit_id' :visit_id ,'tenant_id' : tenant_id})
    else:
        product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={ 'user_id':user_id })
    prod_list = product_list.json()
    
    sub_total1 = 0.0
    total_tax = 0.0
    for i in dropdown_data:
        # print(i['prd_SKU_ID'])
        # print(i['user_entered_qty'])
        data = requests.get('%s/API_bussiness/get_pdt_data'
                                % API_URL_tenant, params={'dms_SKU_ID':i['prd_SKU_ID']})
        json_data = data.json()
        # print(json_data)
        for k in json_data:
            # print(k['prd_GST_applicable'])
            # print(k['prd_Standard_Price'])
            tax_request = requests.get('%s/API_bussiness/get_calculated_tax'
                                % API_URL_tenant, params={'product_price' : k['dms_Standard_Price'],
                                                    'percentage_of_tax' : k['dms_GST_applicable'],
                                                    'user_entered_qty' : i['user_entered_qty']
                                                    })
            # print(tax_request.json())
            total_tax += float(tax_request.json())
            sub_total1 += (float(k['dms_Standard_Price']) * float(i['user_entered_qty']))+float(tax_request.json())
    # print('sub_total1', sub_total1)
    # print('total_tax', total_tax)
    # for data in cart_data:
    #     sub_total = data['sub_total']
    #     tax = int(sub_total) * 0.18
    total_amount = sub_total1 + 100.0
    amount = int(total_amount)*100


    payment_details=razorpay_client.payment.capture(payment_id, amount)

    # Sent Post Request To Create Paayment Endoint
    # try:
    create_request_obj = requests.post('%s/API_bussiness/save_payment_data'
                                                        %API_URL_tenant, params={
                                                                'paymeny_id' : payment_details['id'],
                                                                'paymeny_entity' : payment_details['entity'],
                                                                'paymeny_amount' : payment_details['amount'],
                                                                'paymeny_currency' : payment_details['currency'],
                                                                'paymeny_status' : payment_details['status'],
                                                                'paymeny_order_id' : payment_details['order_id'],
                                                                'paymeny_invoice_id' : payment_details['invoice_id'],
                                                                'paymeny_international' : payment_details['international'],
                                                                'paymeny_method' : payment_details['method'],
                                                                'paymeny_amount_refunded' : payment_details['amount_refunded'],
                                                                'paymeny_refund_status' : payment_details['refund_status'],
                                                                'paymeny_captured' : payment_details['captured'],
                                                                'paymeny_description' :payment_details['description'] ,
                                                                'paymeny_card_id' : payment_details['card_id'],
                                                                'paymeny_bank' : payment_details['bank'],
                                                                'paymeny_wallet' : payment_details['wallet'],
                                                                'paymeny_vpa' : payment_details['vpa'],
                                                                'paymeny_email' : payment_details['email'],
                                                                'paymeny_contact' : payment_details['contact'],
                                                                'paymeny_notes' :payment_details['notes'] ,
                                                                'paymeny_fee' : payment_details['fee'],
                                                                'paymeny_tax' : payment_details['tax'],
                                                                'paymeny_error_code' : payment_details['error_code'],
                                                                'paymeny_error_description' : payment_details['error_description'],
                                                                'paymeny_created_at' : payment_details['created_at'],
                                                                'user_id' : 'USER_1234',
                                                                'visit_id' : visit_id,
                                                                'tenant_id' : tenant_id,
                                                                'company_id' : company_id,

                                                                })

    #     flash('Payment SuccessFull', 'info')
    # except Exception as e :
    #     # print(e)
    #     flash('Payment UnsuccessFull', 'error')

    address_list = requests.get('%s/API_bussiness/get_address'
                        % API_URL_tenant, params={ 'user_id':'USER_1234' })
    
    address = address_list.json()

    # cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
    #                     % API_URL, params={ 'user_id':'USER_1234' })
    cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
                        % API_URL_tenant, params={ 'visit_id':visit_id ,'tenant_id' : tenant_id})
    cart_data = cart_list.json()
    # print('cart_data@@@@', cart_data)
    for data in cart_data:
        dropdown_data = ast.literal_eval(data['checkout_to_cart_row_data'])

    checkout_request = requests.get('%s/API_bussiness/get_checkout_data'
                        % API_URL_tenant, params={ 'visit_id':visit_id ,'tenant_id' : tenant_id})
    checkout_data = checkout_request.json()
    for chk_data in checkout_data:
        del_addr = chk_data['chkot_shipping_address']
    # print(del_addr)

    # Sent Post Request To Create Order Endoint
    # try:
    create_request_obj = requests.post('%s/API_bussiness/save_order_data'
                                                        %API_URL_tenant, params={
                                                                'ord_Order_date' : StartDate,
                                                                'ord_delivery_date': delivery_date,
                                                                'ord_Order_id' : order_id,
                                                                'prd_Product_Title ' : str(dropdown_data),
                                                                'ord_Quantity' : '',
                                                                'ord_Order_del_addr' : del_addr,
                                                                # 'ord_delivery_date' : ,
                                                                'ord_Order_sts' : 'Shipped',
                                                                # 'ord_Order_Compete_dt' : request.form['ui_chkot_pincode'],
                                                                'ord_user_feedback' : "",
                                                                'paymeny_method' : payment_method,
                                                                'paymeny_id' : payment_id,
                                                                # 'chkot_shipping_method' : request.form['ui_chkot_shipping_method'],
                                                                # 'user_id' : current_user.user_id,
                                                                'user_id': 'USER_1234',
                                                                'ord_Gross_Sales' : "data['sub_total']",
                                                                'visit_id' : visit_id,
                                                                'tenant_id' : tenant_id,
                                                                'company_id' : company_id,
                                                                })

    #     flash('Order SuccessFull', 'info')
    # except Exception as e :
    #     # print(e)
    #     flash('Order UnsuccessFull', 'error')

    return order_id


def cash_on_delivery(Page_id, tenant_id, company_id, visit_id, API_URL_consumer, API_URL_tenant):
     # Get Today's Date
    StartDate = datetime.now()
    # Today's date
    todays_date = date.today()

    #delivery date calculation
    delivery_date = str(todays_date + timedelta(days=7))

    # Generate Order Id Dynamically
    generate_order_id = requests.get('%s/API_bussiness/generate_order_id' % API_URL_tenant)

    # Convert In Json
    order_id_json = generate_order_id.json()

    order_id = order_id_json
    # print(order_id)
    payment_method = "Cash On Delivery"

    address_list = requests.get('%s/API_bussiness/get_address'
                        % API_URL_tenant, params={ 'user_id':'USER_1234' })
    
    address = address_list.json()

    # cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
    #                     % API_URL, params={ 'user_id':'USER_1234' })
    cart_list = requests.get('%s/API_bussiness/get_cart_to_checkout'
                        % API_URL_tenant, params={ 'visit_id':visit_id ,'tenant_id' : tenant_id})
    cart_data = cart_list.json()
    # print('cart_data@@@@', cart_data)
    for data in cart_data:
        dropdown_data = ast.literal_eval(data['checkout_to_cart_row_data'])

    checkout_request = requests.get('%s/API_bussiness/get_checkout_data'
                        % API_URL_tenant, params={ 'visit_id':visit_id ,'tenant_id' : tenant_id})
    checkout_data = checkout_request.json()
    for chk_data in checkout_data:
        del_addr = chk_data['chkot_shipping_address']

    # Sent Post Request To Create Order Endoint
    # try:
    create_request_obj = requests.post('%s/API_bussiness/save_order_data'
                                                        %API_URL_tenant, params={
                                                                'ord_Order_date' : StartDate,
                                                                'ord_delivery_date': delivery_date,
                                                                'ord_Order_id' : order_id,
                                                                'prd_Product_Title ' : str(dropdown_data),
                                                                'ord_Quantity' : '',
                                                                'ord_Order_del_addr' : del_addr,
                                                                'ord_Order_sts' : 'Shipped',
                                                                # 'ord_Order_Compete_dt' : request.form['ui_chkot_pincode'],
                                                                'ord_user_feedback' : "",
                                                                'paymeny_method' : payment_method,
                                                                'paymeny_id' : '',
                                                                # 'chkot_shipping_method' : request.form['ui_chkot_shipping_method'],
                                                                # 'user_id' : current_user.user_id,
                                                                'user_id': 'USER_1234',
                                                                'ord_Gross_Sales' : "data['sub_total']",
                                                                'visit_id' : visit_id,
                                                                'tenant_id' : tenant_id,
                                                                'company_id' : company_id,
                                                                })
    #     flash('Order SuccessFull', 'info')
    # except Exception as e :
    #     # print(e)
    #     flash('Order UnsuccessFull', 'error')

    return order_id


def order_details(Page_id, tenant_id, company_id, visit_id, order_id, API_URL_consumer, API_URL_tenant):
    # order_list = requests.get('%s/API_bussiness/get_order_data'
    #                     % API_URL, params={ 'user_id':'USER_1234' })
    order_list = requests.get('%s/API_bussiness/get_order_data'
                        % API_URL_tenant, params={ 'order_id':order_id })
    ord_list = order_list.json()
    # print('ord_list@@@:::', ord_list)
    product_title = []
    title = []
    for data in ord_list:
        ord_date=data['ord_Order_date']
        delivery_date = data['ord_delivery_date']
        del_addr=ast.literal_eval(data['ord_Order_del_addr'])
        product_title=ast.literal_eval(data['prd_Product_Title'])

    for j in product_title:
        title = ast.literal_eval(j)

    product_list = requests.get('%s/API_bussiness/get_pdt_data'
                            % API_URL_tenant, params={'dms_SKU_ID' : 'PROD_1001'})
    product_data_list = product_list.json()
    # print('product_data_list::',product_data_list)

    for i in title:
        # print('prd_SKU_ID:',i['prd_SKU_ID'])
        # print('Quantity:',i['user_entered_qty'])
        # try:
        # create_request_obj = requests.put('%s/API_bussiness/update_add_to_cart_data'
        #                                         %API_URL, params={
        #                                                         'cart_id': i['cart_id'],
        #                                                         'prd_SKU_ID' : i['prd_SKU_ID'],
        #                                                         'status' : "Ordered",
        #                                                         'user_entered_qty':0
        #                                                         })
        create_request_obj = requests.put('%s/API_bussiness/update_add_to_cart_data_after_order'
                                                %API_URL_tenant, params={
                                                                'cart_id': i['cart_id'],
                                                                # 'prd_SKU_ID' : i['prd_SKU_ID'],
                                                                'status' : "Ordered",
                                                                # 'user_entered_qty':0
                                                                })

        #     flash('Your cart Has Been done SuccessFully', 'info')
        # except Exception as e :
        #     # print(e)
        #     flash('Your cart Has Been Not done SuccessFully', 'error')
        product_list = requests.get('%s/API_bussiness/get_pdt_data'
                            % API_URL_tenant, params={'dms_SKU_ID' : i['prd_SKU_ID']})
        product_data_list = product_list.json()
        
        for k in product_data_list:
            # print('product_data_list qty::',k['prd_Qty']) 
            # try:
            create_request_obj = requests.put('%s/API_bussiness/update_tvl_product_data'
                                                    %API_URL_tenant, params={
                                                            'prd_SKU_ID' : i['prd_SKU_ID'],
                                                            'prd_Qty' : int(k['dms_Qty'])-int(i['user_entered_qty'])
                                                            })

            #     flash('Your cart Has Been done SuccessFully', 'info')
            # except Exception as e :
            #     # print(e)
            #     flash('Your cart Has Been Not done SuccessFully', 'error')

    address_list = requests.get('%s/API_bussiness/get_address'
                        % API_URL_tenant, params={ 'user_id':'USER_1234' })
    
    address = address_list.json()
    # print('address::',address)

    if visit_id:
        product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={'visit_id' :visit_id ,'tenant_id' : tenant_id})
    else:
        product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={ 'user_id':user_id })
    prod_list = product_list.json()

    # Sent Whats App Messages
    try:


        # Send Whats APP Message To User 
        create_transaction_document = requests.post('%s/API_bussiness/send_whatsapp_messages'%API_URL,
                                                            params={
                                                                    'receiver_phone_number':'+91'+current_user.dms_WhatsApp_No,
                                                                    'message_text':'Your Order with id %s, has been changed to status %s. Further Details Available at https://www.skf.com/in/index.html'
                                                                                    %(order_id, 'New')
                                                                                    })
    except:
        print('Message Not Send')



    # Sent Messages
    try:

        # Sent SMS By API Url
        send_sms_request_obj = requests.post('%s/API_bussiness/send_sms'%API_URL,
                                            params={
                                                'recipient':int(current_user.phone_number),
                                                'message':'Your Order with id %s, has been changed to status %s. Further Details Available at https://www.skf.com/in/index.html'
                                                            %(order_id, 'New')
                                            })
    except:
        flash('Message Not Send')

    return ord_list, del_addr, title, delivery_date, order_id, prod_list



def product_details(Page_id, tenant_id, company_id, visit_id, pdt_id, API_URL_consumer, API_URL_tenant):

    pg_compnt_list1 = requests.get('%s/API_bussiness/get_och_page_component_data'
                        % API_URL_consumer, params={'Page_id':Page_id})
    page_compnt_list1 = pg_compnt_list1.json()
    # print(page_compnt_list1[0])

    # Get Specific Complaint Details
    # Get Response Through API
    data = requests.get('%s/API_bussiness/get_pdt_data'
                            % API_URL_tenant, params={'dms_SKU_ID':pdt_id})
    json_data = data.json()
    # # print(json_data)
    category_data_json = []
    for k in json_data:
        quantity = k['dms_Qty']
    # for i in json_data:
    #     category = i['dms_Product_category']
    # category_data = requests.get('%s/API_bussiness/get_pdt_data'
    #                         % API_URL_tenant, params={'dms_Product_category':category})
    # category_data_json = category_data.json()

    if visit_id:
        product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={'visit_id' :visit_id ,'tenant_id' : tenant_id})
    else:
        product_list = requests.get('%s/API_bussiness/get_cart_data'
                            % API_URL_tenant, params={ 'user_id':user_id })
    prod_list = product_list.json()
   
    return page_compnt_list1, json_data, category_data_json, quantity, prod_list


def address_save(Page_id, tenant_id, company_id, visit_id, API_URL_consumer, API_URL_tenant):
    # Sent Post Request To Create Order Endoint
    # try:
    create_request_obj = requests.post('%s/API_bussiness/save_address'
                                        %API_URL_tenant, params={
                                                        'addr_First_Name' : request.form['ui_chkot_first_name'],
                                                        'addr_Last_Name' : request.form['ui_chkot_last_name'],
                                                        'addr_email' : request.form['ui_chkot_email'],
                                                        'addr_Phone' : request.form['ui_chkot_ph_number'],
                                                        'addr_Address' : request.form['ui_chkot_shipping_address'],
                                                        'addr_City' : request.form['ui_chkot_city'],
                                                        'addr_Pincode' : request.form['ui_chkot_pincode'],
                                                        'addr_State' : request.form['ui_chkot_state'],
                                                        'addr_Order_Note' : request.form['ui_chkot_note'],
                                                        'user_id' : "USER_1234",
                                                        'visit_id' : session['visit_id'],
                                                        'tenant_id' : tenant_id,
                                                        'company_id' : company_id,  
                                                        })
    #     flash('Order SuccessFull', 'info')
    # except Exception as e :
    #     # print(e)
    #     flash('Order UnsuccessFull', 'error')
    return
