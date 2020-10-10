from django.shortcuts import render
from django.urls import reverse
from .models import DonationClass
from .forms import DonationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def showDonation(request):
    donation = DonationClass.objects.all()

    total = 0
    for amount in donation.all():
        total += amount.amount

    context = {
        'all_donation': donation,
        'total': total
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
            message = "Your donation is successful."
            form = DonationForm()
            context = {
                'message': message
            }
            return render(request, 'Donation/success.html', context)
    context = {
        'form': form
    }
    return render(request, 'Donation/insertDonation.html', context)