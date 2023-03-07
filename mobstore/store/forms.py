from django import forms
from .models import ProductsModel


class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductsModel
        fields=['select_image','product_name','product_type','short_description','price']
        widgets={
            'select_image':forms.FileInput(attrs={'class':'form-control'}),
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'product_type':forms.TextInput(attrs={'class':'form-control'}),
            'short_description':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'})
        }