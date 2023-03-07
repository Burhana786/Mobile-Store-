from django.urls import path
from .views import *

urlpatterns = [
    path('shome/',SHome.as_view(),name='shome'),
    path('add-product/',AddProducts.as_view(),name='add-product'),
    path('delp/<int:did>',DeleteProduct.as_view(),name="delp"),
    path('edit/<int:did>',UpdateProductView.as_view(),name="edit")
    
]





