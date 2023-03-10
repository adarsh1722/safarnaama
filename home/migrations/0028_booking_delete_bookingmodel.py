# Generated by Django 4.1.4 on 2022-12-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_bookingmodel_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('number_of_peoples', models.IntegerField(blank=True, null=True)),
                ('number_of_rooms', models.IntegerField(blank=True, null=True)),
                ('check_in_date', models.DateTimeField(blank=True, null=True)),
                ('chekout_out_date', models.DateTimeField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BookingModel',
        ),
    ]
