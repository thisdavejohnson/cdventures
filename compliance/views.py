from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import RequestContext, loader
from compliance.models import Organization, Employee

from django.shortcuts import render, get_object_or_404

def index(request):
    organization_list = Organization.objects.all()
    organization = Organization.objects.get(pk=1)

    employee_list = Employee.objects.filter(employer=organization)

    context = {'employee_list': employee_list}
    return render(request,'compliance/index.html', context)

def detail(request, org_id):
    organization = get_object_or_404(Organization, pk=org_id)
    return render(request, 'compliance/detail.html', {'organization': organization})
