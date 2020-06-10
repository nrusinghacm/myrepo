# pylint: disable=no-member, missing-docstring, unused-variable, invalid-name


"""

This Program Is For SKF Means All Models User In SKF Those Are Defined Here

"""

# Import All Neccessary Modules
# from mongoengine import connect, disconnect


# Import Our Modules

from APP.UserManagement.models import db

class och_product_master(db.Document):
    prd_Product_category = db.StringField(default='')
    prd_Product_Title = db.StringField(default='')
    prd_Collection_Name = db.StringField(default='')
    prd_Brand = db.StringField(default='')
    prd_SKU_ID = db.StringField(default='')
    prd_Color = db.StringField(default='')
    prd_Capacity_Units = db.StringField(default='')
    prd_Capacity_Value = db.IntField(default='')
    prd_Included_Components = db.StringField(default='')
    prd_Standard_Price = db.FloatField(default='')
    prd_MRP = db.FloatField(default='')
    prd_Manufacturer = db.StringField(default='')
    prd_Product_Length = db.FloatField(default='')
    prd_Product_Breadth = db.FloatField(default='')
    prd_Product_Height = db.FloatField(default='')
    prd_Product_Weight = db.FloatField(default='')
    prd_HSN_Code = db.StringField(default='')
    prd_GST_applicable = db.StringField(default='')
    prd_Qty = db.IntField(default='')
    prd_Main_View_Image = db.StringField(default='')
    prd_Front_View_Image = db.StringField(default='')
    prd_Side_View_Image = db.StringField(default='')
    prd_Commercial_View_Image_1 = db.StringField(default='')
    prd_Explainer_view_image = db.StringField(default='')
    prd_Commercial_View_Image_2 = db.StringField(default='')
    prd_Product_Description = db.StringField(default='')
    prd_Feature_1 = db.StringField(default='')
    prd_Feature_2 = db.StringField(default='')
    prd_Feature_3 = db.StringField(default='')
    prd_Feature_4 = db.StringField(default='')
    prd_Feature_5 = db.StringField(default='')
    prd_Search_Terms = db.StringField(default='')
    prd_Search_Terms_Keywords_1 = db.StringField(default='')
    prd_Search_Terms_Keywords_2 = db.StringField(default='')
    prd_Search_Terms_Keywords_3 = db.StringField(default='')
    prd_Search_Terms_Keywords_4 = db.StringField(default='')
    prd_Search_Terms_Keywords_5 = db.StringField(default='')
    prd_Main_Image_URL = db.StringField(default='')
    prd_Package_Length = db.FloatField(default='')
    prd_Package_Breadth = db.FloatField(default='')
    prd_Package_Height = db.FloatField(default='')
    prd_Package_Weight = db.FloatField(default='')
    prd_Big_Carton_Dimension = db.StringField(default='')
    prd_Big_Carton_Weight = db.StringField(default='')
    prd_Master_Pack_Details = db.StringField(default='')
    prd_Barcode_UPC_Model_Number = db.StringField(default='')
    prd_Entry_Date = db.DateTimeField()
    prd_Category = db.StringField(default='')
    Parent_SKU = db.StringField(default='')

    # user_id = db.StringField(default='')


# Creating Collection Object for Checkout Master

class och_checkout_master(db.Document):
    chkot_last_change = db.DateTimeField()
    chkot_First_Name = db.StringField(default='')
    chkot_Last_Name = db.StringField(default='')
    chkot_email = db.StringField(default='')
    chkot_Phone = db.StringField(default='')
    chkot_Address = db.StringField(default='')
    chkot_City = db.StringField(default='')
    chkot_Pincode = db.StringField(default='')
    chkot_State = db.StringField(default='')
    chkot_Order_Note = db.StringField(default='')
    # chkot_token = db.StringField(default='')
    chkot_quantity = db.StringField(default='')
    # chkot_billing_address = db.StringField(default='')
    # chkot_shipping_address = db.StringField(default='')
    chkot_shipping_method = db.StringField(default='')
    # chkot_note = db.StringField(default='')
    chkot_currency = db.StringField(default='')
    chkot_discount_amount = db.StringField(default='')
    chkot_discount_name = db.StringField(default='')
    chkot_translated_discount_name = db.StringField(default='')
    chkot_voucher_code = db.StringField(default='')
    chkot_gift_cards = db.StringField(default='')
    user_id = db.StringField(default='')



   


