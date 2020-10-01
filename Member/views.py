from django.shortcuts import render
from .models import MemberClass
from .forms import MemberForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def showMember(request):
    member = MemberClass.objects.all()

    context = {
        'all_member': member
    }
    return render(request, 'Member/showmember.html', context)

@login_required
def insertMember(request):

    message = ""
    form = MemberForm()

    if request.method == "POST":
        form = MemberForm(request.POST)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Member is inserted to DB. You can insert a new student now"
            form = MemberForm()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'Member/insertMember.html', context)
