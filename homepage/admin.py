from django.contrib import admin
from homepage.models import HomePage
"""
class HomeAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ('name',)

admin.site.register(HomePage, HomeAdmin)
"""
admin.site.register(HomePage)