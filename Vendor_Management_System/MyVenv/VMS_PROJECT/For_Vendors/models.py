from django.db import models
from django.utils import timezone
# Create your models here.
class Vendor_details(models.Model):
    name = models.CharField(max_length=30)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=5, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.name}'
    
class Purchase_Order(models.Model):
    
    status_choices = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancled', 'Canceled')
    )
    po_number = models.CharField(max_length=5,unique=True)
    vendor = models.ForeignKey(Vendor_details, on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now)####
    delivery_date=models.DateField()
    items = models.JSONField()###
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=status_choices, default='pending')#
    quality_rating = models.FloatField(null=True,blank=True)
    issue_date = models.DateField(default=timezone.now)
    acknowledgment_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f'{self.po_number}'
    
class Performance_Model(models.Model):
    vendor =models.ForeignKey(Vendor_details, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)


