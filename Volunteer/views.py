from django.shortcuts import render
from .models import VolunteerClass
from .forms import VolunteerForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def showVolunteer(request):
    volunteer = VolunteerClass.objects.all()

    context = {
        'all_volunteer': volunteer
    }
    return render(request, 'Volunteer/showvolunteer.html', context)


@login_required
def insertVolunteer(request):

    message = ""
    form = VolunteerForm()

    if request.method == "POST":
        form = VolunteerForm(request.POST)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Member is inserted to DB. You can insert a new student now"
            form = VolunteerForm()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'Volunteer/insertVolunteer.html', context)