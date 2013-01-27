from django.template import Context, loader
from companies.models import Company
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def index(request):
    if not request.user.is_authenticated():
        return render_to_response('companies/index-nonuser.html')
    
    company_list = Company.objects.all().order_by('name')
    return render_to_response('companies/index.html', {'company_list': company_list})

def detail(request, company_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
        
    c = get_object_or_404(Company, pk=company_id)
    return render_to_response('companies/detail.html', {'company': c})
    
def login_view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    
    return HttpResponseRedirect('/')    
    
def logout_view(request):
    logout(request)
    
    return HttpResponseRedirect('/')
