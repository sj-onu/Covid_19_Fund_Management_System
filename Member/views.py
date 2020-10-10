from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from .forms import MemberForm
from .models import MemberClass , Order


# Create your views here.

def showMember(request):
    member = MemberClass.objects.all()

    if request.method == 'POST':
        member = MemberClass.objects.filter(name__icontains=request.POST['search'])

    user_count = User.objects.count()
    member_count = MemberClass.objects.count()

    context = {
        'all_member': member,
        'u_c': user_count,
        'm_c': member_count
    }
    return render(request, 'Member/showmember.html', context)


@login_required
def insertMember(request):
    message = ""
    form = MemberForm()

    if request.method == "POST":
        form = MemberForm(request.POST , request.FILES)
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
@login_required
def memberRequest(request):

    members = MemberClass.objects.all()

    try:
        members = MemberClass.objects.all()
        order_status = True
    except members.DoesNotExist:
        members = MemberClass(user=request.user)
        order_status = False

    context = {
        'members': members,
        'order_status': order_status,
    }

    return render(request, 'Member/memberRequest.html', context)

def showDetails(request, member_id):
    searched_member = MemberClass.objects.filter(id=member_id)  # many return

    if len(searched_member) == 0:
        does_exists = False
        context = {
            'does_exists': does_exists,
        }
    else:
        does_exists = True
        search = searched_member[0]
        context = {
            'does_exists': does_exists,
            'search': search
        }

    return render(request, 'Member/detail_member_view.html', context)
@login_required
def my_orders(request):

    orders = Order(user=request.user)

    try:
        orders = Order.objects.filter(user=request.user)
        order_status = True
    except orders.DoesNotExist:
        orders = Order(user=request.user)
        order_status = False

    context = {
        'orders': orders,
        'order_status': order_status

    }

    return render(request, 'Member/memberRequest.html', context)