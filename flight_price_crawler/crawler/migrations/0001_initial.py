# Generated by Django 4.2.6 on 2023-10-31 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlightReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_city', models.CharField(max_length=3)),
                ('destination_city', models.CharField(max_length=3)),
                ('departure_date', models.DateField()),
                ('traveler_type', models.CharField(max_length=10)),
            ],
        ),
    ]
