# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class types_of_expenses(models.Model):
    expense_name = models.CharField(max_length=200)
    expense_color = models.CharField(max_length=10)

    class Meta:
        db_table = 'buhrax_types_of_expenses'
        verbose_name = 'Типы расходов'
        verbose_name_plural = 'Типы расходов'

    def __unicode__(self):
        return self.expense_name


class expense(models.Model):
    expense_type = models.ForeignKey(types_of_expenses)
    expenditure_name = models.CharField(max_length=200)
    description = models.CharField(
        max_length=250, default='описание статьи затрат')

    class Meta:
        db_table = 'buhrax_expense'
        verbose_name = 'Статьи расходов'
        verbose_name_plural = 'Статьи расходов'

    def __unicode__(self):
        return unicode(self.expenditure_name)


class cash(models.Model):
    cash_type_choices = (
        ('P', 'Приход'),
        ('R', 'Расход'),
    )
    cash_expense = models.ForeignKey(expense, default=None)
    cash_date = models.DateField(default=date.today)
    cash_type = models.CharField(max_length=1, choices=cash_type_choices)
    cash_value = models.FloatField(default=0.0)
    cash_desc = models.CharField(
        max_length=200, default='комментарий к движению средств')

    class Meta:
        db_table = 'buhrax_cash'
        verbose_name = 'Деньги'
        verbose_name_plural = 'Деньги'

    def __unicode__(self):
        return unicode(self.cash_expense)


class cash_planned(models.Model):
    planned_cash_type_choices = (
        ('W', 'Неделя'),
        ('M', 'Месяц'),
        ('Y', 'Год')
    )
    planned_cash_expense = models.ForeignKey(expense, default=None)
    planned_cash_date = models.DateField(default=date.today)
    planned_cash_repeat = models.CharField(max_length=1, choices=planned_cash_type_choices)
    planned_cash_value = models.FloatField(default=0.0)
    planned_cash_desc = models.CharField(
        max_length=200, default='комментарий к движению средств')

    class Meta:
        db_table = 'buhrax_planned_cash'
        verbose_name = 'Запланированные затраты'
        verbose_name_plural = 'Запланированные затраты'

    def __unicode__(self):
        return unicode(self.planned_cash_expense)
