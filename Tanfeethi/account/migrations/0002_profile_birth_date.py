# Generated by Django 5.0 on 2023-12-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(default='2023-01-01'),
        ),
    ]
