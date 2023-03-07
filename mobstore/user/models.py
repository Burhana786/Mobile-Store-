from django.db import models
from store .models import ProductsModel
from account .models import User

# Create your models here.

# class Feedback(models.Model):
#     customer_name = models.CharField(max_length=120)
#     email = models.EmailField()
#     product = models.ForeignKey(Product)
#     details = models.TextField()
#     happy = models.BooleanField()
#     date = models.DateField(auto_now_add=True)


class Orders(models.Model):
    product=models.ForeignKey(ProductsModel,on_delete=models.CASCADE,related_name='product')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    date=models.DateField(auto_now_add=True)
    quantity=models.IntegerField(default=1)
    status=models.CharField(max_length=100)













    

class paymentItem(models.Model):
    # product_item=models.ForeignKey(ProductsModel,on_delete=models.CASCADE,related_name='product')
    # user_buy=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    options=(
        ('UPI/NetBanking','UPI/NetBanking'),
        ('Pay with Debit/Credit/ATM Cards','Pay with Debit/Credit/ATM Cards'),
        ('Cash on Delivery','Cash on Delivery')
    )
    payment_type=models.CharField(max_length=35,choices=options)

