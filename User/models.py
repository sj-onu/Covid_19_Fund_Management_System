from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    contact_no = models.CharField(max_length=20, blank=True, null=True, default='False')
    mobile_no = models.CharField(max_length=20, blank=True, null=True, default='False')
    pro_pic = models.ImageField(upload_to='UsersPic/images/', blank=True, default="UsersPic/images/default.jpg")
    cv = models.FileField(upload_to='files/cv', blank=True, default="files/cv/default.png")

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, blank=True, null=True, default='False')

    def __str__(self):
        return self.user.username