from django.shortcuts import render,redirect
from django.contrib.auth.forms import (AuthenticationForm,UserCreationForm)
from django.contrib.auth.models import User
from django.contrib.auth import (authenticate,login,logout)
from django.contrib.auth.decorators import login_required
# Create your views here.


def signUpview(request):
    fm=UserCreationForm()
    if request.method=='POST':
        fm=UserCreationForm(data=request.POST)
        if fm.is_valid():
            fm.save()
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
                return redirect('home')
    return render(request,'signin.html',{'form':fm})

@login_required('/signin/')
def homeView(request):
    return render(request,'home.html')


    
