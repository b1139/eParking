# Generated by Django 3.1.1 on 2020-09-11 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('registration_no', models.CharField(blank='True', default='', max_length=40)),
            ],
            options={
                'db_table': 'vehicle',
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('slot_no', models.IntegerField()),
                ('parked_vehicle', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.vehicle')),
            ],
            options={
                'db_table': 'slot',
            },
        ),
    ]
