# Generated by Django 3.0.7 on 2020-07-11 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akskate', '0012_auto_20200710_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item_price',
            field=models.IntegerField(),
        ),
    ]
