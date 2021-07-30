from django.contrib import admin
from .models import (
    Support_User_Sponser_detail
)

# Register your models here.

@admin.register(Support_User_Sponser_detail)
class Support_User_Sponser_detail_Admin(admin.ModelAdmin):
    list_display = ['user', 'name', 'city', 'mobile_no', 'sponser_id',  'updated', 'created']