# Generated by Django 3.2.12 on 2022-04-02 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart_api', '0007_alter_productcart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonde',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_command', to='cart_api.user'),
        ),
    ]