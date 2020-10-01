from django.db import models

# Create your models here.
class RequestClass(models.Model):
    person_name = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    mobile = models.IntegerField(blank=True, null=True)
    req_type = models.CharField(max_length=100)
    req_statement = models.CharField(max_length=300)

    def __str__(self):
        return self.person_name