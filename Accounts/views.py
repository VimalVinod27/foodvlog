from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from .forms import RegForm,LoginForm
from cart.models import *
from cart.views import *

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2= form.cleaned_data['password2']
            if password1==password2:
                if User.objects.filter(username=username):
                    messages.info(request,message='username already exists')
                else:
                    User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username,
                                             password=password1)
                    return redirect('shop:shopindex')
            else:
                messages.info(request,message='password mismatch')



    else:
        form=RegForm()
    return render(request,'register.html',{'form':form})

def loginuser(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            #print(user.first_name)
            if user is not None:
                auth.login(request,user)
                request.session['member_id']=user.id

                return redirect('shop:shopindex')
            else:
                form=LoginForm()


    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def logoutuser(request):
    auth.logout(request)
    return redirect('/')








# Create your views here.
