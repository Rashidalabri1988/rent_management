from django import forms
from .models import Tenant, RentalPlace, RentalContract, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    pass

class TenantForm(forms.ModelForm):
    pass
    
class RentalPlaceForm(forms.ModelForm):
    pass
    
class RentalContractForm(forms.ModelForm):
    pass
    
class CustomUserChangeForm(UserChangeForm):
    pass