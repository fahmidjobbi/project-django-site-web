# Generated by Django 3.1.13 on 2021-11-30 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='store.Product'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
