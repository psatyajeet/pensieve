from django.template import Context, loader
from companies.models import Company
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    company_list = Company.objects.all().order_by('name')
    return render_to_response('companies/index.html', {'company_list': company_list})

def detail(request, company_id):
    c = get_object_or_404(Company, pk=company_id)
    return render_to_response('companies/detail.html', {'company': c})