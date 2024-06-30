from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Tenant, RentalPlace, RentalContract
from .forms import TenantForm, RentalPlaceForm, RentalContractForm
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('main_menu')
        else:
            error="اسم المستخدم أو كلمة المرور غير صحيحة"
            return render(request, 'login.html',{'error':error})
    return render(request, 'login.html')
    
@login_required
def main_menu(request):
    return render(request, 'main_menu.html')
        
@login_required
def tenants_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants_list.html', {'tenants':tenants})
    
@login_required
def add_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenants_list')
    else:
        form=TenantForm()
    return render(request, 'add_tenant.html',{'form':form})

@login_required
def edit_tenant(request, tenant_id):
    tenant = get_object_or_404(Tenant, id=tenant_id)
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('tenants_list')
    else:
        form = TenantForm(instance=tenant)
    return render(request, 'edit_tenant.html',{'form':form})
    
@login_required
def rental_places_list(request):
    places = RentalPlace.objects.all()
    return render(request, 'rental_places_list.html', {'places':places})
    
@login_required
def add_rental_places(request):
    if request.method == 'POST':
        form = RentalPlace(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rental_places_list')
    else:
        form=RentalPlace()
    return render(request, 'add_rental_place.html',{'form':form})

@login_required
def edit_rental_place(request, place_id):
    place = get_object_or_404(RentalPlace, id=place_id)
    if request.method == 'POST':
        form = RentalPlace(request.POST, instance=place)
        if form.is_valid():
            form.save()
            return redirect('rental_places_list')
    else:
        form = RentalPlace(instance=place)
    return render(request, 'edit_rental_place.html',{'form':form})
    
@login_required
def rental_contract_list(request):
    contracts = RentalContract.objects.all()
    return render(request, 'rental_contracts_list.html', {'contracts':contracts})
    
@login_required
def add_rental_contract(request):
    if request.method == 'POST':
        form = RentalContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rental_contracts_list')
    else:
        form=RentalContractForm()
    return render(request, 'add_rental_contract.html',{'form':form})

@login_required
def cancel_rental_contract(request, contract_id):
    contract = get_object_or_404(RentalContract, id=contract_id)
    contract.is_cancelled = True
    contract.save()
    return redirect(request, 'rental_contracts_list.html',{'form':form})

@login_required
def print_rental_contract(request, contract_id):
    contract = get_object_or_404(RentalContract, id=contract_id)
    return render(request, 'print_rental_contract.html',{'contract':contract})
    
@login_required
def statistics(request):
    total_tenants = Tenant.objects.count()
    active_contracts = RentalContract.objects.filter(is_cancelled=False).count()
    cancelled_contracts = RentalContract.objects.filter(is_cancelled=True).count()
    return render(request, 'statistics.html', {'total_tenants':total_tenants, 'active_contracts':active_contracts, 'cancelled_contracts':cancelled_contracts})