from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Company
from django.urls import reverse
# Create your views here.


def index(request):
    context = {}
    companies = Company.objects.filter(
        relatedToUser=request.user).order_by('name')
    context['companies'] = companies
    return render(request, 'companies.html', context)


@login_required
def create(request):
    context = {'errors': ''}
    if request.method == "POST":
        try:
            company = Company()
            company.name = request.POST['companyName']
            company.cvr = request.POST['cvr']
            company.eu = request.POST.get('tax', default=False)
            company.relatedToUser = request.user
            company.save()
            return HttpResponseRedirect(reverse('companies:index'))
        except:
            context['errors'] = 'Something went wrong, please try again!'

    return render(request, 'create-company.html', context)


@login_required
def delete(request):
    context = {'errors': ''}
    if request.method == "POST":
        companyId = request.POST['id']

        try:
            company = Company.objects.get(id=companyId)
            company.delete()
        except:
            context['error'] = 'Something went wrong'

    return render(request, 'companies.html', context)
