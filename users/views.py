from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from users.forms import UserModelForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged In Successfully')
                return redirect('home page')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def create_user(request):
    form = UserModelForm()
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return redirect(reverse('login'))
    return render(request, 'users/create_user.html', {'form': form})

# Logout from the system
def logout_view(request):
    logout(request)
    # Consider adding a logout template here (optional)
    return redirect('home page')