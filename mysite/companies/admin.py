from companies.models import Company
from django.contrib import admin

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Contact information', {'fields': ['address','phone_number'],'classes': ['collapse']}),
        ('Android information', {'fields': ['android_users']}),
    ]
    list_display = ('name', 'pub_date', 'address')
    list_filter = ['name']
    search_fields = ['name']
    name_hierarchy = 'name'


admin.site.register(Company, CompanyAdmin)