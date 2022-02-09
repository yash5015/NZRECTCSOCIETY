from django.contrib import admin
from .models import Branch, Loanform
# Register your models here.

admin.site.register(Branch)


@admin.register(Loanform)
class LoanformAdmin(admin.ModelAdmin):
    list_display = ('name', 'phno', 'regno', 'userform', 'date')
