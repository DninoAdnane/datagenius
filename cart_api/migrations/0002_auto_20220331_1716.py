# Generated by Django 3.2.12 on 2022-03-31 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='valited',
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(default='2c93f01c-b116-11ec-b909-0242ac120002', max_length=100),
            preserve_default=False,
        ),
    ]
