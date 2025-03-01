from django.shortcuts import render,redirect
from django.contrib.auth.forms import (AuthenticationForm,UserCreationForm)
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate,login,logout)
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from django.contrib import messages
from .models import CustomUserModel


def signUpview(request):
    fm=CustomUserForm()
    if request.method=='POST' and request.FILES:
        fm=CustomUserForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,'user created Sucessfully')
            return redirect('signin')
    return render(request,'signup.html',{'form':fm})

def logInView(request):
    fm=AuthenticationForm()
    if request.method=='POST':
        fm=AuthenticationForm(data=request.POST)
        if fm.is_valid():
            cleaned_data=fm.cleaned_data
            user=authenticate(**cleaned_data)
            if user is not None:
                login(request,user)
                messages.add_message(request,messages.SUCCESS,'User logged in succesfully')
                return redirect('home')
            
        messages.add_message(request,messages.ERROR,'Invalid Credentials')

    return render(request,'signin.html',{'form':fm})

@login_required(login_url='/signin/')
def homeView(request):
    obj=CustomUserModel.objects.get(username=request.user.username)
    return render(request,'home.html',{'user':obj})

def logOutView(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'User logged out succesfully')

    return redirect('signin')


    
