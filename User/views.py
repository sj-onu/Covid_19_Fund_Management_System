from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .forms import ProfileForm
from .models import Profile


# Create your views here.
def user_registration(request):
    user_form = UserCreationForm()

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

    context = {
        'form': user_form
    }
    return render(request, 'User/registration.html', context)

@login_required
def showProfile(request):
    ProfileList = Profile.objects.all()
    context = {
        'profile': ProfileList
    }
    return render(request, 'User/viewProfile.html', context)


@login_required
def createProfile(request):
    message = ""
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            profiles = form.save(commit=False)

            profiles.user = request.user

            profiles.save()

            message = "Profile is inserted to DB. You can insert a new Profile now"
            form = ProfileForm()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'User/createProfile.html', context)
