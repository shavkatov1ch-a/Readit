from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name', 'email')
    readonly_fields = ['pub_date']


admin.site.register(Contact, ContactAdmin)
