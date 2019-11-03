from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserDetails
from .forms import UserForm, UserExtend, MeasurementForm
from selection.models import Orders, Measurement
import sweetify

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
                sweetify.warning(request, 'Username already taken.')
                return render(request, 'signup.html')
            elif User.objects.filter(email=email).exists():
                sweetify.warning(request, 'Email already exists.')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)
                userdetails = UserDetails.objects.create(userref=user, gender=gender)
                user.save()
                userdetails.save()

                sweetify.success(request, 'Registration successful')
        else:
            sweetify.error(request, 'Email mismatch.')
            return render(request, 'signup.html')

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
            sweetify.success(request, 'logged in as ' + request.user.username)
            return redirect('/')
        else:
            sweetify.error(request, 'user doesn\'t exist')
            return redirect('/login')



def logout(request):

    auth.logout(request)

    return redirect('/')


def userprofile(request):
    try:
        if request.user.is_authenticated:
            if request.method == 'POST':
                formuser = UserForm( instance=User.objects.get(pk=request.user.pk))
                formuserextend = UserExtend(instance=UserDetails.objects.get(userref=request.user))
                try:
                    formmeasuremeasurement = MeasurementForm(request.POST, instance=Measurement.objects.get(user=request.user), initial={'user': request.user.pk})
                except:
                    formmeasuremeasurement = MeasurementForm(request.POST, initial={'user': request.user.pk})
                formmeasuremeasurement.fields['user'].disabled = True

                if formmeasuremeasurement.is_valid():
                    formmeasuremeasurement.save()
                    sweetify.success(request, 'Success')
            else:
                formuser = UserForm(instance=User.objects.get(pk=request.user.pk))
                formuserextend = UserExtend(instance=UserDetails.objects.get(userref=request.user))
                try:
                    formmeasuremeasurement = MeasurementForm(instance=Measurement.objects.get(user=request.user), initial={'user': request.user.pk})
                except:
                    formmeasuremeasurement = MeasurementForm(initial={'user': request.user.pk})
                formmeasuremeasurement.fields['user'].disabled = True
            context = {'formuser': formuser, 'formuserextend': formuserextend, 'formmeasuremeasurement': formmeasuremeasurement}
            return render(request, 'userprofile.html', context)


        else:
            return redirect('/customer/login_page/')
    except Exception as e:
        print(e)
