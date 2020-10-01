from django.db import models
# Create your models here.
class MemberClass(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(blank=True)
    address = models.CharField(max_length=250)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=200)
    interest_in = models.CharField(max_length=300)

    def __str__(self):
        return self.name
