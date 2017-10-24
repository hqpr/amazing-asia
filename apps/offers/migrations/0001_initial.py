# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('expires_at', models.DateField(blank=True, null=True)),
                ('stays_from', models.DateField(blank=True, null=True)),
                ('stays_to', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='offers/')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
