from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import View,TemplateView,CreateView,UpdateView
from django.contrib import messages
from django.contrib.auth import authenticate
from.forms import ProductForm
from .models import ProductsModel

# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect('log')
    return wrapper


@method_decorator(signin_required,name='dispatch')
class SHome(CreateView):
    template_name='shome.html'
    form_class=ProductForm
    model=ProductsModel
    success_url=reverse_lazy('uhome')
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        prdct=self.model.objects.all()
        context['product']=prdct
        return context

class DeleteProduct(View):
    def get(self,request,*args,**kwargs):
        did=kwargs.get("did")
        prd=ProductsModel.objects.get(id=did)
        prd.delete()
        return redirect('shome')

class UpdateProductView(UpdateView):
    template_name='edit.html'
    form_class=ProductForm
    model=ProductsModel
    success_url=reverse_lazy('shome')
    pk_url_kwarg='did'
    def form_valid(self,form):
        self.object=form.save()
        messages.success(self.request,"Product Updated Successfully")
        return super().form_valid(form)




    


@method_decorator(signin_required,name='dispatch')
class AddProducts(CreateView):
    template_name='addprdcts.html'   
    form_class=ProductForm
    model=ProductsModel
    success_url=reverse_lazy('shome')
    def form_valid(self,form):
        # form=ProductForm(request.POST,files=request.FILES)
        form.instance.store=self.request.user
        self.object=form.save()
        messages.success(self.request,"Product Added Successfully !!")
        return super().form_valid(form)





















    