from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Record
from .forms import AddRecordForm

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
    return redirect('login')
def customer_records(request, pk):
    customer_records=Record.objects.get(id=pk)
    return render(request, 'customer_records.html', {'customer_records':customer_records})
def records(request):
    records=Record.objects.all()
    return render(request, 'records.html', {'records':records})
def delete(request,pk):
    if request.user.is_authenticated:
          records=Record.objects.get(id=pk)
          records.delete()
          messages.info(request, ('Record has been deleted!'))
          return redirect('records')
    else:
        messages.info(request, ('You must be logged in to delete records!'))
        return redirect('records')
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('login')  