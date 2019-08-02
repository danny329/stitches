from django.urls import path
from . import views

urlpatterns = [
    path("signupform", views.signupform, name='signupform'),
    path("login_page", views.login_page, name='login_page'),
    path("logout", views.logout, name='logout'),



]