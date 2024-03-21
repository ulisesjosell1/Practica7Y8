from django.contrib import admin
from .models import Orden
# Register your models here.
class OrdenAdmin(admin.ModelAdmin):
    readonly_fields=("fecha_creacion",)

admin.site.register(Orden,OrdenAdmin)