# Generated by Django 4.1.3 on 2023-02-11 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payment',
            new_name='paymentItem',
        ),
        migrations.RenameField(
            model_name='paymentitem',
            old_name='payment',
            new_name='payment_type',
        ),
    ]