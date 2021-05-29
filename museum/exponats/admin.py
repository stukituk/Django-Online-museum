from django.contrib import admin

from .models import *

class ExponatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Exponat, ExponatAdmin)
admin.site.register(Category)