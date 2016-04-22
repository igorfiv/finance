# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buhrax', '0002_expense_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='cash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '\u0414\u0435\u043d\u044c\u0433\u0438',
                'verbose_name_plural': 'cahes',
            },
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name': '\u0420\u0430\u0441\u0445\u043e\u0434', 'verbose_name_plural': '\u0420\u0430\u0441\u0445\u043e\u0434\u044b'},
        ),
        migrations.AlterModelOptions(
            name='types_of_expenses',
            options={'verbose_name': '\u0422\u0438\u043f\u044b \u0440\u0430\u0441\u0445\u043e\u0434\u043e\u0432', 'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0440\u0430\u0441\u0445\u043e\u0434\u043e\u0432'},
        ),
        migrations.AlterModelTable(
            name='expense',
            table='buhrax_expense',
        ),
        migrations.AlterModelTable(
            name='types_of_expenses',
            table='buhrax_types_of_expenses',
        ),
    ]
