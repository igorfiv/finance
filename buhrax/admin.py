from django.contrib import admin

# Register your models here.

from .models import types_of_expenses, expense, cash, cash_planned


class expenseAdmin(admin.ModelAdmin):
    list_display = ('expenditure_name', 'expense_type', 'description')


class cashAdmin(admin.ModelAdmin):
    list_display = ('cash_expense', 'cash_date', 'cash_type', 'cash_value')


class planned_cash_Admin(admin.ModelAdmin):
    list_display = ('planned_cash_expense', 'planned_cash_date', 'planned_cash_repeat', 'planned_cash_value')

admin.site.register(types_of_expenses)
admin.site.register(expense, expenseAdmin)
admin.site.register(cash, cashAdmin)
admin.site.register(cash_planned, planned_cash_Admin)
