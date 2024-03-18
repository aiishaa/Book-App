from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from users.forms import  UserModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# Create your views here.

# def profile(request):
#     url = reverse('login')
#     return redirect(url)
    # return HttpResponse("Login successfully ")

def profile(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home page')
    else:
        form = UserModelForm()
    return render(request, 'registration/login.html', {'form': form})

def create_user(request):
    form = UserModelForm()
    if request.method=='POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("user created successfully")
    return render(request, 'users/create_user.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})