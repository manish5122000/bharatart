from django.contrib import admin
from .models import (
    Support_User_Sponser_detail,
    support_bank_detail
)

# Register your models here.

@admin.register(Support_User_Sponser_detail)
class Support_User_Sponser_detail_Admin(admin.ModelAdmin):
    list_display = ['user', 'name', 'city', 'mobile_no', 'sponser_id',  'updated', 'created']

@admin.register(support_bank_detail)
class support_bank_details_Admin(admin.ModelAdmin):
    list_display = ['Account_Holder_Name', 'Account_Number', 'Confirm_Account_Number', 'IFSC_Code']