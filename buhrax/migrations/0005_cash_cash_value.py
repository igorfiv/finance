# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buhrax', '0004_auto_20160324_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash',
            name='cash_value',
            field=models.FloatField(default=0.0),
        ),
    ]