# Creating Collection Object for Checkout Master

class och_checkout_master_(db.Document):
    chkot_last_change = db.DateTimeField()
    chkot_user = db.StringField(default='')
    chkot_email = db.StringField(default='')
    # chkot_token = db.StringField(default='')
    chkot_quantity = db.StringField(default='')
    chkot_billing_address = db.StringField(default='')
    chkot_shipping_address = db.StringField(default='')
    chkot_shipping_method = db.StringField(default='')
    chkot_note = db.StringField(default='')
    chkot_currency = db.StringField(default='')
    chkot_discount_amount = db.StringField(default='')
    chkot_discount_name = db.StringField(default='')
    chkot_translated_discount_name = db.StringField(default='')
    chkot_voucher_code = db.StringField(default='')
    chkot_gift_cards = db.StringField(default='')

    
    user_id = db.StringField(default='')
    # user_name = db.StringField(default='')
    # company = db.StringField(default='')
    # company_id = db.StringField(default='')
    # department_name = db.StringField(default='')
    # department_id = db.StringField(default='')
    # branch_id = db.StringField(default='')
    # branch_name = db.StringField(default='')

    

# # Creating Collection Object for Checkout Transaction   
# class och_checkout_transaction(db.Document):
#     dms_Claims_Id = db.StringField(default='')
#     dms_Response = db.StringField(default='')
#     dms_response_Date = db.DateTimeField(default='')
#     dms_Status = db.StringField(default='')

#     dms_dealer_id = db.StringField(default='')
#     dms_dealer_name = db.StringField(default='')
#     designation = db.StringField(default='')
#     comments = db.StringField(default='')
#     file_type = db.StringField(default='')
#     file_url = db.StringField(default='')

#     user_id = db.StringField(default='')
#     user_name = db.StringField(default='')
#     company = db.StringField(default='')
#     company_id = db.StringField(default='')
#     department_name = db.StringField(default='')
#     department_id = db.StringField(default='')
#     branch_id = db.StringField(default='')
#     branch_name = db.StringField(default='')

    
class och_add_to_cart_master(db.Document):
    prd_SKU_ID = db.StringField(default='')
    prd_Product_Title = db.StringField(default='')
    prd_MRP = db.FloatField(default='')
    prd_Standard_Price = db.FloatField(default='')
    prd_Qty = db.IntField(default='')
    prd_Main_View_Image = db.StringField(default='')
    cart_Entry_Date = db.DateTimeField()
    # prd_Front_View_Image = db.StringField(default='')
    # prd_Side_View_Image = db.StringField(default='')
    # prd_Commercial_View_Image_1 = db.StringField(default='')
    # prd_Explainer_view_image = db.StringField(default='')
    # prd_Commercial_View_Image_2 = db.StringField(default='')

    user_id = db.StringField(default='')
    # user_name = db.StringField(default='')
    # company = db.StringField(default='')
    # company_id = db.StringField(default='')
    # department_name = db.StringField(default='')
    # department_id = db.StringField(default='')
    # branch_id = db.StringField(default='')
    # branch_name = db.StringField(default='')

class och_cart_transaction(db.Document):
    prd_SKU_ID = db.StringField(default='')
    prd_Product_Title = db.StringField(default='')
    prd_MRP = db.StringField(default='')
    prd_Standard_Price = db.StringField(default='')
    prd_Qty = db.IntField(default='')
    cart_Total = db.FloatField(default='')
    cart_Sub_Total = db.FloatField(default='')
    prd_Main_View_Image = db.StringField(default='')
    cart_transaction_Entry_Date = db.DateTimeField()
    # prd_Front_View_Image = db.StringField(default='')
    # prd_Side_View_Image = db.StringField(default='')
    # prd_Commercial_View_Image_1 = db.StringField(default='')
    # prd_Explainer_view_image = db.StringField(default='')
    # prd_Commercial_View_Image_2 = db.StringField(default='')

    user_id = db.StringField(default='')
    



class och_page_master(db.Document):
    page_id = db.StringField(default='')
    page_name = db.StringField(default='')
    page_url = db.StringField(default='')
    company_id = db.StringField(default='')
    page_type = db.StringField(default='')


