from django.shortcuts import render, redirect
from .forms import CreateUserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


def register_user(request):
    if request.method == 'POST':
        form = CreateUserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'user registered successfully!', 'success')
            return redirect('home')
    else:
        form = CreateUserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in...', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Username or password is incorrect...', 'danger')
                return redirect('user_login')
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})


def logout(request):
    logout(request)
    user = User.is_authenticated
    messages.success(request, f'logged out from {user} successfully!', 'success')
    return redirect('home')
