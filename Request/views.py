from django.shortcuts import render
from .models import RequestClass
from .forms import RequestForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def showRequest(request):
    requests = RequestClass.objects.all()
    context = {
        'all_request': requests
    }
    return render(request, 'Request/showrequest.html', context)


@login_required
def insertRequest(request):

    message = ""
    form = RequestForm()

    if request.method == "POST":
        form = RequestForm(request.POST)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "You request is received.WE will inform you"
            form = RequestForm()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'Request/insertRequest.html', context)
