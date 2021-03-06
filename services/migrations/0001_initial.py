# Generated by Django 3.2.5 on 2021-07-25 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Approved')])),
                ('time_of_result', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Service Name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Sub Service')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
        ),
        migrations.CreateModel(
            name='SubTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeSlot', models.TextField()),
                ('Date', models.TextField()),
                ('servicename', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.service')),
                ('subservice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.subservice')),
            ],
        ),
        migrations.CreateModel(
            name='BookingLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.booking')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
        ),
    ]
