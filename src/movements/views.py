from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Movement
from django.contrib.auth.decorators import login_required
from companies.models import Company
# Create your views here.


@login_required
def index(request):
    userId = request.user.id
    movements = Movement.objects.filter(user__id=userId).order_by('-createdAt')
    balance = 0
    for movement in movements:
        balance += movement.amount
    context = {
        'movements': movements,
        'balance': balance
    }
    return render(request, 'index.html', context)


@login_required
def create(request):
    context = {'message': '', 'errors': '', 'companies': []}
    if request.method == "POST":
        try:
            newMovement = Movement()
            newMovement.amount = request.POST['amount']
            newMovement.partner = request.POST['partner']
            newMovement.invoiceLink = request.POST['invoiceLink']
            newMovement.user = request.user
            newMovement.movementDate = request.POST['movementDate']
            newMovement.save()
            context['message'] = 'Successfully created'
        except:
            context['errors'] = 'You provided wrong datatypes.'

    # provides a list of companies to choose from
    if request.method == 'GET':
        context['companies'] = Company.objects.all().filter(
            relatedToUser=request.user)
    return render(request, 'create.html', context)


@login_required
def delete(request):
    if request.method == "POST":
        id = request.POST['id'] or 0
        movement = Movement.objects.get(id=id)
        if movement.user == request.user:
            movement.delete()

    return HttpResponseRedirect(reverse('movements:movements'))


@login_required
def displayItem(request, id):
    if request.method == "POST":
        movementId = request.POST["movementId"]
        movement = Movement.objects.get(id=movementId)
        if movement and movement.user == request.user:
            movement.amount = request.POST['amount']
            movement.partner = request.POST['partner']
            movement.invoiceLink = request.POST['invoiceLink']
            movement.movementDate = request.POST['movementDate']
            movement.save()
        else:
            return render(request, 'item.html')

    companies = Company.objects.all().filter(
        relatedToUser=request.user)
    movement = Movement.objects.get(id=id)
    context = {
        'movement': movement,
        'companies': companies
    }
    if movement.user.id == request.user.id:
        return render(request, 'item.html', context)
    else:
        print("Should have need to authorize page.")
