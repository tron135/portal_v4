from django.contrib import admin
from .models import Telecallers

# Register your models here.
class TelecallersAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id', 'name')
admin.site.register(Telecallers, TelecallersAdmin)