class och_page_component_master_old(db.Document):
    page_component_id = db.StringField(default='')
    page_id = db.StringField(default='')
    component_name = db.StringField(default='')
    sequence = db.StringField(default='')
    element = db.StringField(default='')
    company_id = db.StringField(default='')
    link_name = db.StringField(default='')
    link_url = db.StringField(default='')
    font_color = db.StringField(default='')
    hover_color = db.StringField(default='')
    bg_color = db.StringField(default='')
    select_color = db.StringField(default='')
    dropdown_name = db.StringField(default='')
    dropdown_data = db.StringField(default='')
    collection_name = db.StringField(default='')	
    image = db.StringField(default='')	
    button_link = db.StringField(default='')	
    description = db.StringField(default='')
    partial_file_path = db.StringField(default='')


class page_component_element_master(db.Document):
    pgem_id = db.StringField(default='')
    Component_Category = db.StringField(default='')
    Component_Name = db.StringField(default='')
    Sequence = db.StringField(default='')
    element = db.StringField(default='')
    Link_Name = db.StringField(default='')
    Link_Url = db.StringField(default='')
    Font_Color = db.StringField(default='')
    Hover_Color = db.StringField(default='')
    bg_Color = db.StringField(default='')
    Select_Color = db.StringField(default='')
    Dropdown_Name = db.StringField(default='')
    Dropdown_Data = db.StringField(default='')
    Collection_Name = db.StringField(default='')	
    Image = db.StringField(default='')	
    Button_Link = db.StringField(default='')	
    Description = db.StringField(default='')
    company_id = db.StringField(default='')


##############webfront###################################
class webfront_page_component_master(db.Document):
    Page_id = db.StringField(default='')
    Page_Name = db.StringField(default='')
    Page_URL = db.StringField(default='')
    Company_Id = db.StringField(default='')
    FrameArray = db.StringField(default='')
    Component_Id = db.StringField(default='')
    Component_Name = db.StringField(default='')
    Component_Category = db.StringField(default='')
    Sequence = db.StringField(default='')
    Element_Id = db.StringField(default='')
    Element_Name = db.ListField()
    partial_file_path = db.StringField(default='')
    component_heading = db.StringField(default='')
    element_heading = db.ListField()
    sub_heading = db.ListField()
    description = db.ListField()
    prd_collection_name = db.ListField()
    link_name = db.StringField(default='')
    # link_name = db.ListField()
    link_url = db.ListField()
    button_name = db.ListField()
    button_link = db.ListField()
    image_url = db.ListField()
    video_url = db.ListField()
    dropdown_name = db.ListField()
    dropdown_data = db.ListField()
    dropdown_url = db.ListField()
    font_color = db.StringField(default='')
    hover_color = db.StringField(default='')
    bg_color = db.StringField(default='')
    hover_bg_color = db.StringField(default='')
    select_color = db.StringField(default='')
    padding = db.StringField(default='')
    margin = db.StringField(default='')
    height = db.StringField(default='')
    width = db.StringField(default='')
    border_color = db.StringField(default='')
    border_hover_color = db.StringField(default='')
##############################################################################







# Page_Id = db.StringField(default='')
#     Page_Name = db.StringField(default='')
#     Page_URL = db.StringField(default='')
#     Company_Id = db.StringField(default='')
#     FrameArray = db.StringField(default='')
#     Component_Id = db.StringField(default='')
#     Component_Name = db.StringField(default='')
#     Component_Category = db.StringField(default='')
#     Sequence = db.StringField(default='')
#     Element_Id = db.StringField(default='')
#     Element_Name = db.StringField(default='')
#     partial_file_path = db.StringField(default='')
#     component_heading = db.StringField(default='')
#     description = db.StringField(default='')
#     prd_collection_name = db.StringField(default='')
#     link_name = db.StringField(default='')
#     link_url = db.StringField(default='')
#     button_name = db.StringField(default='')
#     button_link = db.StringField(default='')
#     image_url = db.StringField(default='')
#     video_url = db.StringField(default='')
#     dropdown_name = db.StringField(default='')
#     dropdown_data = db.StringField(default='')
#     dropdown_url = db.StringField(default='')
#     font_color = db.StringField(default='')
#     hover_color = db.StringField(default='')
#     bg_color = db.StringField(default='')
#     select_color = db.StringField(default='')
#     padding = db.StringField(default='')
#     height = db.StringField(default='')
#     width = db.StringField(default='')
#     border = db.StringField(default='')


###############################################################################################################
#   TVL Section
###############################################################################################################

