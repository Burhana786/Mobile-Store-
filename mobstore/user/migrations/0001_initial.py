# Generated by Django 4.1.3 on 2023-02-05 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('UPI/NetBanking', 'UPI/NetBanking'), ('Pay with Debit/Credit/ATM Cards', 'Pay with Debit/Credit/ATM Cards'), ('Cash on Delivery', 'Cash on Delivery')], max_length=35)),
            ],
        ),
    ]
