# Generated by Django 5.0 on 2023-12-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_reservation_seat_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=10),
            preserve_default=False,
        ),
    ]
