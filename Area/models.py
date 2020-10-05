from django.db import models
from Volunteer.models import VolunteerClass
# Create your models here.
class AreaClass(models.Model):
    area_image = models.ImageField(upload_to='AreaPic/images/', blank=True, default="AreaPic/images/default.jpg")
    volunteer_name = models.ForeignKey(VolunteerClass, on_delete=models.SET_NULL, blank=True, null=True)
    area_name = models.CharField(max_length=100)
    no_of_affected_family = models.IntegerField()
    condition = models.CharField(max_length=300 , default='poor')

    def __str__(self):
        return self.area_name
