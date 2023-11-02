from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth import login as auth_login, authenticate
from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        try:
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                form.save()
                return redirect('login') 
        except IntegrityError:
            form.add_error('email', 'This email is already in use. Please choose a different email.')  
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == "POST":
        email=request.POST('email')
        password=request.POST('password')
        user=authenticate(request,email=email,password=password)
        # auth_login(request,user)
        return redirect('home')
#          
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})


def homePage(request):
    return render(request,'home.html')
