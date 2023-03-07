from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from.models import User
from.forms import UserRegForm,SigninForm

# Create your views here.

class Home(TemplateView):
    template_name='home.html'


class About(TemplateView):
    template_name='about.html'





class UserRegView(CreateView):
    template_name='reg.html'
    model=User
    form_class=UserRegForm
    success_url=reverse_lazy('home')
    def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            email_id=form_data.cleaned_data.get('email')
            uname=form_data.cleaned_data.get('username')
            pwd=form_data.cleaned_data.get('password1')
            msg="You are Registered in Mobile Store .\n Your Username :"+str(uname)+"\n Password :"+str(pwd)
            form_data.save()
            messages.success(request,"Registration Compleated!!!")
            return redirect('home')
        else:
            messages.error(request,"Registration Failed")
            return render(request,"reg.html",{'form':form_data})



class SignIn(FormView):
    form_class=SigninForm
    template_name='log.html'
    success_url=reverse_lazy('home')
    def post(self,request):
        uname=request.POST.get('username')
        pw=request.POST.get('password')
        # utype=User.objects.get('usertype')
        user=authenticate(request,username=uname,password=pw)
        if user:
            if user.usertype=="store":
                login(request,user)
                return redirect('shome')
            else:
                login(request,user)
                return redirect('uhome')
        else:
            
            messages.error(request,"Credentials are wrong")
            return redirect("log")


class SignOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("log")