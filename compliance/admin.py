from django.contrib import admin
from compliance.models import Organization, Employee

class EmployeeInline(admin.TabularInline):
	model = Employee
	extra = 5

class OrganizationAdmin(admin.ModelAdmin):
	fieldsets = [
	    (None, {'fields': ['name']}),
	]
	inlines = [EmployeeInline]

admin.site.register(Organization, OrganizationAdmin)

