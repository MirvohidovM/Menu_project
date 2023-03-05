from django.contrib import admin
from menu_app.models import Menu

class MenuAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Menu, MenuAdmin)
