from django.shortcuts import render,redirect
from .form import RegisterForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def Home(request):
    return render(request,"main/home.html")

def Registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
        
    else:
        form = RegisterForm()
    
        

    return render(request,'registration/register.html', {"form":form})


def Logout(request):
    logout(request)
    return redirect('/login')