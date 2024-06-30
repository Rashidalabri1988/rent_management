from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم")
    address = models.CharField(max_length=200, verbose_name='العنوان')
    phone_number = models.CharField(max_length=15, verbose_name="رقم الهاتف")
    email = models.EmailField(verbose_name="البريد الإلكتروني", null=True, blank=True)
    
    def __str__(self):
        return self.name
        
class RentalPlace(models.Model):
    address = models.CharField(max_length=200, verbose_name='العنوان')
    description = models.TextField(verbose_name='الوصف',null=True, blank=True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='مبلغ الإيجار')
    
    def __str__(self):
        return self.address
        
class RentalContract(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="contracts", verbose_name="المستأجر")
    rental_place = models.ForeignKey(RentalPlace, on_delete=models.CASCADE, verbose_name="مكان الاجار")
    start_date = models.DateField(verbose_name="تالايخ البدء")
    end_date = models.DateField(verbose_name="تاريخ الانتهاء")
    is_cancelled = models.BooleanField(default=False, verbose_name="ملغى")
    
    def __str__(self):
        return f"عقد إيجار بين {self.tenant.name} و {self.rental_place.address}"
        
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, verbose_name="رقم الهاتف", null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name="العنوان", null=True, blank=True)
    
    def __str__(self):
        return self.username
        
class Statistics(models.Model):
    total_tenants = models.IntegerField(verbose_name="إجمالي المستأجرين")
    active_contracts = models.IntegerField(verbose_name="العقود الفعالة")
    cancelled_contracts = models.IntegerField(verbose_name="العقود الملغاة")
    
    def __str__(self):
        return f"إحصائيات {self.pk}"