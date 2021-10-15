from django.urls import path
from . import views

urlpatterns = [
    path('logbook/<user_id>/', views.logbook, name='logbook'),
    path('add/', views.add_bluepoint, name='add_bluepoint'),
]
