from django.shortcuts import render
from .models import DonationClass
from .forms import DonationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def showDonation(request):
    donation = DonationClass.objects.all()
    context = {
        'all_donation': donation
    }

    return render(request, 'Donation/showdonation.html', context)


@login_required
def insertDonation(request):

    message = ""
    form = DonationForm()

    if request.method == "POST":
        form = DonationForm(request.POST)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Member is inserted to DB. You can insert a new student now"
            form = DonationForm()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'Donation/insertDonation.html', context)