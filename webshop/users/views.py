from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User

from users.models import Profile


# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('landing_page')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            print("User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('landing_page')
        else:
            print("User does not exist")

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def profiles(request):
    return render(request, 'users/profile.html')


def manage_users(request):
    users = Profile.objects.all()
    context = {'users': users}
    return render(request, 'users/manage-users.html', context)
