from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<slug:part>/', views.checkout, name='checkout'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),


]