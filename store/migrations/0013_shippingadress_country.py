# Generated by Django 3.1.13 on 2021-12-10 05:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20211209_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingadress',
            name='country',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
