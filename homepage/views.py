from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login_page.html')

def signup(request):
    return render(request, 'signup.html')
def cart(request):
    return render(request, 'cart.html')