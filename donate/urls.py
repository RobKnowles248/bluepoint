from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('pay/<donation_number>', views.pay, name='pay'),
    path('payment_success/<donation_number>', views.payment_success, name='payment_success'),
]
