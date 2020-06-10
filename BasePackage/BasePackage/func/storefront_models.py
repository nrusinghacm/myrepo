# pylint: disable=no-member, missing-docstring, unused-variable, invalid-name


"""

This Program Is For SKF Means All Models User In SKF Those Are Defined Here

"""

# Import All Neccessary Modules
# from mongoengine import connect, disconnect


# Import Our Modules

from APP.UserManagement.models import db


    



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

class och_page_component_master(db.Document):
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
    height = db.StringField(default='')
    width = db.StringField(default='')
    border = db.StringField(default='')
    margin = db.StringField(default='')
    border_color = db.StringField(default='')
    border_hover_color = db.StringField(default='')

