'''
from django.urls import path
from .views import home

urlpatterns = [
    path('',home,name='home'),
]
'''

from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('edit/<int:id>/', views.edit_product, name="edit"),
    path('delete/<int:id>/', views.delete_product, name="delete"),
]
