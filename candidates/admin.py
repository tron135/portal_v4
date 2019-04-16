from django.contrib import admin
from .models import Telecaller, Enquiry, Admission

# Register your models here.
class TelecallersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'qualification', 'course', 'source', 'date')
    list_display_links = ('id', 'name')
    list_filter = ('telecaller',)
    search_fields = ('name', 'email', 'qualification', 'course',)
    list_per_page = 25

admin.site.register(Telecaller,TelecallersAdmin)
admin.site.register(Enquiry)
admin.site.register(Admission)