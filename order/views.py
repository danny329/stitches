from django.shortcuts import render,redirect, reverse, HttpResponse
from selection.models import Color,Pattern,ClothType, ClothMenu, Orders , Collar, Cuff, ButtonHole,Button, Back,Front, Pocket, ShirtFit, Measurement,StandardSize,OrderStatusCode
from customer.forms import MeasurementForm
from homepage.views import cart
from django.contrib.auth.models import User

# Create your views here.
def checkout(request):
    if request.user.is_authenticated:
       context={}
    return render(request,'checkout.html',context)