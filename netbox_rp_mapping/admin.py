from django.contrib import admin
from .models import RPGroupEntry, StaticRP


@admin.register(StaticRP)
class RPAdmin(admin.ModelAdmin):
    pass


@admin.register(RPGroupEntry)
class RPGroupAdmin(admin.ModelAdmin):
    pass
