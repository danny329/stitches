from django.urls import path
from . import views

urlpatterns = [
   
    path('selectionpage/', views.selectionpage, name='selectionpage'),
    path('select/', views.select, name='select'),
    path('select/<slug:part>/', views.select, name='select'),
    path('addtocart/', views.addtocart, name='addtocart'),





]