# Creating product master for TVL
class tvl_product_master(db.Document):
    prd_Product_category = db.StringField(default='')
    prd_Product_Title = db.StringField(default='')
    prd_Collection_Name = db.StringField(default='')
    prd_Brand = db.StringField(default='')
    prd_SKU_ID = db.StringField(default='')
    prd_Color = db.StringField(default='')
    prd_Capacity_Units = db.StringField(default='')
    prd_Capacity_Value = db.IntField(default='')
    prd_Included_Components = db.StringField(default='')
    prd_Standard_Price = db.FloatField(default='')
    prd_MRP = db.FloatField(default='')
    prd_Manufacturer = db.StringField(default='')
    prd_Product_Length = db.FloatField(default='')
    prd_Product_Breadth = db.FloatField(default='')
    prd_Product_Height = db.FloatField(default='')
    prd_Product_Weight = db.FloatField(default='')
    prd_HSN_Code = db.StringField(default='')
    prd_GST_applicable = db.StringField(default='')
    prd_Qty = db.IntField(default='')
    prd_Main_View_Image = db.StringField(default='')
    prd_Front_View_Image = db.StringField(default='')
    prd_Side_View_Image = db.StringField(default='')
    prd_Commercial_View_Image_1 = db.StringField(default='')
    prd_Explainer_view_image = db.StringField(default='')
    prd_Commercial_View_Image_2 = db.StringField(default='')
    prd_Product_Description = db.StringField(default='')
    prd_Feature_1 = db.StringField(default='')
    prd_Feature_2 = db.StringField(default='')
    prd_Feature_3 = db.StringField(default='')
    prd_Feature_4 = db.StringField(default='')
    prd_Feature_5 = db.StringField(default='')
    prd_Search_Terms = db.StringField(default='')
    prd_Search_Terms_Keywords_1 = db.StringField(default='')
    prd_Search_Terms_Keywords_2 = db.StringField(default='')
    prd_Search_Terms_Keywords_3 = db.StringField(default='')
    prd_Search_Terms_Keywords_4 = db.StringField(default='')
    prd_Search_Terms_Keywords_5 = db.StringField(default='')
    prd_Main_Image_URL = db.StringField(default='')
    prd_Package_Length = db.FloatField(default='')
    prd_Package_Breadth = db.FloatField(default='')
    prd_Package_Height = db.FloatField(default='')
    prd_Package_Weight = db.FloatField(default='')
    prd_Big_Carton_Dimension = db.StringField(default='')
    prd_Big_Carton_Weight = db.StringField(default='')
    prd_Master_Pack_Details = db.StringField(default='')
    prd_Barcode_UPC_Model_Number = db.StringField(default='')
    prd_Entry_Date = db.DateTimeField()
    prd_Category = db.StringField(default='')
    Parent_SKU = db.StringField(default='')


# add_to_cart Cart master for TVL
class tvl_add_to_cart_master(db.Document):
    prd_SKU_ID = db.StringField(default='')
    prd_Product_Title = db.StringField(default='')
    prd_MRP = db.FloatField(default='')
    prd_Standard_Price = db.FloatField(default='')
    prd_Qty = db.IntField(default='')
    prd_Main_View_Image = db.StringField(default='')
    prd_total_amount = db.FloatField(default=0.0)
    cart_Entry_Date = db.DateTimeField()
    user_id = db.StringField(default='')
    visit_id = db.StringField(default='')

# checkout_to_Cart master for TVL
class tvl_checkout_to_cart_master(db.Document):

    checkout_to_cart_id = db.StringField(default='')
    checkout_to_cart_row_data = db.StringField(default='')
    sub_total = db.FloatField(default='')
    cart_Entry_Date = db.DateTimeField()
    user_id = db.StringField(default='')
    visit_id = db.StringField(default='')

# Creating Collection Object for TVL Address Master
class tvl_address_master(db.Document):
    # chkot_last_change = db.DateTimeField()
    addr_First_Name = db.StringField(default='')
    addr_Last_Name = db.StringField(default='')
    addr_email = db.StringField(default='')
    addr_Phone = db.StringField(default='')
    addr_Address = db.StringField(default='')
    addr_City = db.StringField(default='')
    addr_Pincode = db.StringField(default='')
    addr_State = db.StringField(default='')
    addr_Order_Note = db.StringField(default='')
    user_id = db.StringField(default='')
    # chkot_token = db.StringField(default='')
    # chkot_quantity = db.StringField(default='')

