# Generated by Django 4.2.2 on 2023-06-24 07:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(blank=True, max_length=255, null=True)),
                ('which_department', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Staffs',
            },
        ),
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Enter a valid cellphone number.', regex='^09\\d{9}$')])),
                ('purpose', models.CharField(blank=True, max_length=500, null=True)),
                ('picture', models.FileField(blank=True, null=True, upload_to='pictures/')),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('person_to_visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AttendanceApp.staffs')),
            ],
            options={
                'verbose_name_plural': 'Visitors',
            },
        ),
    ]
