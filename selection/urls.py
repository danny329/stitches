from django.urls import path
from . import views

urlpatterns = [
   
    path('selectionpage/', views.selectionpage, name='selectionpage')

]