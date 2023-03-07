from django.db import models
from account.models import User
# Create your models here.


class ProductsModel(models.Model):
    select_image=models.ImageField(upload_to='product_images',null=True)
    product_name=models.CharField(max_length=50)
    product_type=models.CharField(max_length=50)
    short_description=models.CharField(max_length=100)
    price=models.IntegerField()
    store=models.ForeignKey(User,on_delete=models.CASCADE,related_name='store')
    


class pay(models.Model):
    product_buy=models.ManyToManyField(ProductsModel)
    user_buy=models.ManyToManyField(User)
    options=(
        ('UPI/NetBanking','UPI/NetBanking'),
        ('Pay with Debit/Credit/ATM Cards','Pay with Debit/Credit/ATM Cards'),
        ('Cash on Delivery','Cash on Delivery')
    )
    payment_type=models.CharField(max_length=35,choices=options)