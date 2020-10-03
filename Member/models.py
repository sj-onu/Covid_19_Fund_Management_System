from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MemberClass(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(blank=True)
    address = models.CharField(max_length=250)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=200)
    interest_in = models.CharField(max_length=300)
    image = models.ImageField(upload_to='MembersPic/images/', blank=True, default="MembersPic/images/default.jpg")

    def __str__(self):
        return self.name
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    member = models.ManyToManyField(MemberClass) # can be blank or null by default
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username