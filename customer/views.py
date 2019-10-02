from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserDetails
from .forms import UserForm, UserExtend, MeasurementForm
from selection.models import Orders,Measurement

# Create your views here.


def signupform(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        gender = request.POST['gender']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)
                userdetails = UserDetails.objects.create(userref=user, gender=gender)
                user.save()
                userdetails.save()

                print('user created')
        else:
            print('password wrng')
        return redirect('/')
    else:
        return render(request, 'signup.html')


# verify login
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('invalid ')
            return redirect('/login')



def logout(request):

    auth.logout(request)

    return redirect('/')


def userprofile(request):
    try:
        if request.user.is_authenticated:
            if request.method == 'POST':
                formuser = UserForm(request.POST, instance=User.objects.get(pk=request.user.pk))
                formuserextend = UserExtend(request.POST, instance=UserDetails.objects.get(userref=request.user))
                formmeasuremeasurement = MeasurementForm(request.POST, instance=Measurement.objects.get(user=request.user))

                if formuser.is_valid() and formuserextend.is_valid() and formmeasuremeasurement.is_valid():
                    formuser.save(commit=False)
                    formuserextend.save(commit=False)
                    formmeasuremeasurement.save()
                    print("success")
            else:
                formuser = UserForm(instance=User.objects.get(pk=request.user.pk))
                formuserextend = UserExtend(instance=UserDetails.objects.get(userref=request.user))
                formmeasuremeasurement = MeasurementForm()
            context = {'formuser': formuser, 'formuserextend': formuserextend, 'formmeasuremeasurement': formmeasuremeasurement}
            return render(request, 'userprofile.html', context)


        else:
            return redirect('/customer/login_page/')
    except Exception as e:
        print(e)
