from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MemberClass(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(blank=True)
    address = models.CharField(max_length=250)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=200)
    STATUS_CHOICES = (
        ('Volunteer', 'Volunteer'),
        ('Donor', 'Donor'),
    )
    interest_in = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Null')
    image = models.ImageField(upload_to='MembersPic/images', blank=True, null=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    member = models.ForeignKey(MemberClass, on_delete=models.CASCADE, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed')
     )

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')