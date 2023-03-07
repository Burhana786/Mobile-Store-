from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from django.views.generic import TemplateView,FormView,CreateView,View
from django.contrib import messages
from store .forms import ProductForm
from store .models import ProductsModel
from .forms import PaymentForm
from .models import paymentItem,Orders
from account.models import User

# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect('log')
    return wrapper

@method_decorator(signin_required,name='dispatch')
class UHome(FormView):
    template_name='uhome.html'
    form_class=ProductForm
    model=ProductsModel
    success_url=reverse_lazy('uhome')
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        prdct=self.model.objects.all()
        context['product']=prdct
        return context


@method_decorator(signin_required,name='dispatch')
class CartProduct(FormView):
    model=Orders
    template_name='cart.html'
    success_url=reverse_lazy('cart')
    def get(self,request,*args,**kwargs):
        did=kwargs.get("did")
        prd=ProductsModel.objects.get(id=did)
        user=self.request.user
        Orders.objects.create(product=prd,user=user,status="cart")
        return redirect('uhome')
    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     user=self.request.user
    #     cart=self.model.objects.filter(status="cart",user=user)
    #     print(cart)
    #     context['product']=cart
    #     return context



# @method_decorator(signin_required,name='dispatch')
# class ViewCart(FormView):
#     template_name='cart.html'
#     model=Orders
#     success_url=reverse_lazy('cart')
#     def get_context_data(self,**kwargs):
#         context=super().get_context_data(**kwargs)
#         user=self.request.user
#         cart=self.model.objects.filter(status="cart",user=user)
#         context['product']=cart
#         return context
@method_decorator(signin_required,name='dispatch')
class ViewCart(View):
    def get(self,request,*args,**kwargs):
        user=self.request.user    
        cart=Orders.objects.filter(status="cart",user=user)
        return render(request,"cart.html",{"data":cart})
    




@method_decorator(signin_required,name='dispatch')
class PlaceOrderFromCart(View):
    def get(self,request,*args,**kwargs):
        user=self.request.user
        oid=kwargs.get("oid")
        oitem=Orders.objects.get(id=oid)
        return render(request,"placeorder.html",{"data":oitem})
    

@method_decorator(signin_required,name='dispatch')
class PlaceOrderFromCartqty(CreateView):
    model=Orders
    template_name='placeorder.html'
    success_url=reverse_lazy('viewcart')
    
    def post(self,request,*args,**kwargs):
        user=self.request.user
        oid=kwargs.get("oid")
        qty=request.POST.get("qty")
        oitem=Orders.objects.get(id=oid,user=user)
        oitem.quantity=qty
        Orders.objects.create(product=oitem,user=user,status="ordered")
        oitem.status="ordered"
        oitem.save()
        return redirect("uhome")












# 1

# @method_decorator(signin_required,name='dispatch')
# class BuyProduct(FormView):
#     model=Orders
#     template_name='placeorder.html'
#     success_url=reverse_lazy('vbuy')
#     def get(self,request,*args,**kwargs):
#         oid=kwargs.get("oid")
#         prd=ProductsModel.objects.get(id=oid)
#         user=self.request.user
#         Orders.objects.create(product=prd,user=user,status="ordered")
#         return render(request,"viewbuy.html")
#     # def get_context_data(self,**kwargs):
#     #     context=super().get_context_data(**kwargs)
#     #     oid=kwargs.get("oid")
#     #     prd=ProductsModel.objects.get(id=oid)
#     #     user=self.request.user
#     #     oitem=self.model.objects.filter(id=oid,user=user,status="ordered")
#     #     context['data']=oitem
#     #     return context

# 2
# @method_decorator(signin_required,name='dispatch')
# class PlaceOrderFromBuy(View):
#     def get(self,request,*args,**kwargs):
#         user=self.request.user
#         oid=kwargs.get("oid")
#         oitem=Orders.objects.get(id=oid)
#         return render(request,"viewbuy.html",{"data":oitem})

#     def post(self,request,*args,**kwargs):
#         user=self.request.user
#         oid=kwargs.get("oid")
#         qty=request.POST.get("qty")
#         order=Orders.objects.get(id=oid)
#         order.quantity=qty
#         # order.status="ordered"
#         order.save()
#         return redirect("frombuy")
    






# @method_decorator(signin_required,name='dispatch')
# class BuyOrderFromBuy(View):
#     def get(self,request,*args,**kwargs):
#         user=self.request.user  
#         oid=kwargs.get("oid")
#         oitem=Orders.objects.get(id=oid)  
#         cart=Orders.objects.filter(status="ordered",user=user,product=oitem)
#         return render(request,"cart.html",{"data":cart})
    
    
    
    
    
    
    # def get(self,request,*args,**kwargs):
    #     user=self.request.user
    #     oid=kwargs.get("oid")
    #     oitem=Orders.objects.filter(id=oid,user=user,status="ordered")
    #     return render(request,"viewbuy.html",{"data":oitem})

    # def post(self,request,*args,**kwargs):
    #     user=self.request.user
    #     oid=kwargs.get("oid")
    #     qty=request.POST.get("qty")
    #     order=Orders.objects.filter(id=oid,user=user,status="ordered")
    #     order.quantity=qty
    #     # order.status="ordered"
    #     order.save()
    #     return redirect("uhome")









# class ViewBuyItem(View):
#     def get(self,request,*args,**kwargs):
#         user=self.request.user 
#         oid=kwargs.get("oid")
#         bitem=Orders.objects.filter(id=oid,user=user)   
#         return redirect(request,"placeorder.html.html",{"data":bitem})
    

    # def post(self,request,*args,**kwargs):
    #     user=self.request.user
    #     oid=kwargs.get("oid")
    #     qty=request.POST.get("qty")
    #     order=Orders.objects.get(id=oid)
    #     order.quantity=qty
    #     order.status="ordered"
    #     order.save()
    #     return redirect("viewcart")
















# @method_decorator(signin_required,name='dispatch')
# class PaymentView(CreateView):
#     model=paymentItem
#     form_class=PaymentForm
#     template_name='pay.html'
#     success_url=reverse_lazy('uhome')
#     def form_valid(self,form):
#         form.instance.user=self.request.user
#         self.object=form.save()
#         messages.success(self.request,"payment Compleated Successfully")
#         return super().form_valid(form)

    

    













    