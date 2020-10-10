from django.db import models
from Donor.models import DonorClass
# Create your models here.
class DonationClass(models.Model):
    donor_name = models.ForeignKey(DonorClass, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    DONATION_CHOICES = (
        ('Bkash', 'Bkash'),
        ('Rocket', 'Rocket'),
        ('Donate by person', 'Donate by person')
    )
    donation_options = models.CharField(max_length=50, choices=DONATION_CHOICES, default='Donate by person')
    have_donate_before = models.BooleanField(default=False)

    transaction_id = models.CharField(max_length=30, null =True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __int__(self):
        return self.donor_name
