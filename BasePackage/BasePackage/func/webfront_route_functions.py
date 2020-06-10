# pylint: disable=missing-docstring, no-member, unused-variable

"""

This Program Is For SKF All Function For Routes Related To SKF Modules Defined Here

"""

# Import All Neccessary Modules

from datetime import datetime, timedelta
import json
from flask import Blueprint, jsonify
from mongoengine.queryset.visitor import Q


# Importing Our modules

from APP.WebFront.models import och_add_to_cart_master, och_product_master, och_checkout_master,\
                                och_cart_transaction,och_page_master,webfront_page_component_master,\
                                tvl_product_master, tvl_add_to_cart_master, tvl_checkout_master,\
                                nkshi_product_master, nkshi_add_to_cart_master, nkshi_checkout_master,\
                                atlasware_product_master, atlasware_add_to_cart_master, atlasware_checkout_master
# from APP.WebFront.models import och_add_to_cart_master, och_product_master, och_checkout_master,\
#                                 och_cart_transaction,och_page_master,webfront_page_component_master,tvl_product_master,\
#                                 nkshi_product_master, atlasware_product_master
# from APP.Checkout.queries.create_claim_id import func_create_claim_id
# from APP.Checkout.queries.claim_transaction import func_claims_transaction_support


# Creating Blueprint

WebFront = Blueprint(__name__, 'WebFront')



# All Route Functions

# Route Function For Dynamic Genration Of lead Id

def func_genrate_claim_id():

    
    dms_claim_id = func_create_claim_id()

    return dms_claim_id


# New add_to_cart Creation Functions

def func_create_add_to_cart(
    prd_SKU_ID = '',
    prd_Product_Title = '',
    prd_MRP = '',
    prd_Standard_Price  = '',
    prd_Qty  = '',
    prd_Main_View_Image = '',
    cart_Entry_Date= '',
    

    user_id = '',
    # user_name = '',
    # company = '',
    # company_id = '',
    # department_name = '',
    # department_id = '',
    # branch_id = '',
    # branch_name = '', 
   
        ):

 
    create_object = och_add_to_cart_master(
        prd_SKU_ID = prd_SKU_ID,
        prd_Product_Title = prd_Product_Title,
        prd_MRP = prd_MRP,
        prd_Standard_Price = prd_Standard_Price,
        prd_Qty = prd_Qty,
        prd_Main_View_Image = prd_Main_View_Image,
        cart_Entry_Date = cart_Entry_Date,
         
        user_id = user_id,
        # user_name = user_name,
        # company = company,
        # company_id = company_id,
        # department_name = department_name,
        # department_id = department_id,
        # branch_id = branch_id,
        # branch_name = branch_name,
        
        )


    # Save Create Object data in Database

    create_object.save()
    response = {'Response': 'One product added to cart Sucssesfully'}

    return response

def func_cart_transaction(
    prd_SKU_ID = '',
    prd_Product_Title = '',
    prd_MRP = '',
    prd_Standard_Price = '',
    prd_Qty = '',
    cart_Total = '',
    cart_Sub_Total = '',
    user_id = '',
    prd_Main_View_Image = '',
    cart_transaction_Entry_Date = '',

        ):

 
    create_object = och_cart_transaction(
        
        cart_Total =  cart_Total,
        cart_Sub_Total =  cart_Sub_Total,
        prd_SKU_ID = prd_SKU_ID,
        prd_Product_Title = prd_Product_Title,
        prd_MRP = prd_MRP,
        prd_Standard_Price = prd_Standard_Price,
        prd_Qty = prd_Qty,
        user_id = user_id,
         prd_Main_View_Image = prd_Main_View_Image,
         cart_transaction_Entry_Date = cart_transaction_Entry_Date,
        )


    # Save Create Object data in Database

    create_object.save()
    response = {'Response': 'One cart transaction added Sucssesfully'}

    return response


# New Checkout Creation Functions

def func_och_checkout(
    chkot_last_change = '',
    chkot_First_Name = '',
    chkot_Last_Name = '', 
    chkot_email = '',
    chkot_Phone = '',
    chkot_Address = '',
    chkot_City = '',
    chkot_Pincode = '',
    chkot_State = '',
    chkot_Order_Note = '',
    # chkot_token = '',
    chkot_quantity = '',
    # chkot_billing_address = '',
    # chkot_shipping_address = '',
    chkot_shipping_method = '',
    # chkot_note = '',
    chkot_currency = '',
    chkot_discount_amount = '',
    chkot_discount_name = '',
    chkot_translated_discount_name = '',
    chkot_voucher_code = '',
    chkot_gift_cards = '',
    user_id = '',
        ):

 
    create_object = och_checkout_master(
        chkot_last_change = chkot_last_change,
        chkot_First_Name = chkot_First_Name,
        chkot_Last_Name  = chkot_Last_Name,
        chkot_email = chkot_email,
        chkot_Phone = chkot_Phone,
        chkot_Address = chkot_Address,
        chkot_City = chkot_City,
        chkot_Pincode = chkot_Pincode,
        chkot_State = chkot_State,
        chkot_Order_Note = chkot_Order_Note,
        # chkot_token = chkot_token,
        chkot_quantity = chkot_quantity,
        # chkot_billing_address = chkot_billing_address,
        # chkot_shipping_address = chkot_shipping_address,
        chkot_shipping_method = chkot_shipping_method,
        # chkot_note = chkot_note,
        chkot_currency = chkot_currency,
        chkot_discount_amount = chkot_discount_amount,
        chkot_discount_name = chkot_discount_name,
        chkot_translated_discount_name = chkot_translated_discount_name,
        chkot_voucher_code = chkot_voucher_code,
        chkot_gift_cards = chkot_gift_cards,
        user_id = user_id,
        

        )


    # Save Create Object data in Database

    create_object.save()
    response = {'Response': 'One Checkout completed'}

    return response






# New Checkout Creation Functions

def func_och_checkout_(
    chkot_last_change = '',
    chkot_user = '',
    chkot_email = '',
    # chkot_token = db.StringField(default='')
    chkot_quantity = '',
    chkot_billing_address = '',
    chkot_shipping_address = '',
    chkot_shipping_method = '',
    chkot_note = '',
    chkot_currency = '',
    chkot_discount_amount = '',
    chkot_discount_name = '',
    chkot_translated_discount_name = '',
    chkot_voucher_code = '',
    chkot_gift_cards = '',
    user_id = '',
        ):

 
    create_object = och_checkout_master_(
        chkot_last_change = chkot_last_change,
        chkot_user = chkot_user,
        chkot_email = chkot_email,
        # chkot_token = chkot_token,
        chkot_quantity = chkot_quantity,
        chkot_billing_address = chkot_billing_address,
        chkot_shipping_address = chkot_shipping_address,
        chkot_shipping_method = chkot_shipping_method,
        chkot_note = chkot_note,
        chkot_currency = chkot_currency,
        chkot_discount_amount = chkot_discount_amount,
        chkot_discount_name = chkot_discount_name,
        chkot_translated_discount_name = chkot_translated_discount_name,
        chkot_voucher_code = chkot_voucher_code,
        chkot_gift_cards = chkot_gift_cards,
        user_id = user_id,

        )


    # Save Create Object data in Database

    create_object.save()
    response = {'Response': 'One Checkout completed'}

    return response













# This Function Getting All Data From Claims Master By Claims Types

def func_get_cart_data(start_data_no=0,
                        
                        user_id = None,
                        company_id = None,
                        department_id = None,
                        branch_id = None,
                                
                                ):





    
    if user_id:
        data_obj = och_add_to_cart_master.objects(user_id=user_id)
    # elif dms_Company_Type:
    #     data_obj = dms_claims_master.objects(dms_Company_Type=dms_Company_Type)
    # elif dms_Company_Name:
    #     data_obj = dms_claims_master.objects(dms_Company_Name=dms_Company_Name)
    # elif dms_Claims_Id:
    #     data_obj = dms_claims_master.objects(dms_Claims_Id=dms_Claims_Id)
    # elif dms_Claims_Create_Date:
    #     data_obj = dms_claims_master.objects(dms_Claims_Create_Date=dms_Claims_Create_Date)
    # elif dms_Claims_Close_Date:
    #     data_obj = dms_claims_master.objects(dms_Claims_Close_Date=dms_Claims_Close_Date)
    # elif dms_Claims_Sts:
    #     data_obj = dms_claims_master.objects(dms_Claims_Sts=dms_Claims_Sts)
    # elif dms_Claims_By:
    #     data_obj = dms_claims_master.objects(dms_Claims_By=dms_Claims_By)
    # elif dms_Claims_Type:
    #     data_obj = dms_claims_master.objects(dms_Claims_Type=dms_Claims_Type)
    
    # elif request_before_date:
    #     request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')
    #     if request_after_date:
    #         request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #         data_obj = dms_claims_master.objects(Q(dms_Claims_Create_Date__gt=request_before_date_)
    #                                             & Q(dms_Claims_Create_Date__lt=request_after_date_))                                                
    #     else:
            
    #         data_obj = dms_claims_master.objects
    # else:
    #     data_obj = dms_claims_master.objects
    
    # Declaring List For Order Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic['prd_SKU_ID'] = i.prd_SKU_ID
        dic['prd_Product_Title'] = i.prd_Product_Title
        dic['prd_MRP'] = i.prd_MRP
        dic['prd_Standard_Price'] = i.prd_Standard_Price
        dic['prd_Qty'] = i.prd_Qty
        dic['user_id'] = i.user_id
        dic['prd_Main_View_Image'] = i.prd_Main_View_Image
        dic['cart_Entry_Date'] = i.cart_Entry_Date
        
        list_of_data.append(dic)

        # Sort List By Dates
        list_of_data.sort(key=lambda r: r['cart_Entry_Date'], reverse=True)


     # This Section Is For Pagination Logic

    # start_data_no = start_data_no
    # end_data_no = start_data_no + total_result

    # Adding Exception Handling For if Geiven Start Page no Is Not In Index
    # list_of_data_for_pagination = list_of_data[start_data_no:end_data_no+1]

    # There Is No Data For Perticular Query

    # if len(list_of_data_for_pagination)<1:
    #     dic = {}
    #     dic['prd_SKU_ID'] = "Data Not Available"
    #     dic['prd_Product_Title'] = "Data Not Available"
    #     dic['prd_MRP'] = "Data Not Available"
    #     dic['prd_Standard_Price'] = "Data Not Available"
    #     dic['prd_Qty'] = "Data Not Available"
    #     dic['user_id'] = "Data Not Available"
       

    #     list_of_data_for_pagination.append(dic)

    # return list_of_data_for_pagination
    return list_of_data