# Creating Collection Object for TVL Checkout Master
class tvl_checkout_master(db.Document):
    chkot_last_change = db.DateTimeField()
    chkot_First_Name = db.StringField(default='')
    chkot_Last_Name = db.StringField(default='')
    chkot_email = db.StringField(default='')
    chkot_Phone = db.StringField(default='')
    chkot_Address = db.StringField(default='')
    chkot_City = db.StringField(default='')
    chkot_Pincode = db.StringField(default='')
    chkot_State = db.StringField(default='')
    chkot_Order_Note = db.StringField(default='')
    # chkot_token = db.StringField(default='')
    chkot_quantity = db.StringField(default='')
    # chkot_billing_address = db.StringField(default='')
    # chkot_shipping_address = db.StringField(default='')
    # chkot_shipping_method = db.StringField(default='')
    # chkot_note = db.StringField(default='')
    # chkot_currency = db.StringField(default='')
    # chkot_discount_amount = db.StringField(default='')
    # chkot_discount_name = db.StringField(default='')
    # chkot_translated_discount_name = db.StringField(default='')
    # chkot_voucher_code = db.StringField(default='')
    # chkot_gift_cards = db.StringField(default='')
    visit_id = db.StringField(default='')
    user_id = db.StringField(default='')

# Creating Collection Object for TVL Payment Master
class tvl_payment_master(db.Document):
    paymeny_id = db.StringField(default='')
    paymeny_entity = db.StringField(default='')
    paymeny_amount = db.StringField(default='')
    paymeny_currency = db.StringField(default='')
    paymeny_status = db.StringField(default='')
    paymeny_order_id = db.StringField(default='')
    paymeny_invoice_id = db.StringField(default='')
    paymeny_international = db.StringField(default='')
    paymeny_method = db.StringField(default='')
    paymeny_amount_refunded = db.StringField(default='')
    paymeny_refund_status = db.StringField(default='')
    paymeny_captured = db.StringField(default='')
    paymeny_description = db.StringField(default='')
    paymeny_card_id = db.StringField(default='')
    paymeny_bank = db.StringField(default='')
    paymeny_wallet = db.StringField(default='')
    paymeny_vpa = db.StringField(default='')
    paymeny_email = db.StringField(default='')
    paymeny_contact = db.StringField(default='')
    paymeny_notes = db.StringField(default='')
    paymeny_fee = db.StringField(default='')
    paymeny_tax = db.StringField(default='')
    paymeny_error_code = db.StringField(default='')
    paymeny_error_description = db.StringField(default='')
    paymeny_created_at = db.StringField(default='')

    user_id = db.StringField(default='')


# Creating Collection Object for Order Master

class tvl_order_master(db.Document):
    ord_company_id = db.StringField(default='')
    ord_company_type = db.StringField(default='')
    ord_company_name = db.StringField(default='')
    ord_Order_id = db.StringField(default='')
    ord_Order_date = db.DateTimeField()
    ord_Product_id = db.StringField(default='')
    prd_Product_Title = db.StringField(default='')
    ord_Quantity = db.StringField(default='')
    ord_Order_del_addr = db.StringField(default='')
    ord_Order_bill_addr = db.StringField(default='')
    ord_delivery_date = db.DateTimeField()
    ord_Order_sts = db.StringField(default='')
    ord_Order_Compete_dt = db.DateTimeField()
    ord_user_feedback = db.StringField(default='')
    paymeny_method = db.StringField(default='')
    paymeny_id = db.StringField(default='')

    ord_Prd_Desc = db.StringField(default='')
    ord_Gross_Sales = db.StringField(default='')
    ord_Net_Sales = db.StringField(default='')
    ord_price_per_piece = db.StringField(default='')
    ord_Country_Code = db.StringField(default='')

    user_id = db.StringField(default='')




########################################################################################################################
#   NKSHI Section
########################################################################################################################

