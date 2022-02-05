from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from donations import views
# from donations.views import Paypal_donation

# app_name = 'donations'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),
    path('donation/', views.donation, name="donation"),
    # path('paypal/', include('paypal.standard.ipn.urls')),
]