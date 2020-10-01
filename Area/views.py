from django.shortcuts import render
from .models import AreaClass
from .forms import AreaForm
from django.contrib.auth.decorators import login_required


def showArea(request):
    area = AreaClass.objects.all()
    context = {
        'all_area': area
    }
    return render(request, 'Area/showarea.html', context)
@login_required
def insertArea(request):

    message = ""
    form = AreaForm()

    if request.method == "POST":
        form = AreaForm(request.POST)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Member is inserted to DB. You can insert a new student now"
            form = AreaForm()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'Area/insertArea.html', context)