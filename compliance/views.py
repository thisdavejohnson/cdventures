from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import RequestContext, loader
from compliance.models import Organization

from django.shortcuts import render, get_object_or_404

def index(request):
    organization_list = Organization.objects.all()
    context = {'organization_list': organization_list}
    return render(request,'compliance/index.html', context)

def detail(request, name):
    organization = get_object_or_404(Organization, ok=name)
    return render(request, 'organization/detail.html', {'organization': organization})