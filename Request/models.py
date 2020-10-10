from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RequestClass(models.Model):
    # person_name = models.CharField(max_length=150)
    # person_name = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , blank=True, null=True)
    person_name = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    mobile = models.IntegerField(blank=True, null=True)
    req_type = models.CharField(max_length=100)
    req_statement = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.user.username