# Generated by Django 3.0.7 on 2020-07-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akskate', '0008_auto_20200710_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trucks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Wheels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Decks',
        ),
    ]
