from django.contrib import admin
from .models import Tenant, RentalPlace, RentalContract, CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(Tenant)
admin.site.register(RentalPlace)
admin.site.register(RentalContract)
admin.site.register(CustomUser)