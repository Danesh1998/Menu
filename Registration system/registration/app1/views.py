# from django.http import render, HttpResponse,redirect
# from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def homepage(request):
    return render (request,'home.html')

def signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass11=request.POST.get('password1')
        pass2=request.POST.get('password2')
        my_user=User.objects.create_user(uname,email,pass11)

        if pass11!=pass2:
            return HttpResponse("youe password is wrong")
        my_user.save()
        return redirect('login')
    return render (request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass11=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass11)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('password is wrong')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')