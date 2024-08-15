from django.contrib import admin

from master.models import Server


@admin.register(Server)
class Server_Admin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)
