# Generated by Django 3.0.7 on 2020-07-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akskate', '0015_bearings_hardgoods_lijas'),
    ]

    operations = [
        migrations.AddField(
            model_name='decks',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
