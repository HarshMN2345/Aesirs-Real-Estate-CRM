from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Record

def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form=SignUpForm()
    return render(request, 'register.html', {'form': form})
def home(request):
    records=Record.objects.all()
    
    return render(request, 'home.html',{'records':records})    
def login_user(request):
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
            return redirect('login')
     return render(request, 'login.html')
def logout_user(request):
    logout(request)
    messages.info(request, ('You have been logged out!'))
    return redirect('home')
def customer_records(request, pk):
    customer_records=Record.objects.get(id=pk)
    return render(request, 'customer_records.html', {'customer_records':customer_records})
def records(request):
    records=Record.objects.all()
    return render(request, 'records.html', {'records':records})
    