######################################################################################
####    Product Section

# This Function Getting All Data From Product Master 

def func_get_och_product(start_data_no=0,
                                total_result=300,
                                request_before_date = None,
                                request_after_date = None,

                                prd_Product_Name = None,
                                prd_Brand = None,
                                prd_SKU_ID = None,
                                prd_Manufacturer = None,
                                prd_HSN_Code = None,
                                prd_Search_Terms = None,
                                prd_Search_Terms_Keywords_1 = None,
                                
                                prd_Status = None,
                                assigned_to = None,

                                user_id = None,
                                company_id = None,
                                department_id = None,
                                branch_id = None,
                                prd_Product_category = None,
                                ):

    # # If Date I None, Get Today Date - 30 Days Date

    # if request_before_date == None:

    #     # Get Todays Date
    #     todays_date = datetime.today()

    #     # Date For Before 30 Days
    #     # Calculate 30 day's Back Date
    #     request_before_date_tmp = todays_date - timedelta(days=30)

    # else:
    #     request_before_date_tmp = request_before_date
    #     request_before_date_tmp = request_before_date




    # # If Company Is In Request Then Find data For That Specific Company
    # # If Company Id And Branch Id Are Not None Then File Dealer Branch Level Data For That Customer
    # # If Company Id , Branch Id And Department Id Is Not None The Find Department Level Data For That Customer
    # # If User Id Is Not None Then Find User Level Data

    # if assigned_to != None:
    #     data_obj = och_product_master.objects(assigned_to=assigned_to)

    # elif user_id != None:
    #     if request_before_date:
    #         request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')
    #         if request_after_date:
    #             request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #             data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                 & Q(prd_Entry_Date__lt=request_after_date_)
    #                                                 & Q(user_id=user_id))
    #         else:
    #             data_obj = och_product_master.objects(user_id=user_id)
    #     else:
    #         data_obj = och_product_master.objects(user_id=user_id)

    # elif company_id != None :


    #     # If Department Is Available In Endpont request
    #     if branch_id != None :
    #         # Is Section Is For Query Data Related Logic


    #         # If Department Is Available
    #         if department_id != None:



    #             # If User Id Is Available Get User Specific Data
    #             if user_id != None:

    #                 if prd_SKU_ID:
    #                     data_obj = och_product_master.objects(prd_SKU_ID=prd_SKU_ID)

    #                 elif prd_Status:
    #                     if request_before_date:
    #                         request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')

    #                         if request_after_date:
    #                             request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #                             data_obj = och_product_master.objects(Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                            & Q(prd_Status=prd_Status)
    #                                                                            & Q(company_id=company_id) & Q(branch_id=branch_id) & Q(department_id=department_id)& Q(user_id=user_id))
    #                         else:
    #                             data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                            & Q(prd_Status=prd_Status)
    #                                                                            & Q(company_id=company_id) & Q(branch_id=branch_id) & Q(department_id=department_id)& Q(user_id=user_id))


    #                     else:
    #                         data_obj = och_product_master.objects(Q(prd_Status=prd_Status)
    #                                                                        & Q(company_id=company_id) & Q(branch_id=branch_id) & Q(department_id=department_id)& Q(user_id=user_id))


    #                 elif request_before_date:
    #                     request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')

    #                     if enquiry_request_after_date:
    #                         request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #                         data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                        & Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                        & Q(company_id=company_id) & Q(branch_id=branch_id) & Q(department_id=department_id)& Q(user_id=user_id))
    #                     else:
    #                         data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                        & Q(company_id=company_id) & Q(branch_id=branch_id) & Q(department_id=department_id)& Q(user_id=user_id))



    #                 elif request_after_date:
    #                     request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #                     data_obj = och_product_master.objects(Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                    & Q(company_id=company_id) & Q(branch_id=branch_id) & Q(department_id=department_id)& Q(user_id=user_id))

    #                 else:
    #                     data_obj = och_product_master.objects(Q(company_id=company_id) & Q(branch_id=branch_id) & Q(department_id=department_id)& Q(user_id=user_id))




    #             ############ else Get Department Specific Data ################
    #             else:
    #                 # Else Get Department Specific Data

    #                 if prd_SKU_ID:
    #                     data_obj = och_product_master.objects(prd_SKU_ID=prd_SKU_ID)

    #                 elif prd_Status:
    #                     if request_before_date:
    #                         request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')

    #                         if request_after_date:
    #                             request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #                             data_obj = och_product_master.objects(Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                            & Q(prd_Status=prd_Status)
    #                                                                            & Q(company_id=company_id) & Q(branch_id=branch_id)& Q(department_id=department_id))
    #                         else:
    #                             data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                            & Q(prd_Status=prd_Status)
    #                                                                            & Q(company_id=company_id) & Q(branch_id=branch_id)& Q(department_id=department_id))


    #                     else:
    #                         data_obj = och_product_master.objects(Q(prd_Status=prd_Status)
    #                                                                        & Q(company_id=company_id) & Q(branch_id=branch_id)& Q(department_id=department_id))


    #                 elif request_before_date:
    #                     request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')

    #                     if request_after_date:
    #                         request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #                         data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                        & Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                        & Q(company_id=company_id) & Q(branch_id=branch_id)& Q(department_id=department_id))
    #                     else:
    #                         data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                        & Q(company_id=company_id) & Q(branch_id=branch_id)& Q(department_id=department_id))



    #                 elif request_after_date:
    #                     request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #                     data_obj = och_product_master.objects(Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                    & Q(company_id=company_id) & Q(branch_id=branch_id)& Q(department_id=department_id))

    #                 else:
    #                     data_obj = och_product_master.objects(Q(company_id=company_id) & Q(branch_id=branch_id)& Q(department_id=department_id))




    #         ############ else Get Branch Specific Data ################
    #         else:
    #             if prd_SKU_ID:
    #                 data_obj = och_product_master.objects(prd_SKU_ID=prd_SKU_ID)

    #             elif prd_Status:
    #                 if request_before_date:
    #                     request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')

    #                     if request_after_date:
    #                         request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #                         data_obj = och_product_master.objects(Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                        & Q(prd_Status=prd_Status)
    #                                                                        & Q(company_id=company_id)& Q(branch_id=branch_id))
    #                     else:
    #                         data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=enquiry_request_before_date_)
    #                                                                        & Q(prd_Status=prd_Status)
    #                                                                        & Q(company_id=company_id)& Q(branch_id=branch_id))


    #                 else: data_obj = och_product_master.objects(Q(prd_Status=prd_Status)
    #                                                                        & Q(company_id=company_id)& Q(branch_id=branch_id))


    #             elif request_before_date:
    #                 request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')

    #                 if request_after_date:
    #                     request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #                     data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                    & Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                    & Q(company_id=company_id)& Q(branch_id=branch_id))
    #                 else:
    #                     data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                    & Q(company_id=company_id)
    #                                                                    & Q(branch_id=branch_id))



    #             elif request_after_date:
    #                 request_after_date_ = datetime.strptime(request_after_date,'%Y-%m-%d')
    #                 data_obj = och_product_master.objects(Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                & Q(company_id=company_id)& Q(branch_id=branch_id))

    #             else:
    #                 data_obj = och_product_master.objects(Q(company_id=company_id)& Q(branch_id=branch_id))




    #     ############ else Get Company Specific Data ################
    #     # Else Avoid Above
    #     else:

    #         # Is Section Is For Query Data Related Logic

    #         if prd_SKU_ID:
    #             data_obj = och_product_master.objects(prd_SKU_ID=prd_SKU_ID)

    #         elif prd_Status:
    #             if request_before_date:
    #                 request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')

    #                 if request_after_date:
    #                     request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #                     data_obj = och_product_master.objects(Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                    & Q(prd_Status=prd_Status)
    #                                                                    & Q(company_id=company_id))
    #                 else:
    #                     data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                    & Q(prd_Status=prd_Status)
    #                                                                    & Q(company_id=company_id))


    #             else: data_obj = och_product_master.objects(Q(prd_Status=prd_Status)
    #                                                                    & Q(company_id=company_id))


    #         elif request_before_date:
    #             request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')

    #             if request_after_date:
    #                 request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #                 data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                & Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                & Q(company_id=company_id))
    #             else:
    #                 data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                & Q(company_id=company_id))



    #         elif request_after_date:
    #             request_after_date_ = datetime.strptime(request_after_date,'%Y-%m-%d')
    #             data_obj = och_product_master.objects(Q(prd_Entry_Date__lt=request_after_date_)
    #                                                            & Q(company_id=company_id))

    #         else:
    #             data_obj = och_product_master.objects(company_id=company_id)





    # # Else Search For All enquiry And Based on Other parameters

    # else:


    #     #Check For Open Status
    #     if prd_Status == 'Open':
    #         data_obj = och_product_master.objects(Q(prd_Status__ne='Accepted-And-Closed')& Q(prd_Status__ne='Draft'))


    #     else:
    #         # data_obj = och_product_master.objects(Q(prd_Status=prd_Status))
    #         data_obj = och_product_master.objects()



    #     # Is Section Is For Query Data Related Logic

    #     if prd_SKU_ID:
    #         data_obj = och_product_master.objects(prd_SKU_ID=prd_SKU_ID)

    #     elif prd_Status:
    #         if request_before_date:
    #             request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')

    #             if request_after_date:
    #                 request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #                 data_obj = och_product_master.objects(Q(prd_Entry_Date__lt=request_after_date_)
    #                                                                & Q(prd_Status=prd_Status))
    #             else:
    #                 data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                                & Q(prd_Status=prd_Status))


    #         else: data_obj = och_product_master.objects(prd_Status=prd_Status)


    #     elif request_before_date:
    #         request_before_date_ = datetime.strptime(request_before_date, '%Y-%m-%d')

    #         if request_after_date:
    #             request_after_date_ = datetime.strptime(request_after_date, '%Y-%m-%d')
    #             data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_)
    #                                                            & Q(prd_Entry_Date__lt=request_after_date_))
    #         else:
    #             data_obj = och_product_master.objects(Q(prd_Entry_Date__gt=request_before_date_))



    #     elif request_after_date:
    #         request_after_date_ = datetime.strptime(request_after_date,'%Y-%m-%d')
    #         data_obj = och_product_master.objects(Q(prd_Entry_Date__lt=request_after_date_))

    #     else:
    #         data_obj = och_product_master.objects()


    if prd_SKU_ID:
        data_obj = och_product_master.objects(prd_SKU_ID=prd_SKU_ID)

    elif prd_Product_category:
        data_obj = och_product_master.objects(prd_Product_category=prd_Product_category)

    else:
        data_obj = och_product_master.objects()  
   
    
    # Declaring List For Order Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic[ 'prd_Product_category' ] = i.prd_Product_category
        dic[ 'prd_Product_Title' ] = i.prd_Product_Title
        dic[ 'prd_Collection_Name' ] = i.prd_Collection_Name
        dic[ 'prd_Brand' ] = i.prd_Brand
        dic[ 'prd_SKU_ID' ] = i.prd_SKU_ID
        dic[ 'prd_Color' ] = i.prd_Color
        dic[ 'prd_Capacity_Units' ] = i.prd_Capacity_Units
        dic[ 'prd_Capacity_Value' ] = i.prd_Capacity_Value
        dic[ 'prd_Included_Components' ] = i.prd_Included_Components
        dic[ 'prd_Standard_Price' ] = i.prd_Standard_Price
        dic[ 'prd_MRP' ] = i.prd_MRP
        dic[ 'prd_Manufacturer' ] = i.prd_Manufacturer
        dic[ 'prd_Product_Length' ] = i.prd_Product_Length
        dic[ 'prd_Product_Breadth' ] = i.prd_Product_Breadth
        dic[ 'prd_Product_Height' ] = i.prd_Product_Height
        dic[ 'prd_Product_Weight' ] = i.prd_Product_Weight
        dic[ 'prd_HSN_Code' ] = i.prd_HSN_Code
        dic[ 'prd_GST_applicable' ] = i.prd_GST_applicable
        dic[ 'prd_Qty' ] = i.prd_Qty
        dic[ 'prd_Main_View_Image' ] = i.prd_Main_View_Image
        dic[ 'prd_Front_View_Image' ] = i.prd_Front_View_Image
        dic[ 'prd_Side_View_Image' ] = i.prd_Side_View_Image
        dic[ 'prd_Commercial_View_Image_1' ] = i.prd_Commercial_View_Image_1
        dic[ 'prd_Explainer_view_image' ] = i.prd_Explainer_view_image
        dic[ 'prd_Commercial_View_Image_2' ] = i.prd_Commercial_View_Image_2
        dic[ 'prd_Product_Description' ] = i.prd_Product_Description
        dic[ 'prd_Feature_1' ] = i.prd_Feature_1
        dic[ 'prd_Feature_2' ] = i.prd_Feature_2
        dic[ 'prd_Feature_3' ] = i.prd_Feature_3
        dic[ 'prd_Feature_4' ] = i.prd_Feature_4
        dic[ 'prd_Feature_5' ] = i.prd_Feature_5
        dic[ 'prd_Search_Terms' ] = i.prd_Search_Terms
        dic[ 'prd_Search_Terms_Keywords_1' ] = i.prd_Search_Terms_Keywords_1
        dic[ 'prd_Search_Terms_Keywords_2' ] = i.prd_Search_Terms_Keywords_2
        dic[ 'prd_Search_Terms_Keywords_3' ] = i.prd_Search_Terms_Keywords_3
        dic[ 'prd_Search_Terms_Keywords_4' ] = i.prd_Search_Terms_Keywords_4
        dic[ 'prd_Search_Terms_Keywords_5' ] = i.prd_Search_Terms_Keywords_5
        dic[ 'prd_Main_Image_URL' ] = i.prd_Main_Image_URL
        dic[ 'prd_Package_Length' ] = i.prd_Package_Length
        dic[ 'prd_Package_Breadth' ] = i.prd_Package_Breadth
        dic[ 'prd_Package_Height' ] = i.prd_Package_Height
        dic[ 'prd_Package_Weight' ] = i.prd_Package_Weight
        dic[ 'prd_Big_Carton_Dimension' ] = i.prd_Big_Carton_Dimension
        dic[ 'prd_Big_Carton_Weight' ] = i.prd_Big_Carton_Weight
        dic[ 'prd_Master_Pack_Details' ] = i.prd_Master_Pack_Details
        dic[ 'prd_Barcode_UPC_Model_Number' ] = i.prd_Barcode_UPC_Model_Number
        dic[ 'prd_Category' ] = i.prd_Category
        dic[ 'Parent_SKU' ] = i.Parent_SKU
        # dic[ 'user_id' ] = i.user_id

        
        list_of_data.append(dic)

        # Sort List By Dates
        # list_of_data.sort(key=lambda r: r['dms_Lead_Date'], reverse=True)


     # This Section Is For Pagination Logic

    start_data_no = start_data_no
    end_data_no = start_data_no + total_result

    # Adding Exception Handling For if Geiven Start Page no Is Not In Index
    list_of_data_for_pagination = list_of_data[start_data_no:end_data_no+1]

    # There Is No Data For Perticular Query

    if len(list_of_data_for_pagination)<1:
        dic = {}
        dic[ 'prd_Product_category' ] = 'Data Not Available'
        dic[ 'prd_Product_Title' ] = 'Data Not Available'
        dic[ 'prd_Collection_Name' ] = 'Data Not Available'
        dic[ 'prd_Brand' ] = 'Data Not Available'
        dic[ 'prd_SKU_ID' ] = 'Data Not Available'
        dic[ 'prd_Color' ] = 'Data Not Available'
        dic[ 'prd_Capacity_Units' ] = 'Data Not Available'
        dic[ 'prd_Capacity_Value' ] = 'Data Not Available'
        dic[ 'prd_Included_Components' ] = 'Data Not Available'
        dic[ 'prd_Standard_Price' ] = 'Data Not Available'
        dic[ 'prd_MRP' ] = 'Data Not Available'
        dic[ 'prd_Manufacturer' ] = 'Data Not Available'
        dic[ 'prd_Product_Length' ] = 'Data Not Available'
        dic[ 'prd_Product_Breadth' ] = 'Data Not Available'
        dic[ 'prd_Product_Height' ] = 'Data Not Available'
        dic[ 'prd_Product_Weight' ] = 'Data Not Available'
        dic[ 'prd_HSN_Code' ] = 'Data Not Available'
        dic[ 'prd_GST_applicable' ] = 'Data Not Available'
        dic[ 'prd_Qty' ] = 'Data Not Available'
        dic[ 'prd_Main_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Front_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Side_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Commercial_View_Image_1' ] = 'Data Not Available'
        dic[ 'prd_Explainer_view_image' ] = 'Data Not Available'
        dic[ 'prd_Commercial_View_Image_2' ] = 'Data Not Available'
        dic[ 'prd_Product_Description' ] = 'Data Not Available'
        dic[ 'prd_Feature_1' ] = 'Data Not Available'
        dic[ 'prd_Feature_2' ] = 'Data Not Available'
        dic[ 'prd_Feature_3' ] = 'Data Not Available'
        dic[ 'prd_Feature_4' ] = 'Data Not Available'
        dic[ 'prd_Feature_5' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_1' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_2' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_3' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_4' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_5' ] = 'Data Not Available'
        dic[ 'prd_Main_Image_URL' ] = 'Data Not Available'
        dic[ 'prd_Package_Length' ] = 'Data Not Available'
        dic[ 'prd_Package_Breadth' ] = 'Data Not Available'
        dic[ 'prd_Package_Height' ] = 'Data Not Available'
        dic[ 'prd_Package_Weight' ] = 'Data Not Available'
        dic[ 'prd_Big_Carton_Dimension' ] = 'Data Not Available'
        dic[ 'prd_Big_Carton_Weight' ] = 'Data Not Available'
        dic[ 'prd_Master_Pack_Details' ] = 'Data Not Available'
        dic[ 'prd_Barcode_UPC_Model_Number' ] = 'Data Not Available'
        dic[ 'prd_Category' ] = 'Data Not Available'
        dic[ 'user_id' ] = 'Data Not Available'
        dic[ 'Parent_SKU' ] = 'Data Not Available'


        list_of_data_for_pagination.append(dic)

    return list_of_data_for_pagination




def func_get_page_data(start_data_no=0,
                        page_id = None,
                        company_id = None,
                        ):

    
    if company_id:
        data_obj = och_page_master.objects(company_id=company_id)
    # elif dms_Company_Type:
    #     data_obj = dms_claims_master.objects(dms_Company_Type=dms_Company_Type)
    
    # else:
    #     data_obj = dms_claims_master.objects
    
    # Declaring List For Order Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic['page_id'] = i.page_id
        dic['page_name'] = i.page_name
        dic['page_url'] = i.page_url
        dic['company_id'] = i.company_id
        dic['page_type'] = i.page_type

        list_of_data.append(dic)

        # Sort List By Dates
        # list_of_data.sort(key=lambda r: r['cart_Entry_Date'], reverse=True)
    return list_of_data










#############################webfront#########################
def func_get_page_component_data(start_data_no=0,
                                Page_id = None,
                                company_id = None,
                                ):

    
    if Page_id:
        data_obj = webfront_page_component_master.objects(Page_id=Page_id)
    # elif dms_Company_Type:
    #     data_obj = dms_claims_master.objects(dms_Company_Type=dms_Company_Type)
    
    # else:
    #     data_obj = dms_claims_master.objects
    
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




        # dic['page_component_id'] = i.page_component_id
        # dic['page_id'] = i.page_id
        # dic['component_name'] = i.component_name
        # dic['sequence'] = i.sequence
        # dic['element'] = i.element
        # dic['company_id'] = i.company_id
        # dic['link_name'] = i.link_name
        # dic['link_url'] = i.link_url
        # dic['font_color'] = i.font_color
        # dic['hover_color'] = i.hover_color
        # dic['bg_color'] = i.bg_color
        # dic['select_color'] = i.select_color
        # dic['dropdown_name'] = i.dropdown_name
        # dic['dropdown_data'] = i.dropdown_data
        # dic['collection_name'] = i.collection_name
        # dic['image'] = i.image
        # dic['button_link'] = i.button_link
        # dic['description'] = i.description
        # dic['partial_file_path'] = i.partial_file_path

        list_of_data.append(dic)

        # Sort List By Dates
        # list_of_data.sort(key=lambda r: r['cart_Entry_Date'], reverse=True)
    return list_of_data


def func_get_page_component_element(
                        page_id = None,
                        company_id = None,
                        ):

    
    if company_id:
        data_obj = page_component_element_master.objects(company_id=company_id)
    # elif dms_Company_Type:
    #     data_obj = dms_claims_master.objects(dms_Company_Type=dms_Company_Type)
    
    # else:
    #     data_obj = dms_claims_master.objects
    
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

# def func_get_page_component_data(start_data_no=0,
#                                 page_id = None,
#                                 company_id = None,
#                                 ):

    
#     if page_id:
#         data_obj = webfront_page_component_master.objects(page_id=page_id)
#     # elif dms_Company_Type:
#     #     data_obj = dms_claims_master.objects(dms_Company_Type=dms_Company_Type)
    
#     # else:
#     #     data_obj = dms_claims_master.objects
    
#     # Declaring List For Order Data

#     list_of_data = []

#     # Getting Data From Data Object

#     for i in data_obj:
#         dic = {}
#         dic['page_component_id'] = i.page_component_id
#         dic['page_id'] = i.page_id
#         dic['component_name'] = i.component_name
#         dic['sequence'] = i.sequence
#         dic['element'] = i.element
#         dic['company_id'] = i.company_id
#         dic['link_name'] = i.link_name
#         dic['link_url'] = i.link_url
#         dic['font_color'] = i.font_color
#         dic['hover_color'] = i.hover_color
#         dic['bg_color'] = i.bg_color
#         dic['select_color'] = i.select_color
#         dic['dropdown_name'] = i.dropdown_name
#         dic['dropdown_data'] = i.dropdown_data
#         dic['collection_name'] = i.collection_name
#         dic['image'] = i.image
#         dic['button_link'] = i.button_link
#         dic['description'] = i.description

#         list_of_data.append(dic)

#         # Sort List By Dates
#         # list_of_data.sort(key=lambda r: r['cart_Entry_Date'], reverse=True)
#     return list_of_data




####################################################################################################################
#   TVL Section
####################################################################################################################

# This Function Getting All Data From Product Master 

def func_get_tvl_product(start_data_no=0,
                                total_result=300,
                                request_before_date = None,
                                request_after_date = None,

                                prd_Product_Name = None,
                                prd_Brand = None,
                                prd_SKU_ID = None,
                                prd_Manufacturer = None,
                                prd_HSN_Code = None,
                                prd_Search_Terms = None,
                                prd_Search_Terms_Keywords_1 = None,
                                
                                prd_Status = None,
                                assigned_to = None,

                                user_id = None,
                                company_id = None,
                                department_id = None,
                                branch_id = None,
                                prd_Product_category = None,
                                ):




    if prd_SKU_ID:
        data_obj = tvl_product_master.objects(prd_SKU_ID=prd_SKU_ID)

    elif prd_Product_category:
        data_obj = tvl_product_master.objects(prd_Product_category=prd_Product_category)

    else:
        data_obj = tvl_product_master.objects()  
   
    
    # Declaring List For Order Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic[ 'prd_Product_category' ] = i.prd_Product_category
        dic[ 'prd_Product_Title' ] = i.prd_Product_Title
        dic[ 'prd_Collection_Name' ] = i.prd_Collection_Name
        dic[ 'prd_Brand' ] = i.prd_Brand
        dic[ 'prd_SKU_ID' ] = i.prd_SKU_ID
        dic[ 'prd_Color' ] = i.prd_Color
        dic[ 'prd_Capacity_Units' ] = i.prd_Capacity_Units
        dic[ 'prd_Capacity_Value' ] = i.prd_Capacity_Value
        dic[ 'prd_Included_Components' ] = i.prd_Included_Components
        dic[ 'prd_Standard_Price' ] = i.prd_Standard_Price
        dic[ 'prd_MRP' ] = i.prd_MRP
        dic[ 'prd_Manufacturer' ] = i.prd_Manufacturer
        dic[ 'prd_Product_Length' ] = i.prd_Product_Length
        dic[ 'prd_Product_Breadth' ] = i.prd_Product_Breadth
        dic[ 'prd_Product_Height' ] = i.prd_Product_Height
        dic[ 'prd_Product_Weight' ] = i.prd_Product_Weight
        dic[ 'prd_HSN_Code' ] = i.prd_HSN_Code
        dic[ 'prd_GST_applicable' ] = i.prd_GST_applicable
        dic[ 'prd_Qty' ] = i.prd_Qty
        dic[ 'prd_Main_View_Image' ] = i.prd_Main_View_Image
        dic[ 'prd_Front_View_Image' ] = i.prd_Front_View_Image
        dic[ 'prd_Side_View_Image' ] = i.prd_Side_View_Image
        dic[ 'prd_Commercial_View_Image_1' ] = i.prd_Commercial_View_Image_1
        dic[ 'prd_Explainer_view_image' ] = i.prd_Explainer_view_image
        dic[ 'prd_Commercial_View_Image_2' ] = i.prd_Commercial_View_Image_2
        dic[ 'prd_Product_Description' ] = i.prd_Product_Description
        dic[ 'prd_Feature_1' ] = i.prd_Feature_1
        dic[ 'prd_Feature_2' ] = i.prd_Feature_2
        dic[ 'prd_Feature_3' ] = i.prd_Feature_3
        dic[ 'prd_Feature_4' ] = i.prd_Feature_4
        dic[ 'prd_Feature_5' ] = i.prd_Feature_5
        dic[ 'prd_Search_Terms' ] = i.prd_Search_Terms
        dic[ 'prd_Search_Terms_Keywords_1' ] = i.prd_Search_Terms_Keywords_1
        dic[ 'prd_Search_Terms_Keywords_2' ] = i.prd_Search_Terms_Keywords_2
        dic[ 'prd_Search_Terms_Keywords_3' ] = i.prd_Search_Terms_Keywords_3
        dic[ 'prd_Search_Terms_Keywords_4' ] = i.prd_Search_Terms_Keywords_4
        dic[ 'prd_Search_Terms_Keywords_5' ] = i.prd_Search_Terms_Keywords_5
        dic[ 'prd_Main_Image_URL' ] = i.prd_Main_Image_URL
        dic[ 'prd_Package_Length' ] = i.prd_Package_Length
        dic[ 'prd_Package_Breadth' ] = i.prd_Package_Breadth
        dic[ 'prd_Package_Height' ] = i.prd_Package_Height
        dic[ 'prd_Package_Weight' ] = i.prd_Package_Weight
        dic[ 'prd_Big_Carton_Dimension' ] = i.prd_Big_Carton_Dimension
        dic[ 'prd_Big_Carton_Weight' ] = i.prd_Big_Carton_Weight
        dic[ 'prd_Master_Pack_Details' ] = i.prd_Master_Pack_Details
        dic[ 'prd_Barcode_UPC_Model_Number' ] = i.prd_Barcode_UPC_Model_Number
        dic[ 'prd_Category' ] = i.prd_Category
        dic[ 'Parent_SKU' ] = i.Parent_SKU
        # dic[ 'user_id' ] = i.user_id

        
        list_of_data.append(dic)

        # Sort List By Dates
        # list_of_data.sort(key=lambda r: r['dms_Lead_Date'], reverse=True)


     # This Section Is For Pagination Logic

    start_data_no = start_data_no
    end_data_no = start_data_no + total_result

    # Adding Exception Handling For if Geiven Start Page no Is Not In Index
    list_of_data_for_pagination = list_of_data[start_data_no:end_data_no+1]

    # There Is No Data For Perticular Query

    if len(list_of_data_for_pagination)<1:
        dic = {}
        dic[ 'prd_Product_category' ] = 'Data Not Available'
        dic[ 'prd_Product_Title' ] = 'Data Not Available'
        dic[ 'prd_Collection_Name' ] = 'Data Not Available'
        dic[ 'prd_Brand' ] = 'Data Not Available'
        dic[ 'prd_SKU_ID' ] = 'Data Not Available'
        dic[ 'prd_Color' ] = 'Data Not Available'
        dic[ 'prd_Capacity_Units' ] = 'Data Not Available'
        dic[ 'prd_Capacity_Value' ] = 'Data Not Available'
        dic[ 'prd_Included_Components' ] = 'Data Not Available'
        dic[ 'prd_Standard_Price' ] = 'Data Not Available'
        dic[ 'prd_MRP' ] = 'Data Not Available'
        dic[ 'prd_Manufacturer' ] = 'Data Not Available'
        dic[ 'prd_Product_Length' ] = 'Data Not Available'
        dic[ 'prd_Product_Breadth' ] = 'Data Not Available'
        dic[ 'prd_Product_Height' ] = 'Data Not Available'
        dic[ 'prd_Product_Weight' ] = 'Data Not Available'
        dic[ 'prd_HSN_Code' ] = 'Data Not Available'
        dic[ 'prd_GST_applicable' ] = 'Data Not Available'
        dic[ 'prd_Qty' ] = 'Data Not Available'
        dic[ 'prd_Main_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Front_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Side_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Commercial_View_Image_1' ] = 'Data Not Available'
        dic[ 'prd_Explainer_view_image' ] = 'Data Not Available'
        dic[ 'prd_Commercial_View_Image_2' ] = 'Data Not Available'
        dic[ 'prd_Product_Description' ] = 'Data Not Available'
        dic[ 'prd_Feature_1' ] = 'Data Not Available'
        dic[ 'prd_Feature_2' ] = 'Data Not Available'
        dic[ 'prd_Feature_3' ] = 'Data Not Available'
        dic[ 'prd_Feature_4' ] = 'Data Not Available'
        dic[ 'prd_Feature_5' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_1' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_2' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_3' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_4' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_5' ] = 'Data Not Available'
        dic[ 'prd_Main_Image_URL' ] = 'Data Not Available'
        dic[ 'prd_Package_Length' ] = 'Data Not Available'
        dic[ 'prd_Package_Breadth' ] = 'Data Not Available'
        dic[ 'prd_Package_Height' ] = 'Data Not Available'
        dic[ 'prd_Package_Weight' ] = 'Data Not Available'
        dic[ 'prd_Big_Carton_Dimension' ] = 'Data Not Available'
        dic[ 'prd_Big_Carton_Weight' ] = 'Data Not Available'
        dic[ 'prd_Master_Pack_Details' ] = 'Data Not Available'
        dic[ 'prd_Barcode_UPC_Model_Number' ] = 'Data Not Available'
        dic[ 'prd_Category' ] = 'Data Not Available'
        dic[ 'user_id' ] = 'Data Not Available'
        dic[ 'Parent_SKU' ] = 'Data Not Available'


        list_of_data_for_pagination.append(dic)

    return list_of_data_for_pagination




# New add_to_cart Creation Functions for TVL

def func_create_tvl_add_to_cart(
    prd_SKU_ID = '',
    prd_Product_Title = '',
    prd_MRP = '',
    prd_Standard_Price  = '',
    prd_Qty  = '',
    prd_Main_View_Image = '',
    cart_Entry_Date= '',
    user_id = '',
    visit_id = '',
        ):

 
    create_object = tvl_add_to_cart_master(
        prd_SKU_ID = prd_SKU_ID,
        prd_Product_Title = prd_Product_Title,
        prd_MRP = prd_MRP,
        prd_Standard_Price = prd_Standard_Price,
        prd_Qty = prd_Qty,
        prd_Main_View_Image = prd_Main_View_Image,
        cart_Entry_Date = cart_Entry_Date,
        user_id = user_id,
        visit_id = visit_id
        )

    # Save Create Object data in Database
    create_object.save()
    response = {'Response': 'One product added to cart Sucssesfully'}
    return response

# Update Functions for Updating Contact data

def func_update_tvl_add_to_cart( 
    prd_SKU_ID = '',
    prd_Product_Title = '',
    prd_MRP = '',
    prd_Standard_Price  = '',
    prd_Qty  = '',
    prd_Main_View_Image = '',
    cart_Entry_Date= '',
    prd_total_amount = '',
    user_id = '',
    visit_id = ''):

    # dms_contact_Id = dms_contact_Id
    tvl_add_to_cart_master.objects(prd_SKU_ID=prd_SKU_ID).update_one(
        # set__prd_SKU_ID = prd_SKU_ID,
        set__prd_Product_Title = prd_Product_Title,
        set__prd_MRP = prd_MRP,
        set__prd_Standard_Price = prd_Standard_Price,
        set__prd_Qty = prd_Qty,
        set__prd_Main_View_Image = prd_Main_View_Image,
        set__cart_Entry_Date = cart_Entry_Date,
        set__prd_total_amount = prd_total_amount,
        set__user_id = user_id,
        set__visit_id = visit_id )

    response = {'Response': 'product Updated to cart Sucssesfully'}

    return response




# This Function Getting All TVL Cart Data From add_to_cart Master By userId

def func_get_tvl_cart_data(start_data_no=0,
                        user_id = None,
                        visit_id = None,
                        
                        ):
    if user_id:
        data_obj = tvl_add_to_cart_master.objects(user_id=user_id)
    elif visit_id:
        data_obj = tvl_add_to_cart_master.objects(visit_id=visit_id)
    
    # Declaring List For Cart Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic['prd_SKU_ID'] = i.prd_SKU_ID
        dic['prd_Product_Title'] = i.prd_Product_Title
        dic['prd_MRP'] = i.prd_MRP
        dic['prd_Standard_Price'] = i.prd_Standard_Price
        dic['prd_Qty'] = i.prd_Qty
        dic['user_id'] = i.user_id
        dic['visit_id'] = i.visit_id
        dic['prd_Main_View_Image'] = i.prd_Main_View_Image
        dic['cart_Entry_Date'] = i.cart_Entry_Date
        
        list_of_data.append(dic)

        # Sort List By Dates
        list_of_data.sort(key=lambda r: r['cart_Entry_Date'], reverse=True)


     # This Section Is For Pagination Logic

    # start_data_no = start_data_no
    # end_data_no = start_data_no + total_result

    # Adding Exception Handling For if Geiven Start Page no Is Not In Index
    # list_of_data_for_pagination = list_of_data[start_data_no:end_data_no+1]

    # There Is No Data For Perticular Query

    # if len(list_of_data_for_pagination)<1:
    #     dic = {}
    #     dic['prd_SKU_ID'] = "Data Not Available"
    #     dic['prd_Product_Title'] = "Data Not Available"
    #     dic['prd_MRP'] = "Data Not Available"
    #     dic['prd_Standard_Price'] = "Data Not Available"
    #     dic['prd_Qty'] = "Data Not Available"
    #     dic['user_id'] = "Data Not Available"
       

    #     list_of_data_for_pagination.append(dic)

    # return list_of_data_for_pagination
    return list_of_data



# New Checkout Creation Functions for TVL

def func_tvl_checkout(
    chkot_last_change = '',
    chkot_First_Name = '',
    chkot_Last_Name = '', 
    chkot_email = '',
    chkot_Phone = '',
    chkot_Address = '',
    chkot_City = '',
    chkot_Pincode = '',
    chkot_State = '',
    chkot_Order_Note = '',
    # chkot_token = '',
    chkot_quantity = '',
    # chkot_billing_address = '',
    # chkot_shipping_address = '',
    # chkot_shipping_method = '',
    # chkot_note = '',
    # chkot_currency = '',
    # chkot_discount_amount = '',
    # chkot_discount_name = '',
    # chkot_translated_discount_name = '',
    # chkot_voucher_code = '',
    # chkot_gift_cards = '',
    # user_id = '',
    visit_id = '',
        ):

 
    create_object = tvl_checkout_master(
        chkot_last_change = chkot_last_change,
        chkot_First_Name = chkot_First_Name,
        chkot_Last_Name  = chkot_Last_Name,
        chkot_email = chkot_email,
        chkot_Phone = chkot_Phone,
        chkot_Address = chkot_Address,
        chkot_City = chkot_City,
        chkot_Pincode = chkot_Pincode,
        chkot_State = chkot_State,
        chkot_Order_Note = chkot_Order_Note,
        # chkot_token = chkot_token,
        chkot_quantity = chkot_quantity,
        # chkot_billing_address = chkot_billing_address,
        # chkot_shipping_address = chkot_shipping_address,
        # chkot_shipping_method = chkot_shipping_method,
        # chkot_note = chkot_note,
        # chkot_currency = chkot_currency,
        # chkot_discount_amount = chkot_discount_amount,
        # chkot_discount_name = chkot_discount_name,
        # chkot_translated_discount_name = chkot_translated_discount_name,
        # chkot_voucher_code = chkot_voucher_code,
        # chkot_gift_cards = chkot_gift_cards,
        # user_id = user_id,
        visit_id = visit_id,
        

        )


    # Save Create Object data in Database

    create_object.save()
    response = {'Response': 'One Checkout completed'}

    return response

def func_get_tvl_checkout_data(start_data_no=0,
                        user_id = None,
                        visit_id = None,
                        
                        ):
    if user_id:
        data_obj = tvl_checkout_master.objects(user_id=user_id)
    elif visit_id:
        data_obj = tvl_checkout_master.objects(visit_id=visit_id)
    
    # Declaring List For Cart Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic['chkot_last_change'] = i.chkot_last_change
        dic['chkot_First_Name'] = i.chkot_First_Name
        dic['chkot_Last_Name'] = i.chkot_Last_Name
        dic['chkot_email'] = i.chkot_email
        dic['chkot_Phone'] = i.chkot_Phone
        dic['chkot_Address'] = i.chkot_Address
        dic['chkot_City'] = i.chkot_City
        dic['chkot_Pincode'] = i.chkot_Pincode
        dic['chkot_State'] = i.chkot_State
        dic['chkot_Order_Note'] = i.chkot_Order_Note
        dic['chkot_quantity'] = i.chkot_quantity
        dic['visit_id'] = i.visit_id
        
        list_of_data.append(dic)

        # Sort List By Dates
        # list_of_data.sort(key=lambda r: r['cart_Entry_Date'], reverse=True)


     # This Section Is For Pagination Logic

    # start_data_no = start_data_no
    # end_data_no = start_data_no + total_result

    # Adding Exception Handling For if Geiven Start Page no Is Not In Index
    # list_of_data_for_pagination = list_of_data[start_data_no:end_data_no+1]

    # There Is No Data For Perticular Query

    # if len(list_of_data_for_pagination)<1:
    #     dic = {}
    #     dic['prd_SKU_ID'] = "Data Not Available"
    #     dic['prd_Product_Title'] = "Data Not Available"
    #     dic['prd_MRP'] = "Data Not Available"
    #     dic['prd_Standard_Price'] = "Data Not Available"
    #     dic['prd_Qty'] = "Data Not Available"
    #     dic['user_id'] = "Data Not Available"
       

    #     list_of_data_for_pagination.append(dic)

    # return list_of_data_for_pagination
    return list_of_data


# # New Address Creation Functions for TVL

# def func_tvl_checkout(
#     addr_First_Name= '',
#     addr_Last_Name= '',
#     addr_email= '',
#     addr_Phone= '',
#     addr_Address= '',
#     addr_City= '',
#     addr_Pincode= '',
#     addr_State= '',
#     addr_Order_Note= '',
#     visit_id = '',
#         ):

 
#     create_object = tvl_checkout_master(
#         chkot_last_change = chkot_last_change,
#         addr_First_Name = chkot_First_Name,
#         addr_Last_Name  = chkot_Last_Name,
#         addr_email = chkot_email,
#         addr_Phone = chkot_Phone,
#         addr_Address = chkot_Address,
#         addr_City = chkot_City,
#         addr_Pincode = chkot_Pincode,
#         addr_State = chkot_State,
#         chkot_Order_Note = chkot_Order_Note,
#         # chkot_token = chkot_token,
#         chkot_quantity = chkot_quantity,
#         # chkot_billing_address = chkot_billing_address,
#         # chkot_shipping_address = chkot_shipping_address,
#         # chkot_shipping_method = chkot_shipping_method,
#         # chkot_note = chkot_note,
#         # chkot_currency = chkot_currency,
#         # chkot_discount_amount = chkot_discount_amount,
#         # chkot_discount_name = chkot_discount_name,
#         # chkot_translated_discount_name = chkot_translated_discount_name,
#         # chkot_voucher_code = chkot_voucher_code,
#         # chkot_gift_cards = chkot_gift_cards,
#         # user_id = user_id,
#         visit_id = visit_id,
        

#         )


#     # Save Create Object data in Database

#     create_object.save()
#     response = {'Response': 'One Checkout completed'}

#     return response



####################################################################################################################
#   NKSHI Section
####################################################################################################################

# This Function Getting All Data From Product Master 

def func_get_nkshi_product(start_data_no=0,
                                total_result=300,
                                request_before_date = None,
                                request_after_date = None,

                                prd_Product_Name = None,
                                prd_Brand = None,
                                prd_SKU_ID = None,
                                prd_Manufacturer = None,
                                prd_HSN_Code = None,
                                prd_Search_Terms = None,
                                prd_Search_Terms_Keywords_1 = None,
                                
                                prd_Status = None,
                                assigned_to = None,

                                user_id = None,
                                company_id = None,
                                department_id = None,
                                branch_id = None,
                                prd_Product_category = None,
                                ):




    if prd_SKU_ID:
        data_obj = nkshi_product_master.objects(prd_SKU_ID=prd_SKU_ID)

    elif prd_Product_category:
        data_obj = nkshi_product_master.objects(prd_Product_category=prd_Product_category)

    else:
        data_obj = nkshi_product_master.objects()  
   
    
    # Declaring List For Order Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic[ 'prd_Product_category' ] = i.prd_Product_category
        dic[ 'prd_Product_Title' ] = i.prd_Product_Title
        dic[ 'prd_Collection_Name' ] = i.prd_Collection_Name
        dic[ 'prd_Brand' ] = i.prd_Brand
        dic[ 'prd_SKU_ID' ] = i.prd_SKU_ID
        dic[ 'prd_Color' ] = i.prd_Color
        dic[ 'prd_Capacity_Units' ] = i.prd_Capacity_Units
        dic[ 'prd_Capacity_Value' ] = i.prd_Capacity_Value
        dic[ 'prd_Included_Components' ] = i.prd_Included_Components
        dic[ 'prd_Standard_Price' ] = i.prd_Standard_Price
        dic[ 'prd_MRP' ] = i.prd_MRP
        dic[ 'prd_Manufacturer' ] = i.prd_Manufacturer
        dic[ 'prd_Product_Length' ] = i.prd_Product_Length
        dic[ 'prd_Product_Breadth' ] = i.prd_Product_Breadth
        dic[ 'prd_Product_Height' ] = i.prd_Product_Height
        dic[ 'prd_Product_Weight' ] = i.prd_Product_Weight
        dic[ 'prd_HSN_Code' ] = i.prd_HSN_Code
        dic[ 'prd_GST_applicable' ] = i.prd_GST_applicable
        dic[ 'prd_Qty' ] = i.prd_Qty
        dic[ 'prd_Main_View_Image' ] = i.prd_Main_View_Image
        dic[ 'prd_Front_View_Image' ] = i.prd_Front_View_Image
        dic[ 'prd_Side_View_Image' ] = i.prd_Side_View_Image
        dic[ 'prd_Commercial_View_Image_1' ] = i.prd_Commercial_View_Image_1
        dic[ 'prd_Explainer_view_image' ] = i.prd_Explainer_view_image
        dic[ 'prd_Commercial_View_Image_2' ] = i.prd_Commercial_View_Image_2
        dic[ 'prd_Product_Description' ] = i.prd_Product_Description
        dic[ 'prd_Feature_1' ] = i.prd_Feature_1
        dic[ 'prd_Feature_2' ] = i.prd_Feature_2
        dic[ 'prd_Feature_3' ] = i.prd_Feature_3
        dic[ 'prd_Feature_4' ] = i.prd_Feature_4
        dic[ 'prd_Feature_5' ] = i.prd_Feature_5
        dic[ 'prd_Search_Terms' ] = i.prd_Search_Terms
        dic[ 'prd_Search_Terms_Keywords_1' ] = i.prd_Search_Terms_Keywords_1
        dic[ 'prd_Search_Terms_Keywords_2' ] = i.prd_Search_Terms_Keywords_2
        dic[ 'prd_Search_Terms_Keywords_3' ] = i.prd_Search_Terms_Keywords_3
        dic[ 'prd_Search_Terms_Keywords_4' ] = i.prd_Search_Terms_Keywords_4
        dic[ 'prd_Search_Terms_Keywords_5' ] = i.prd_Search_Terms_Keywords_5
        dic[ 'prd_Main_Image_URL' ] = i.prd_Main_Image_URL
        dic[ 'prd_Package_Length' ] = i.prd_Package_Length
        dic[ 'prd_Package_Breadth' ] = i.prd_Package_Breadth
        dic[ 'prd_Package_Height' ] = i.prd_Package_Height
        dic[ 'prd_Package_Weight' ] = i.prd_Package_Weight
        dic[ 'prd_Big_Carton_Dimension' ] = i.prd_Big_Carton_Dimension
        dic[ 'prd_Big_Carton_Weight' ] = i.prd_Big_Carton_Weight
        dic[ 'prd_Master_Pack_Details' ] = i.prd_Master_Pack_Details
        dic[ 'prd_Barcode_UPC_Model_Number' ] = i.prd_Barcode_UPC_Model_Number
        dic[ 'prd_Category' ] = i.prd_Category
        dic[ 'Parent_SKU' ] = i.Parent_SKU
        # dic[ 'user_id' ] = i.user_id

        
        list_of_data.append(dic)

        # Sort List By Dates
        # list_of_data.sort(key=lambda r: r['dms_Lead_Date'], reverse=True)


     # This Section Is For Pagination Logic

    start_data_no = start_data_no
    end_data_no = start_data_no + total_result

    # Adding Exception Handling For if Geiven Start Page no Is Not In Index
    list_of_data_for_pagination = list_of_data[start_data_no:end_data_no+1]

    # There Is No Data For Perticular Query

    if len(list_of_data_for_pagination)<1:
        dic = {}
        dic[ 'prd_Product_category' ] = 'Data Not Available'
        dic[ 'prd_Product_Title' ] = 'Data Not Available'
        dic[ 'prd_Collection_Name' ] = 'Data Not Available'
        dic[ 'prd_Brand' ] = 'Data Not Available'
        dic[ 'prd_SKU_ID' ] = 'Data Not Available'
        dic[ 'prd_Color' ] = 'Data Not Available'
        dic[ 'prd_Capacity_Units' ] = 'Data Not Available'
        dic[ 'prd_Capacity_Value' ] = 'Data Not Available'
        dic[ 'prd_Included_Components' ] = 'Data Not Available'
        dic[ 'prd_Standard_Price' ] = 'Data Not Available'
        dic[ 'prd_MRP' ] = 'Data Not Available'
        dic[ 'prd_Manufacturer' ] = 'Data Not Available'
        dic[ 'prd_Product_Length' ] = 'Data Not Available'
        dic[ 'prd_Product_Breadth' ] = 'Data Not Available'
        dic[ 'prd_Product_Height' ] = 'Data Not Available'
        dic[ 'prd_Product_Weight' ] = 'Data Not Available'
        dic[ 'prd_HSN_Code' ] = 'Data Not Available'
        dic[ 'prd_GST_applicable' ] = 'Data Not Available'
        dic[ 'prd_Qty' ] = 'Data Not Available'
        dic[ 'prd_Main_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Front_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Side_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Commercial_View_Image_1' ] = 'Data Not Available'
        dic[ 'prd_Explainer_view_image' ] = 'Data Not Available'
        dic[ 'prd_Commercial_View_Image_2' ] = 'Data Not Available'
        dic[ 'prd_Product_Description' ] = 'Data Not Available'
        dic[ 'prd_Feature_1' ] = 'Data Not Available'
        dic[ 'prd_Feature_2' ] = 'Data Not Available'
        dic[ 'prd_Feature_3' ] = 'Data Not Available'
        dic[ 'prd_Feature_4' ] = 'Data Not Available'
        dic[ 'prd_Feature_5' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_1' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_2' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_3' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_4' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_5' ] = 'Data Not Available'
        dic[ 'prd_Main_Image_URL' ] = 'Data Not Available'
        dic[ 'prd_Package_Length' ] = 'Data Not Available'
        dic[ 'prd_Package_Breadth' ] = 'Data Not Available'
        dic[ 'prd_Package_Height' ] = 'Data Not Available'
        dic[ 'prd_Package_Weight' ] = 'Data Not Available'
        dic[ 'prd_Big_Carton_Dimension' ] = 'Data Not Available'
        dic[ 'prd_Big_Carton_Weight' ] = 'Data Not Available'
        dic[ 'prd_Master_Pack_Details' ] = 'Data Not Available'
        dic[ 'prd_Barcode_UPC_Model_Number' ] = 'Data Not Available'
        dic[ 'prd_Category' ] = 'Data Not Available'
        dic[ 'user_id' ] = 'Data Not Available'
        dic[ 'Parent_SKU' ] = 'Data Not Available'


        list_of_data_for_pagination.append(dic)

    return list_of_data_for_pagination




# New add_to_cart Creation Functions for NKSHI

def func_create_nkshi_add_to_cart(
    prd_SKU_ID = '',
    prd_Product_Title = '',
    prd_MRP = '',
    prd_Standard_Price  = '',
    prd_Qty  = '',
    prd_Main_View_Image = '',
    cart_Entry_Date= '',
    user_id = '',
        ):

 
    create_object = nkshi_add_to_cart_master(
        prd_SKU_ID = prd_SKU_ID,
        prd_Product_Title = prd_Product_Title,
        prd_MRP = prd_MRP,
        prd_Standard_Price = prd_Standard_Price,
        prd_Qty = prd_Qty,
        prd_Main_View_Image = prd_Main_View_Image,
        cart_Entry_Date = cart_Entry_Date,
        user_id = user_id,
        )

    # Save Create Object data in Database
    create_object.save()
    response = {'Response': 'One product added to cart Sucssesfully'}
    return response


# This Function Getting All NKSHI Cart Data From add_to_cart Master By userId

def func_get_nkshi_cart_data(start_data_no=0,
                        user_id = None,
                        company_id = None,
                        department_id = None,
                        branch_id = None,
                        ):
    if user_id:
        data_obj = nkshi_add_to_cart_master.objects(user_id=user_id)
    
    # Declaring List For Cart Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic['prd_SKU_ID'] = i.prd_SKU_ID
        dic['prd_Product_Title'] = i.prd_Product_Title
        dic['prd_MRP'] = i.prd_MRP
        dic['prd_Standard_Price'] = i.prd_Standard_Price
        dic['prd_Qty'] = i.prd_Qty
        dic['user_id'] = i.user_id
        dic['prd_Main_View_Image'] = i.prd_Main_View_Image
        dic['cart_Entry_Date'] = i.cart_Entry_Date
        
        list_of_data.append(dic)

        # Sort List By Dates
        list_of_data.sort(key=lambda r: r['cart_Entry_Date'], reverse=True)


     # This Section Is For Pagination Logic

    # start_data_no = start_data_no
    # end_data_no = start_data_no + total_result

    # Adding Exception Handling For if Geiven Start Page no Is Not In Index
    # list_of_data_for_pagination = list_of_data[start_data_no:end_data_no+1]

    # There Is No Data For Perticular Query

    # if len(list_of_data_for_pagination)<1:
    #     dic = {}
    #     dic['prd_SKU_ID'] = "Data Not Available"
    #     dic['prd_Product_Title'] = "Data Not Available"
    #     dic['prd_MRP'] = "Data Not Available"
    #     dic['prd_Standard_Price'] = "Data Not Available"
    #     dic['prd_Qty'] = "Data Not Available"
    #     dic['user_id'] = "Data Not Available"
       

    #     list_of_data_for_pagination.append(dic)

    # return list_of_data_for_pagination
    return list_of_data



# New Checkout Creation Functions for NKSHI

def func_nkshi_checkout(
    chkot_last_change = '',
    chkot_First_Name = '',
    chkot_Last_Name = '', 
    chkot_email = '',
    chkot_Phone = '',
    chkot_Address = '',
    chkot_City = '',
    chkot_Pincode = '',
    chkot_State = '',
    chkot_Order_Note = '',
    # chkot_token = '',
    chkot_quantity = '',
    # chkot_billing_address = '',
    # chkot_shipping_address = '',
    chkot_shipping_method = '',
    # chkot_note = '',
    chkot_currency = '',
    chkot_discount_amount = '',
    chkot_discount_name = '',
    chkot_translated_discount_name = '',
    chkot_voucher_code = '',
    chkot_gift_cards = '',
    user_id = '',
        ):

 
    create_object = nkshi_checkout_master(
        chkot_last_change = chkot_last_change,
        chkot_First_Name = chkot_First_Name,
        chkot_Last_Name  = chkot_Last_Name,
        chkot_email = chkot_email,
        chkot_Phone = chkot_Phone,
        chkot_Address = chkot_Address,
        chkot_City = chkot_City,
        chkot_Pincode = chkot_Pincode,
        chkot_State = chkot_State,
        chkot_Order_Note = chkot_Order_Note,
        # chkot_token = chkot_token,
        chkot_quantity = chkot_quantity,
        # chkot_billing_address = chkot_billing_address,
        # chkot_shipping_address = chkot_shipping_address,
        chkot_shipping_method = chkot_shipping_method,
        # chkot_note = chkot_note,
        chkot_currency = chkot_currency,
        chkot_discount_amount = chkot_discount_amount,
        chkot_discount_name = chkot_discount_name,
        chkot_translated_discount_name = chkot_translated_discount_name,
        chkot_voucher_code = chkot_voucher_code,
        chkot_gift_cards = chkot_gift_cards,
        user_id = user_id,
        

        )


    # Save Create Object data in Database

    create_object.save()
    response = {'Response': 'One Checkout completed'}

    return response





####################################################################################################################
#   Atlasware Section
####################################################################################################################

# This Function Getting All Data From Product Master 

def func_get_atlasware_product(start_data_no=0,
                                total_result=300,
                                request_before_date = None,
                                request_after_date = None,

                                prd_Product_Name = None,
                                prd_Brand = None,
                                prd_SKU_ID = None,
                                prd_Manufacturer = None,
                                prd_HSN_Code = None,
                                prd_Search_Terms = None,
                                prd_Search_Terms_Keywords_1 = None,
                                
                                prd_Status = None,
                                assigned_to = None,

                                user_id = None,
                                company_id = None,
                                department_id = None,
                                branch_id = None,
                                prd_Product_category = None,
                                ):




    if prd_SKU_ID:
        data_obj = atlasware_product_master.objects(prd_SKU_ID=prd_SKU_ID)

    elif prd_Product_category:
        data_obj = atlasware_product_master.objects(prd_Product_category=prd_Product_category)

    else:
        data_obj = atlasware_product_master.objects()  
   
    
    # Declaring List For Order Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic[ 'prd_Product_category' ] = i.prd_Product_category
        dic[ 'prd_Product_Title' ] = i.prd_Product_Title
        dic[ 'prd_Collection_Name' ] = i.prd_Collection_Name
        dic[ 'prd_Brand' ] = i.prd_Brand
        dic[ 'prd_SKU_ID' ] = i.prd_SKU_ID
        dic[ 'prd_Color' ] = i.prd_Color
        dic[ 'prd_Capacity_Units' ] = i.prd_Capacity_Units
        dic[ 'prd_Capacity_Value' ] = i.prd_Capacity_Value
        dic[ 'prd_Included_Components' ] = i.prd_Included_Components
        dic[ 'prd_Standard_Price' ] = i.prd_Standard_Price
        dic[ 'prd_MRP' ] = i.prd_MRP
        dic[ 'prd_Manufacturer' ] = i.prd_Manufacturer
        dic[ 'prd_Product_Length' ] = i.prd_Product_Length
        dic[ 'prd_Product_Breadth' ] = i.prd_Product_Breadth
        dic[ 'prd_Product_Height' ] = i.prd_Product_Height
        dic[ 'prd_Product_Weight' ] = i.prd_Product_Weight
        dic[ 'prd_HSN_Code' ] = i.prd_HSN_Code
        dic[ 'prd_GST_applicable' ] = i.prd_GST_applicable
        dic[ 'prd_Qty' ] = i.prd_Qty
        dic[ 'prd_Main_View_Image' ] = i.prd_Main_View_Image
        dic[ 'prd_Front_View_Image' ] = i.prd_Front_View_Image
        dic[ 'prd_Side_View_Image' ] = i.prd_Side_View_Image
        dic[ 'prd_Commercial_View_Image_1' ] = i.prd_Commercial_View_Image_1
        dic[ 'prd_Explainer_view_image' ] = i.prd_Explainer_view_image
        dic[ 'prd_Commercial_View_Image_2' ] = i.prd_Commercial_View_Image_2
        dic[ 'prd_Product_Description' ] = i.prd_Product_Description
        dic[ 'prd_Feature_1' ] = i.prd_Feature_1
        dic[ 'prd_Feature_2' ] = i.prd_Feature_2
        dic[ 'prd_Feature_3' ] = i.prd_Feature_3
        dic[ 'prd_Feature_4' ] = i.prd_Feature_4
        dic[ 'prd_Feature_5' ] = i.prd_Feature_5
        dic[ 'prd_Search_Terms' ] = i.prd_Search_Terms
        dic[ 'prd_Search_Terms_Keywords_1' ] = i.prd_Search_Terms_Keywords_1
        dic[ 'prd_Search_Terms_Keywords_2' ] = i.prd_Search_Terms_Keywords_2
        dic[ 'prd_Search_Terms_Keywords_3' ] = i.prd_Search_Terms_Keywords_3
        dic[ 'prd_Search_Terms_Keywords_4' ] = i.prd_Search_Terms_Keywords_4
        dic[ 'prd_Search_Terms_Keywords_5' ] = i.prd_Search_Terms_Keywords_5
        dic[ 'prd_Main_Image_URL' ] = i.prd_Main_Image_URL
        dic[ 'prd_Package_Length' ] = i.prd_Package_Length
        dic[ 'prd_Package_Breadth' ] = i.prd_Package_Breadth
        dic[ 'prd_Package_Height' ] = i.prd_Package_Height
        dic[ 'prd_Package_Weight' ] = i.prd_Package_Weight
        dic[ 'prd_Big_Carton_Dimension' ] = i.prd_Big_Carton_Dimension
        dic[ 'prd_Big_Carton_Weight' ] = i.prd_Big_Carton_Weight
        dic[ 'prd_Master_Pack_Details' ] = i.prd_Master_Pack_Details
        dic[ 'prd_Barcode_UPC_Model_Number' ] = i.prd_Barcode_UPC_Model_Number
        dic[ 'prd_Category' ] = i.prd_Category
        dic[ 'Parent_SKU' ] = i.Parent_SKU
        # dic[ 'user_id' ] = i.user_id

        
        list_of_data.append(dic)

        # Sort List By Dates
        # list_of_data.sort(key=lambda r: r['dms_Lead_Date'], reverse=True)


     # This Section Is For Pagination Logic

    start_data_no = start_data_no
    end_data_no = start_data_no + total_result

    # Adding Exception Handling For if Geiven Start Page no Is Not In Index
    list_of_data_for_pagination = list_of_data[start_data_no:end_data_no+1]

    # There Is No Data For Perticular Query

    if len(list_of_data_for_pagination)<1:
        dic = {}
        dic[ 'prd_Product_category' ] = 'Data Not Available'
        dic[ 'prd_Product_Title' ] = 'Data Not Available'
        dic[ 'prd_Collection_Name' ] = 'Data Not Available'
        dic[ 'prd_Brand' ] = 'Data Not Available'
        dic[ 'prd_SKU_ID' ] = 'Data Not Available'
        dic[ 'prd_Color' ] = 'Data Not Available'
        dic[ 'prd_Capacity_Units' ] = 'Data Not Available'
        dic[ 'prd_Capacity_Value' ] = 'Data Not Available'
        dic[ 'prd_Included_Components' ] = 'Data Not Available'
        dic[ 'prd_Standard_Price' ] = 'Data Not Available'
        dic[ 'prd_MRP' ] = 'Data Not Available'
        dic[ 'prd_Manufacturer' ] = 'Data Not Available'
        dic[ 'prd_Product_Length' ] = 'Data Not Available'
        dic[ 'prd_Product_Breadth' ] = 'Data Not Available'
        dic[ 'prd_Product_Height' ] = 'Data Not Available'
        dic[ 'prd_Product_Weight' ] = 'Data Not Available'
        dic[ 'prd_HSN_Code' ] = 'Data Not Available'
        dic[ 'prd_GST_applicable' ] = 'Data Not Available'
        dic[ 'prd_Qty' ] = 'Data Not Available'
        dic[ 'prd_Main_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Front_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Side_View_Image' ] = 'Data Not Available'
        dic[ 'prd_Commercial_View_Image_1' ] = 'Data Not Available'
        dic[ 'prd_Explainer_view_image' ] = 'Data Not Available'
        dic[ 'prd_Commercial_View_Image_2' ] = 'Data Not Available'
        dic[ 'prd_Product_Description' ] = 'Data Not Available'
        dic[ 'prd_Feature_1' ] = 'Data Not Available'
        dic[ 'prd_Feature_2' ] = 'Data Not Available'
        dic[ 'prd_Feature_3' ] = 'Data Not Available'
        dic[ 'prd_Feature_4' ] = 'Data Not Available'
        dic[ 'prd_Feature_5' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_1' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_2' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_3' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_4' ] = 'Data Not Available'
        dic[ 'prd_Search_Terms_Keywords_5' ] = 'Data Not Available'
        dic[ 'prd_Main_Image_URL' ] = 'Data Not Available'
        dic[ 'prd_Package_Length' ] = 'Data Not Available'
        dic[ 'prd_Package_Breadth' ] = 'Data Not Available'
        dic[ 'prd_Package_Height' ] = 'Data Not Available'
        dic[ 'prd_Package_Weight' ] = 'Data Not Available'
        dic[ 'prd_Big_Carton_Dimension' ] = 'Data Not Available'
        dic[ 'prd_Big_Carton_Weight' ] = 'Data Not Available'
        dic[ 'prd_Master_Pack_Details' ] = 'Data Not Available'
        dic[ 'prd_Barcode_UPC_Model_Number' ] = 'Data Not Available'
        dic[ 'prd_Category' ] = 'Data Not Available'
        dic[ 'user_id' ] = 'Data Not Available'
        dic[ 'Parent_SKU' ] = 'Data Not Available'


        list_of_data_for_pagination.append(dic)

    return list_of_data_for_pagination




# New add_to_cart Creation Functions for atlasware

def func_create_atlasware_add_to_cart(
    prd_SKU_ID = '',
    prd_Product_Title = '',
    prd_MRP = '',
    prd_Standard_Price  = '',
    prd_Qty  = '',
    prd_Main_View_Image = '',
    cart_Entry_Date= '',
    user_id = '',
        ):

 
    create_object = atlasware_add_to_cart_master(
        prd_SKU_ID = prd_SKU_ID,
        prd_Product_Title = prd_Product_Title,
        prd_MRP = prd_MRP,
        prd_Standard_Price = prd_Standard_Price,
        prd_Qty = prd_Qty,
        prd_Main_View_Image = prd_Main_View_Image,
        cart_Entry_Date = cart_Entry_Date,
        user_id = user_id,
        )

    # Save Create Object data in Database
    create_object.save()
    response = {'Response': 'One product added to cart Sucssesfully'}
    return response


# This Function Getting All ATLASWARE Cart Data From add_to_cart Master By userId

def func_get_atlasware_cart_data(start_data_no=0,
                        user_id = None,
                        company_id = None,
                        department_id = None,
                        branch_id = None,
                        ):
    if user_id:
        data_obj = atlasware_add_to_cart_master.objects(user_id=user_id)
    
    # Declaring List For Cart Data

    list_of_data = []

    # Getting Data From Data Object

    for i in data_obj:
        dic = {}
        dic['prd_SKU_ID'] = i.prd_SKU_ID
        dic['prd_Product_Title'] = i.prd_Product_Title
        dic['prd_MRP'] = i.prd_MRP
        dic['prd_Standard_Price'] = i.prd_Standard_Price
        dic['prd_Qty'] = i.prd_Qty
        dic['user_id'] = i.user_id
        dic['prd_Main_View_Image'] = i.prd_Main_View_Image
        dic['cart_Entry_Date'] = i.cart_Entry_Date
        
        list_of_data.append(dic)

        # Sort List By Dates
        list_of_data.sort(key=lambda r: r['cart_Entry_Date'], reverse=True)


     # This Section Is For Pagination Logic

    # start_data_no = start_data_no
    # end_data_no = start_data_no + total_result

    # Adding Exception Handling For if Geiven Start Page no Is Not In Index
    # list_of_data_for_pagination = list_of_data[start_data_no:end_data_no+1]

    # There Is No Data For Perticular Query

    # if len(list_of_data_for_pagination)<1:
    #     dic = {}
    #     dic['prd_SKU_ID'] = "Data Not Available"
    #     dic['prd_Product_Title'] = "Data Not Available"
    #     dic['prd_MRP'] = "Data Not Available"
    #     dic['prd_Standard_Price'] = "Data Not Available"
    #     dic['prd_Qty'] = "Data Not Available"
    #     dic['user_id'] = "Data Not Available"
       

    #     list_of_data_for_pagination.append(dic)

    # return list_of_data_for_pagination
    return list_of_data



# New Checkout Creation Functions for atlasware

def func_atlasware_checkout(
    chkot_last_change = '',
    chkot_First_Name = '',
    chkot_Last_Name = '', 
    chkot_email = '',
    chkot_Phone = '',
    chkot_Address = '',
    chkot_City = '',
    chkot_Pincode = '',
    chkot_State = '',
    chkot_Order_Note = '',
    # chkot_token = '',
    chkot_quantity = '',
    # chkot_billing_address = '',
    # chkot_shipping_address = '',
    chkot_shipping_method = '',
    # chkot_note = '',
    chkot_currency = '',
    chkot_discount_amount = '',
    chkot_discount_name = '',
    chkot_translated_discount_name = '',
    chkot_voucher_code = '',
    chkot_gift_cards = '',
    user_id = '',
        ):

 
    create_object = atlasware_checkout_master(
        chkot_last_change = chkot_last_change,
        chkot_First_Name = chkot_First_Name,
        chkot_Last_Name  = chkot_Last_Name,
        chkot_email = chkot_email,
        chkot_Phone = chkot_Phone,
        chkot_Address = chkot_Address,
        chkot_City = chkot_City,
        chkot_Pincode = chkot_Pincode,
        chkot_State = chkot_State,
        chkot_Order_Note = chkot_Order_Note,
        # chkot_token = chkot_token,
        chkot_quantity = chkot_quantity,
        # chkot_billing_address = chkot_billing_address,
        # chkot_shipping_address = chkot_shipping_address,
        chkot_shipping_method = chkot_shipping_method,
        # chkot_note = chkot_note,
        chkot_currency = chkot_currency,
        chkot_discount_amount = chkot_discount_amount,
        chkot_discount_name = chkot_discount_name,
        chkot_translated_discount_name = chkot_translated_discount_name,
        chkot_voucher_code = chkot_voucher_code,
        chkot_gift_cards = chkot_gift_cards,
        user_id = user_id,
        

        )


    # Save Create Object data in Database

    create_object.save()
    response = {'Response': 'One Checkout completed'}

    return response

