from django.template import Context, loader, RequestContext
from companies.models import Company
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from companies.forms import UserCreateForm


def index(request):
    # If not authenticated, redirect to a nonuser home page.
    if not request.user.is_authenticated():
        return render_to_response('companies/index-nonuser.html')
        
    # If authenticated, show list of all companies
    company_list = Company.objects.all().order_by('name')
    return render_to_response('companies/index.html', {'company_list': company_list,         'user': request.user})

def detail(request, company_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
        
    c = get_object_or_404(Company, pk=company_id)
    return render_to_response('companies/detail.html', {'company': c})
    
def login_view(request):
    # If not authenticated, then redirect to a login page which then redirects back to         originally requested page
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    
    # If already authenticated, redirect to home page
    return HttpResponseRedirect('/')    
    
def logout_view(request):
    # Logout user and return to homepage
    logout(request)
    return HttpResponseRedirect('/')
    
def signup_view(request):
    if request.method =='POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
        return render_to_response('companies/index-nonuser.html') # Redirect after POST
    else:
        form = UserCreateForm() # An unbound form
        return render_to_response('registration/register.html', {
            'form': form, },context_instance=RequestContext(request))
    
    
    
