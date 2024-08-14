from django.contrib import admin

from master.models import NameServer


@admin.register(NameServer)
class NameServer_Admin(admin.ModelAdmin):
    list_display = ('name', 'ip')
    search_fields = ('name',)
