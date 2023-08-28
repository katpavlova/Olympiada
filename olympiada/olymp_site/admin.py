from django.contrib import admin
from .models import Blank


class BlankAdmin(admin.ModelAdmin):
    list_display = ('fio', 'education', 'phone', 'email',)
    search_fields = ('fio', 'education', 'phone', 'email',)


admin.site.register(Blank, BlankAdmin)
