from django.contrib import admin
from .models import MenuItem
from .forms import MenuItemForm


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    form = MenuItemForm


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    form = MenuItemForm

admin.site.register(MenuItem, MenuItemAdmin)
