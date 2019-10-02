from django.shortcuts import render,redirect, reverse, HttpResponse
from selection.models import Color,Pattern,ClothType, ClothMenu, Orders , Collar, Cuff, ButtonHole,Button, Back,Front, Pocket, ShirtFit, Measurement,StandardSize,OrderStatusCode
from customer.forms import MeasurementForm, UserDetailForm
from payment.models import OrderHistory
from customer.models import UserDetails
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.
def checkout(request,part=1):
    try:
        if request.user.is_authenticated:
            cart = Orders.objects.filter(user__username=request.user, status__status=OrderStatusCode.objects.get(status='INCART')).order_by('pk')
            print(cart.exists())
            if cart.exists() == False:
                print('here')
                return redirect('/selection/select')
            gt = 0
            for item in cart:
                gt += item.subtotal
                print(type(gt))
            if request.method == 'POST':
                if 'finishpayment' in request.POST:
                    carttoorder = OrderHistory.objects.create(user=request.user, price=gt, date=datetime.now())
                    # carttoorder.user = request.user
                    # carttoorder.price = gt
                    # carttoorder.date = datetime.now()
                    for item in cart:
                        item.status = OrderStatusCode.objects.get(status='CONFIRMED')
                        item.save()
                        carttoorder.order.add(item)
                    carttoorder.save()
                    print('e')
                try:
                    shippingdetail = UserDetailForm(request.POST, instance=UserDetails.objects.get(userref=request.user))
                except Exception as e:
                    shippingdetail = UserDetailForm(request.POST)
                if shippingdetail.is_valid():
                    shipinfo = shippingdetail.save(commit=False)
                    shipinfo.userref = request.user
                    shipinfo.save()
            else:
                try:
                    shippingdetail = UserDetailForm(instance=UserDetails.objects.get(userref=request.user))
                except Exception as e:
                    shippingdetail = UserDetailForm()
                    print(e)
            context={'cart' : cart, 'gt' : gt, 'shippingdetail' : shippingdetail}
            if part == 'review':
                context['review'] = 'show active'
            if part == 'shipping':
                context['shipping'] = 'show active'
                context['payment'] = 'invisible'
            if part == 'payment':
                context['payment'] = 'show active'
            return render(request,'checkout.html', context)
        else:
            return redirect('/')
    except Exception as e:
        print(e)

def orders(request):
    try:
        if request.user.is_authenticated:
            allordersitemconfirmed = Orders.objects.filter(user__username=request.user,
                                         status__status=OrderStatusCode.objects.get(status='CONFIRMED')).order_by('pk')
            allordersitemdelivered = Orders.objects.filter(user__username=request.user,
                                                           status__status=OrderStatusCode.objects.get(
                                                               status='DELIVERED')).order_by('pk')
            allorders = OrderHistory.objects.filter(user=request.user)
            context={'allorders' : allorders, 'allordersitemconfirmed': allordersitemconfirmed, 'allordersitemdelivered': allordersitemdelivered}
            return render(request, 'orders.html', context)
        else:
            return redirect('/')
    except Exception as e:
        print(e)