from django.shortcuts import render
from .models import DonorClass
from .forms import DonorForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def showDonor(request):
    donor = DonorClass.objects.all()
    context = {
        'all_donor': donor
    }
    return render(request, 'Donor/showDonor.html', context)

@login_required
def insertDonor(request):

    message = ""
    form = DonorForm()

    if request.method == "POST":
        form = DonorForm(request.POST)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Member is inserted to DB. You can insert a new student now"
            form = DonorForm()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'Donor/insertDonor.html', context)