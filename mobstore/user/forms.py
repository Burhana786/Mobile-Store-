from django import forms
from .models import paymentItem


class PaymentForm(forms.ModelForm):
    class Meta:
        model=paymentItem
        exclude=['user_buy','product_item']