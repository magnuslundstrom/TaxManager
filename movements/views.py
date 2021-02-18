from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Movement
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    userId = request.user.id
    movements = Movement.objects.filter(user__id=userId).order_by('-createdAt')

    context = {
        'movements': movements
    }
    return render(request, 'index.html', context)


@login_required
def create(request):
    context = {'message': '', 'errors': ''}
    if request.method == "POST":
        try:
            newMovement = Movement()
            newMovement.amount = request.POST['amount']
            newMovement.sender = request.POST['sender']
            newMovement.receiver = request.POST['receiver']
            newMovement.user = request.user
            newMovement.save()
            context['message'] = 'Successfully created'
        except:
            context['errors'] = 'You provided wrong datatypes. Please provide num - string - string'

    return render(request, 'create.html', context)


@login_required
def delete(request):
    if request.method == "POST":
        id = request.POST['id'] or 0
        movement = Movement.objects.get(id=id)
        if movement.user.id == request.user.id:
            movement.delete()

    return HttpResponseRedirect(reverse('movements:movements'))
