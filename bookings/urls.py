from django.urls import path
from . import views

urlpatterns = [
     path('', views.bookings, name='bookings'),
     path('booking_success/<booking_number>/', views.booking_success,
          name='booking_success'),
     path('booking_management/', views.booking_management,
          name='booking_management'),
]
