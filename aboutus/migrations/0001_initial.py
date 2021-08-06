# Generated by Django 3.2.5 on 2021-08-06 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='About Us')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Home Description')),
                ('contactdetail', models.TextField(verbose_name='Contcat Us')),
            ],
        ),
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutus.home')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutus.aboutus')),
            ],
        ),
    ]