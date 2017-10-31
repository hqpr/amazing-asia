# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resort', '0004_resort_featured_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resort',
            name='featured_position',
            field=models.IntegerField(blank=True, choices=[(0, 'Top left'), (1, 'Top right'), (2, 'Bottom left'), (3, 'Bottom center')], null=True),
        ),
    ]