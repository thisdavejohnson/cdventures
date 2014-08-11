from django.contrib import admin
from compliance.models import Organization, Employee

class EmployeeInline(admin.StackedInline):
	model = Employee
	extra = 2

class OrganizationAdmin(admin.ModelAdmin):
	fieldsets = [
	    (None, {'fields': ['name']}),
	]
	inlines = [EmployeeInline]

admin.site.register(Organization, OrganizationAdmin)

