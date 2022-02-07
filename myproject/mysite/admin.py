from django.contrib import admin
from .models import Branch
# Register your models here.
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display=('bname','bfiles')