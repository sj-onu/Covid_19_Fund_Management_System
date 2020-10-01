from django.db import models
from Member.models import MemberClass
# Create your models here.
class DonorClass(models.Model):
    donor_name = models.ForeignKey(MemberClass, on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.donor_name.name

