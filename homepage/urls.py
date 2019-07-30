from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('login/', views.login, name='login'),
=======
    path('signup', views.signup, name='signup'),
>>>>>>> origin/weaves

]