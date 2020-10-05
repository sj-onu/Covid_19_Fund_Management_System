"""Covid_Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Member import views as memberviews
from Volunteer import views as volunteerviews
from Donor import views as donorviews
from Area import views as areaviews
from Donation import views as donationviews
from Request import views as requestviews
from User import views as userviews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('member/', memberviews.showMember, name='member'),
                  path('insertMember/', memberviews.insertMember, name='insertMember'),
                  path('member/<int:member_id>', memberviews.showDetails, name='detail_view'),

                  path('email/', userviews.sendEmail, name='email'),
                  path('verification/', userviews.verifyEmail, name='verification'),

                  path('volunteer/', volunteerviews.showVolunteer, name='volunteer'),
                  path('insertVolunteer/', volunteerviews.insertVolunteer, name='insertVolunteer'),

                  path('donor/', donorviews.showDonor, name='donor'),
                  path('insertDonor/', donorviews.insertDonor, name='insertDonor'),

                  path('donation/', donationviews.showDonation, name='donation'),
                  path('insertDonation/', donationviews.insertDonation, name='insertDonation'),

                  path('area/', areaviews.showArea, name='area'),
                  path('insertArea/', areaviews.insertArea, name='insertArea'),
                  path('area/<int:area_id>', areaviews.showDetails, name='detail_area_view'),

                  path('requests/', requestviews.showRequest, name='requests'),
                  path('insertRequest/', requestviews.insertRequest, name='insertRequest'),

                  path('registration/', userviews.user_registration, name='registration'),
                  path('accounts/', include('django.contrib.auth.urls')),

                  path('profile/', userviews.showProfile, name='profile'),
                  path('createProfile/', userviews.createProfile, name='createProfile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
