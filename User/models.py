from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    full_name = models.CharField(max_length=100, default='user.username')
    pro_pic = models.ImageField(upload_to='UsersPic/images/', blank=True, default="UsersPic/images/default.jpg")
    cv = models.FileField(upload_to='files/cv', blank=True, default="files/cv/default.png")

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, blank=True, null=True, default='False')

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    message = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='media/UsersPic/chat/images', blank=True, null=True)
    file = models.FileField(upload_to='media/UsersPic/chat/files', blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.sender.username + " : " + self.receiver.username