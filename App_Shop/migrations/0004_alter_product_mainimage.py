# Generated by Django 3.2 on 2021-05-26 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Shop', '0003_alter_product_mainimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mainimage',
            field=models.ImageField(upload_to='Products'),
        ),
    ]
