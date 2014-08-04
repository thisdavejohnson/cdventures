from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from compliance.models import Organization

def index(request):
    organization_list = Organization.objects.all()
    template = loader.get_template('compliance/index.html')
    context = RequestContext(request, {
	'organization_list': organization_list,
    })
    return HttpResponse(template.render(context))
