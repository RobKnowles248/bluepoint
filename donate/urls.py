from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('pay/', views.pay, name='pay'),
]
