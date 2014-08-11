from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import RequestContext, loader
from compliance.models import Organization, Employee
#from ExcelParser import ExcelParser

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

def importExcel(request):
    c = RequestContext(request, {'other_context':'details here'})
    if request.method == 'POST': # If the form has been submitted...
        form = ImportExcelForm(request.POST,  request.FILES) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            excel_parser= ExcelParser()
            success, log  = excel_parser.read_excel(request.FILES['file'] )
            if success:
                return redirect(reverse('admin:index')) ## redirects to aliquot page ordered by the most recent
            else:
                errors = '* Problem with import * <br><br>log details below:<br>' + "<br>".join(log)
                c['errors'] = mark_safe(errors)
        else:
            c['errors'] = form.errors 
    else:
        form = ImportExcelForm() # An unbound form
    c['form'] = form
    return render_to_response('compliance/file_upload.html')