from companies.models import Company
from django.contrib import admin

class CompanyAdmin(admin.ModelAdmin):

    list_display = ('name', 'address')
    list_filter = ['name']
    search_fields = ['name']
    name_hierarchy = 'name'


admin.site.register(Company, CompanyAdmin)
