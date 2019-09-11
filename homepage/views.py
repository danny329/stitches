from django.shortcuts import render,redirect
from selection.models import Orders,OrderStatusCode
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login_page.html')

def signup(request):
    return render(request, 'signup.html')
def cart(request):

        cart = Orders.objects.filter(user__username=request.user, status__status='INCART').order_by('pk')
        total = 0
        if request.method == 'POST':
            #addition n sub to cart
            if 'clothid_plus' in request.POST:
                print(request.POST['clothid_plus'])
                changecart = Orders.objects.get(pk=request.POST['clothid_plus'])
                if changecart.quantity < 6:
                    changecart.quantity = changecart.quantity + 1
                    changecart.subtotal = changecart.cloth_menu.price * changecart.quantity
                    changecart.save()
            if 'clothid_minus' in request.POST:
                print(request.POST['clothid_minus'])
                changecart = Orders.objects.get(pk=request.POST['clothid_minus'])
                if changecart.quantity > 1:
                    changecart.quantity = changecart.quantity - 1
                    changecart.subtotal = changecart.cloth_menu.price * changecart.quantity
                    changecart.save()
            if 'clothid_delete' in request.POST:
                print(request.POST['clothid_delete'])
                changecart = Orders.objects.get(pk=request.POST['clothid_delete'])
                changecart.delete()
        for item in cart:
            total = total + item.subtotal

        context = {'cart': cart,'total': total}
        return render(request, 'cart.html', context)



