# from app.views import Sponser_id
from django import forms
from django.db import models
from .models import Support_User_Sponser_detail, support_bank_detail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _


#Registration Form
class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':"form-control"}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':"form-control"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        label = {'email':'Email'}
        widget = {'username':forms.TextInput(attrs={'class':'form-control'})}

#Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs=
        {'autocomplete':'current-password', 'class':'form-control'}))

#Change Password Form
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=('Old Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))

    new_password1 = forms.CharField(label=('New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.
        password_validators_help_text_html())

    new_password2 = forms.CharField(label=('Confirm New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}))


# Reset Password Form
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=('Email'),max_length=255, widget=forms.EmailInput
        (attrs={'autocomplete':'email','class':'form-control'}))



#Confirm Reset Password Form
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=('New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.
        password_validators_help_text_html())
    new_password2 = forms.CharField(label=('Confirm New Password'),strip=False, widget=forms.PasswordInput
        (attrs={'autocomplete':'new-password','class':'form-control'}))

class Sponser_id_form(forms.ModelForm):
    Sponser_id = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
    # city = forms.Select(attrs={'class':"form-control"})
    
    class Meta:
        model = Support_User_Sponser_detail
        fields =  ['name']

class bank_detail(forms.Form):
    Account_Holder_Name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"form-control"}))
    Account_Number = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':"form-control"}))
    Confirm_Account_Number = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class':"form-control"}))
    IFSC_Code = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"form-control"}))

    class Meta:
        model = support_bank_detail
        fields = ['Account_Holder_Name', 'Account_Number', 'Confirm_Account_Number', 'IFSC_Code']
