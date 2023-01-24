from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    return render(request,"PizzaStore/index.html")

def signup(request):
    return render(request,"PizzaStore/Signup.html")

def signupHandle(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        user=User.objects.create_user(username,email,pass1)
        user.save()
        return redirect('/')
    else:
        return HttpResponse("404 not found")

def loginhandle(request):
    if request.method=="POST":
        lusername=request.POST['lusername']
        lpassword=request.POST['lpassword']
        user=authenticate(username=lusername,password=lpassword)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("404 not found")

def logoutHandle(request):
    logout(request)
    return redirect('/')       

def about(request):
    return render(request,"PizzaStore/about.html")

def menu(request):
    products=Product.objects.all()
    print(products)
    product_count=len(products)
    params={'products':products,'range':range(0,product_count),'cat1':'pizza','cat2':'pasta','cat3':'drinks'}
    return render(request,'PizzaStore/Menu.html',params)