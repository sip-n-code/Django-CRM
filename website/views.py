from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # Check to see if the user is logging
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            # return render(request, 'home.html', {})
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('home')
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return render(request, 'home.html', {})
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    #return render(request, 'home.html', {})
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})