# Generated by Django 3.0.7 on 2020-07-21 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akskate', '0025_auto_20200720_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.IntegerField(),
        ),
    ]
