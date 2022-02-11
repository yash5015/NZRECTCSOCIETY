from django.contrib import admin
from .models import Branch, Contact, Loanform
# Register your models here.

admin.site.register(Branch)
admin.site.register(Contact)


@admin.register(Loanform)
class LoanformAdmin(admin.ModelAdmin):
    list_display = ('name', 'phno', 'regno', 'userform', 'date','status')
