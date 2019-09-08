from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserDetails
from selection.models import Design

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
