from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('add/', views.add_service, name='add_service'),
    path('edit/<int:service_id>/', views.edit_service, name='edit_service'),
    path('delete/<int:service_id>/', views.delete_service,
         name='delete_service'),
    path('<slug:slug>/', views.service_detail, name='service_detail'),
]
