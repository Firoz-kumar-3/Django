from django.shortcuts import render, HttpResponseRedirect
from .forms import Userform,EditUserProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import Userform
def sign_up(request):
    if request.method=="POST":
        fm=Userform(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=Userform()
    return render(request,'enroll/registration.html',{'form':fm})

def user_login(request):
   if not request.user.is_authenticated: 
       if request.method=="POST":
           fm=AuthenticationForm(request=request,data=request.POST)
           if fm.is_valid():
               uname=fm.cleaned_data['username']
               upass=fm.cleaned_data['password']
               user=authenticate(username=uname,password=upass)
               if user is not None:
                   login(request,user)
                   messages.success(request,"You have been successfully login ")
                   return HttpResponseRedirect('/profile/')
       else:
           fm=AuthenticationForm()
       return render(request,'enroll/login.html',{'form':fm})
   else:
        return HttpResponseRedirect('/profile/') 

def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Your profile has been updated niga")
                return HttpResponseRedirect('/profile/')
        else:
            fm=EditUserProfileForm(instance=request.user)
        return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def change_pass(request):
    if request.method=="POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect('/profile/')
    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'enroll/changepass.html',{'form':fm})