# Creating product master for NKSHI
class nkshi_product_master(db.Document):
    prd_Product_category = db.StringField(default='')
    prd_Product_Title = db.StringField(default='')
    prd_Collection_Name = db.StringField(default='')
    prd_Brand = db.StringField(default='')
    prd_SKU_ID = db.StringField(default='')
    prd_Color = db.StringField(default='')
    prd_Capacity_Units = db.StringField(default='')
    prd_Capacity_Value = db.IntField(default='')
    prd_Included_Components = db.StringField(default='')
    prd_Standard_Price = db.FloatField(default='')
    prd_MRP = db.FloatField(default='')
    prd_Manufacturer = db.StringField(default='')
    prd_Product_Length = db.FloatField(default='')
    prd_Product_Breadth = db.FloatField(default='')
    prd_Product_Height = db.FloatField(default='')
    prd_Product_Weight = db.FloatField(default='')
    prd_HSN_Code = db.StringField(default='')
    prd_GST_applicable = db.StringField(default='')
    prd_Qty = db.IntField(default='')
    prd_Main_View_Image = db.StringField(default='')
    prd_Front_View_Image = db.StringField(default='')
    prd_Side_View_Image = db.StringField(default='')
    prd_Commercial_View_Image_1 = db.StringField(default='')
    prd_Explainer_view_image = db.StringField(default='')
    prd_Commercial_View_Image_2 = db.StringField(default='')
    prd_Product_Description = db.StringField(default='')
    prd_Feature_1 = db.StringField(default='')
    prd_Feature_2 = db.StringField(default='')
    prd_Feature_3 = db.StringField(default='')
    prd_Feature_4 = db.StringField(default='')
    prd_Feature_5 = db.StringField(default='')
    prd_Search_Terms = db.StringField(default='')
    prd_Search_Terms_Keywords_1 = db.StringField(default='')
    prd_Search_Terms_Keywords_2 = db.StringField(default='')
    prd_Search_Terms_Keywords_3 = db.StringField(default='')
    prd_Search_Terms_Keywords_4 = db.StringField(default='')
    prd_Search_Terms_Keywords_5 = db.StringField(default='')
    prd_Main_Image_URL = db.StringField(default='')
    prd_Package_Length = db.FloatField(default='')
    prd_Package_Breadth = db.FloatField(default='')
    prd_Package_Height = db.FloatField(default='')
    prd_Package_Weight = db.FloatField(default='')
    prd_Big_Carton_Dimension = db.StringField(default='')
    prd_Big_Carton_Weight = db.StringField(default='')
    prd_Master_Pack_Details = db.StringField(default='')
    prd_Barcode_UPC_Model_Number = db.StringField(default='')
    prd_Entry_Date = db.DateTimeField()
    prd_Category = db.StringField(default='')
    Parent_SKU = db.StringField(default='')


# Creating Collection Object of Cart master for nkshi
class nkshi_add_to_cart_master(db.Document):
    prd_SKU_ID = db.StringField(default='')
    prd_Product_Title = db.StringField(default='')
    prd_MRP = db.FloatField(default='')
    prd_Standard_Price = db.FloatField(default='')
    prd_Qty = db.IntField(default='')
    prd_Main_View_Image = db.StringField(default='')
    cart_Entry_Date = db.DateTimeField()
    user_id = db.StringField(default='')


# Creating Collection Object for NKSHI Checkout Master
class nkshi_checkout_master(db.Document):
    chkot_last_change = db.DateTimeField()
    chkot_First_Name = db.StringField(default='')
    chkot_Last_Name = db.StringField(default='')
    chkot_email = db.StringField(default='')
    chkot_Phone = db.StringField(default='')
    chkot_Address = db.StringField(default='')
    chkot_City = db.StringField(default='')
    chkot_Pincode = db.StringField(default='')
    chkot_State = db.StringField(default='')
    chkot_Order_Note = db.StringField(default='')
    # chkot_token = db.StringField(default='')
    chkot_quantity = db.StringField(default='')
    # chkot_billing_address = db.StringField(default='')
    # chkot_shipping_address = db.StringField(default='')
    chkot_shipping_method = db.StringField(default='')
    # chkot_note = db.StringField(default='')
    chkot_currency = db.StringField(default='')
    chkot_discount_amount = db.StringField(default='')
    chkot_discount_name = db.StringField(default='')
    chkot_translated_discount_name = db.StringField(default='')
    chkot_voucher_code = db.StringField(default='')
    chkot_gift_cards = db.StringField(default='')






########################################################################################################################
#   Atlasware Section
########################################################################################################################

