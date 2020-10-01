from django.db import models
from Member.models import MemberClass


# Create your models here.
class VolunteerClass(models.Model):
    volunteer_name = models.ForeignKey(MemberClass, on_delete=models.SET_NULL, blank=True, null=True)
    work_type = models.CharField(max_length=300)

    def __str__(self):
        return self.volunteer_name.name
