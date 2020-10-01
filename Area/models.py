from django.db import models
from Volunteer.models import VolunteerClass
# Create your models here.
class AreaClass(models.Model):
    volunteer_name = models.ForeignKey(VolunteerClass, on_delete=models.SET_NULL, blank=True, null=True)
    area_name = models.CharField(max_length=100)
    no_of_affected_family = models.IntegerField()

    def __str__(self):
        return self.area_name
