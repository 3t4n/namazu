# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 01:30
from __future__ import unicode_literals

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
            name='AccelerationComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServerTime', models.DateField(auto_now_add=True)),
                ('Accelerometer_time', models.DateField()),
                ('XValue', models.FloatField()),
                ('YValue', models.FloatField()),
                ('ZValue', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Accelerometer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MemoryAddress', models.CharField(max_length=255)),
                ('Status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('GpsLatitude', models.CharField(max_length=255)),
                ('GpsLongitude', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GroupNodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GroupsNodes', to='api.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Synced', models.BooleanField(default=False)),
                ('PingTime', models.IntegerField()),
                ('GroupsNode', models.ManyToManyField(related_name='Nodes', to='api.GroupNodes')),
                ('Shared', models.ManyToManyField(related_name='SharedWith', to=settings.AUTH_USER_MODEL)),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='accelerometer',
            name='NodeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Accelerometers', to='api.Node'),
        ),
        migrations.AddField(
            model_name='accelerationcomponent',
            name='AccelerometerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Data', to='api.Accelerometer'),
        ),
    ]
