from django.contrib import admin
from .models import EntryURL
# Register your models here.
@admin.register(EntryURL)
class UserAdmin(admin.ModelAdmin):
    list_display = ('URL','E1','E1O','E2','E2O','E3','E3O','E4','E4O','E5','E5O','E6','E6O','E7','E7O','E8','E8O','E9','E9O','E10','E10O')
