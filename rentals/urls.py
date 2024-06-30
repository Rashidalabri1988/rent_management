from django.urls import path, include
from . import views
urlpatterns = [

    path('login/', views.login_view, name='login'),
    
    path('', views.main_menu, name='main_menu'),
    
    path('tenants/', views.tenants_list, name='tenants_list'),
    path('tenants/add/', views.add_tenant, name='add_tenant'),
    path('tenants/edit/<int:tenant_id>/', views.edit_tenant, name='edit_tenant'),
    
    path('rental_places/', views.rental_places_list, name='rental_places_list'),
    path('rental_places/add/', views.add_rental_places, name='add_rental_places'),
    path('rental_places/edit/<int:places_id>/', views.edit_rental_place, name='edit_rental_place'),
    
    path('rental_contracts/', views.rental_contract_list, name='rental_contract_list'),
    path('rental_contracts/add/', views.add_rental_contract, name='add_rental_contract'),
    path('rental_contracts/cancel/<int:contract_id>/', views.cancel_rental_contract, name='cancel_rental_contract'),
    path('rental_contracts/print/<int:contract_id>/',views.print_rental_contract, name='print_rental_contract'),
    
    path('statistics/', views.statistics, name='statistics'),
]
