from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('<slug:slug>/', views.service_detail, name='service_detail'),
    path('add/', views.add_service, name='add_service'),
]
