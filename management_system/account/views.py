from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def Signup(request):
    form = SignupForm()
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        my_user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        my_user.save()
        return redirect('login')
    return render(request, 'signup.html', {'form': form})

def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request,"Invalid username or password")

    form = SignupForm()
    return render(request, 'login.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect('login')