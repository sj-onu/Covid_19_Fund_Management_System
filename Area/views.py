from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import AreaForm
from .models import AreaClass


def showArea(request):
    area = AreaClass.objects.all()
    if request.method == 'POST':
        area = AreaClass.objects.filter(area_name__icontains=request.POST['search'])

    context = {
        'all_area': area,

    }
    return render(request, 'Area/showarea.html', context)
@login_required
def insertArea(request):

    message = ""
    form = AreaForm()

    if request.method == "POST":
        form = AreaForm(request.POST, request.FILES)
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
def showDetails(request, area_id):
    searched_area = AreaClass.objects.filter(id=area_id)  # many return

    if len(searched_area) == 0:
        does_exists = False
        context = {
            'does_exists': does_exists,
        }
    else:
        does_exists = True
        search = searched_area[0]
        context = {
            'does_exists': does_exists,
            'search': search
        }

    return render(request, 'Area/detail_area_view.html', context)