# Generated by Django 4.0.4 on 2022-04-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_list_cart_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_list',
            name='username',
            field=models.CharField(default=None, max_length=200, unique=True),
        ),
    ]
