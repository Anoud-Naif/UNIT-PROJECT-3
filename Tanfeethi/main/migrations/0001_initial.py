# Generated by Django 5.0 on 2023-12-06 10:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_from', models.CharField(choices=[('Riyadh', 'Riyadh'), ('Doha', 'Doha'), ('Khobar', 'Khobar'), ('Muscat', 'Muscat')], default='Riyadh', max_length=20)),
                ('_to', models.CharField(choices=[('Riyadh', 'Riyadh'), ('Doha', 'Doha'), ('Khobar', 'Khobar'), ('Muscat', 'Muscat')], default='Doha', max_length=20)),
                ('departing', models.DateField()),
                ('returning', models.TimeField()),
                ('passenge_number', models.IntegerField()),
                ('passenge_age', models.CharField(choices=[('Adults', 'Adults'), ('Children', 'Children'), ('infants', 'Infants'), ('infant on seat', 'Infant On Seat')], default='Adults', max_length=20)),
                ('_class', models.CharField(choices=[('Guest', 'Guest'), ('Business', 'Business'), ('First', 'First')], default='Guest', max_length=10)),
                ('passenger', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
