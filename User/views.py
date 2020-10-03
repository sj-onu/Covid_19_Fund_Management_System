from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import ProfileForm
from .models import Profile

from django.core.mail import send_mail
import random
import string


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


@login_required
def showProfile(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile
    }
    return render(request, 'User/viewProfile.html', context)


def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@login_required
def sendEmail(request):
    recipient_list = []
    subject = ''
    message = ''
    status = Profile.objects.get(user=request.user).status
    user_message = '' + status

    if request.method == 'POST':

        recipient_list.append(request.POST['recipient'])
        subject = request.POST['subject']

        code = id_generator()
        v_code = code
        request.session['v_code'] = code

        message += request.POST['body']
        message += '\n Activation code: ' + code

        status = send_mail(
            subject=subject,
            message=message,
            from_email='contact.formulabd71@gmail.com',
            recipient_list=recipient_list,
            fail_silently=True
        )

        if status == 1:

            user_message = 'Email sent successfully. Please enter the verification code.'
            context = {
                'message': user_message
            }

            return redirect('verification')
        else:
            user_message = 'Failed! Try again please!'

    context = {
        'message': user_message
    }
    return render(request, 'user/sendEmail.html', context)


@login_required
def verifyEmail(request):
    message = ''

    if request.method == "POST":
        code = request.POST['code']
        print(code, request.session['v_code'])
        message = 'Not matched!'

        if request.session['v_code'] == code:
            message = "Successful! Your account if activated now!"
            profile = Profile.objects.get(user=request.user)
            profile.status = "True"
            profile.save()
            context = {
                'message': message
            }
            return render(request, 'User/success.html', context)

    context = {
        'message': message
    }
    return render(request, 'User/emailVerificationcode.html', context)
