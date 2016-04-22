# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenditure_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='types_of_expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_name', models.CharField(max_length=200)),
                ('expense_color', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buhrax.types_of_expenses'),
        ),
    ]