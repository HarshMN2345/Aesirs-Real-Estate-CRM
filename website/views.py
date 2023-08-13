from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

def register_user(request):
    return render(request, 'register.html')  
def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.info(request, ('Error logging in - Please try again...'))
            return redirect('home')
    return render(request, 'home.html')        
def login_user(request):
   return render(request, 'login.html')
def logout_user(request):
    logout(request)
    messages.info(request, ('You have been logged out!'))
    return redirect('home')
   