# Creating product master for Atlasware
class atlasware_product_master(db.Document):
    prd_Product_category = db.StringField(default='')
    prd_Product_Title = db.StringField(default='')
    prd_Collection_Name = db.StringField(default='')
    prd_Brand = db.StringField(default='')
    prd_SKU_ID = db.StringField(default='')
    prd_Color = db.StringField(default='')
    prd_Capacity_Units = db.StringField(default='')
    prd_Capacity_Value = db.IntField(default='')
    prd_Included_Components = db.StringField(default='')
    prd_Standard_Price = db.FloatField(default='')
    prd_MRP = db.FloatField(default='')
    prd_Manufacturer = db.StringField(default='')
    prd_Product_Length = db.FloatField(default='')
    prd_Product_Breadth = db.FloatField(default='')
    prd_Product_Height = db.FloatField(default='')
    prd_Product_Weight = db.FloatField(default='')
    prd_HSN_Code = db.StringField(default='')
    prd_GST_applicable = db.StringField(default='')
    prd_Qty = db.IntField(default='')
    prd_Main_View_Image = db.StringField(default='')
    prd_Front_View_Image = db.StringField(default='')
    prd_Side_View_Image = db.StringField(default='')
    prd_Commercial_View_Image_1 = db.StringField(default='')
    prd_Explainer_view_image = db.StringField(default='')
    prd_Commercial_View_Image_2 = db.StringField(default='')
    prd_Product_Description = db.StringField(default='')
    prd_Feature_1 = db.StringField(default='')
    prd_Feature_2 = db.StringField(default='')
    prd_Feature_3 = db.StringField(default='')
    prd_Feature_4 = db.StringField(default='')
    prd_Feature_5 = db.StringField(default='')
    prd_Search_Terms = db.StringField(default='')
    prd_Search_Terms_Keywords_1 = db.StringField(default='')
    prd_Search_Terms_Keywords_2 = db.StringField(default='')
    prd_Search_Terms_Keywords_3 = db.StringField(default='')
    prd_Search_Terms_Keywords_4 = db.StringField(default='')
    prd_Search_Terms_Keywords_5 = db.StringField(default='')
    prd_Main_Image_URL = db.StringField(default='')
    prd_Package_Length = db.FloatField(default='')
    prd_Package_Breadth = db.FloatField(default='')
    prd_Package_Height = db.FloatField(default='')
    prd_Package_Weight = db.FloatField(default='')
    prd_Big_Carton_Dimension = db.StringField(default='')
    prd_Big_Carton_Weight = db.StringField(default='')
    prd_Master_Pack_Details = db.StringField(default='')
    prd_Barcode_UPC_Model_Number = db.StringField(default='')
    prd_Entry_Date = db.DateTimeField()
    prd_Category = db.StringField(default='')
    Parent_SKU = db.StringField(default='')


# Creating Collection Object of Cart master for Atlasware
class atlasware_add_to_cart_master(db.Document):
    prd_SKU_ID = db.StringField(default='')
    prd_Product_Title = db.StringField(default='')
    prd_MRP = db.FloatField(default='')
    prd_Standard_Price = db.FloatField(default='')
    prd_Qty = db.IntField(default='')
    prd_Main_View_Image = db.StringField(default='')
    cart_Entry_Date = db.DateTimeField()
    user_id = db.StringField(default='')


# Creating Collection Object for Atlasware Checkout Master
class atlasware_checkout_master(db.Document):
    chkot_last_change = db.DateTimeField()
    chkot_First_Name = db.StringField(default='')
    chkot_Last_Name = db.StringField(default='')
    chkot_email = db.StringField(default='')
    chkot_Phone = db.StringField(default='')
    chkot_Address = db.StringField(default='')
    chkot_City = db.StringField(default='')
    chkot_Pincode = db.StringField(default='')
    chkot_State = db.StringField(default='')
    chkot_Order_Note = db.StringField(default='')
    # chkot_token = db.StringField(default='')
    chkot_quantity = db.StringField(default='')
    # chkot_billing_address = db.StringField(default='')
    # chkot_shipping_address = db.StringField(default='')
    chkot_shipping_method = db.StringField(default='')
    # chkot_note = db.StringField(default='')
    chkot_currency = db.StringField(default='')
    chkot_discount_amount = db.StringField(default='')
    chkot_discount_name = db.StringField(default='')
    chkot_translated_discount_name = db.StringField(default='')
    chkot_voucher_code = db.StringField(default='')
    chkot_gift_cards = db.StringField(default='')
