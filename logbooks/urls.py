from django.urls import path
from . import views

urlpatterns = [
    path('logbook/<username>/', views.logbook, name='logbook'),
    path('add/', views.add_bluepoint, name='add_bluepoint'),
    path('search/', views.search, name='search'),
    path('edit/<int:bluepoint_id>/', views.edit_bluepoint, name='edit_bluepoint'),
    path('delete/<int:bluepoint_id>/', views.delete_bluepoint, name='delete_bluepoint'),
]
