from django.urls import path
from .views import *

urlpatterns = [
    path('uhome/',UHome.as_view(),name='uhome'),
    path('cart/<int:did>',CartProduct.as_view(),name="cart"),
    # path('paym/',PaymentView.as_view(),name="paym"),
    path('viewcart/',ViewCart.as_view(),name="viewcart"),
    path('ordrcart/<int:oid>',PlaceOrderFromCart.as_view(),name="ordrcart"),
    path('bcart/<int:oid>',PlaceOrderFromCartqty.as_view(),name="bcart")
    # path('buy/<int:oid>',1BuyProduct.as_view(),name="buy"),
    # path('vbuy/<int:oid>',ViewBuyItem.as_view(),name="vbuy")
    # path('frombuy/<int:oid>',2PlaceOrderFromBuy.as_view(),name="frombuy")
]




