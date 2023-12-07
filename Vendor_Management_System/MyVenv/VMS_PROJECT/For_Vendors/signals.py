from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchase_Order, Vendor_details, Performance_Model
from datetime import datetime


@receiver(post_save, sender=Purchase_Order)
def performance_metric_calculation(sender, instance, created, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        completed_orders_before_date = Purchase_Order.objects.filter(
            vendor=vendor,
            status='completed',
            delivery_date__lte=instance.delivery_date
        ).count()
        total_orders_completed = Purchase_Order.objects.filter(
            vendor=vendor,
            status='completed'
        ).count()
        on_time_delivery_rate = completed_orders_before_date / total_orders_completed if total_orders_completed > 0 else 0.0

                           # Quality_Rating_Average
        completed_orders_with_ratings =Purchase_Order.objects.filter(
            vendor=vendor, 
            status='completed',
            quality_rating__isnull=False)
        Quality_Ratings = completed_orders_with_ratings.values_list('quality_rating',flat=True)
        quality_rating_average = sum(Quality_Ratings)/len(Quality_Ratings)

                         # Average Response Time
        acknowledged_pos = Purchase_Order.objects.filter(
            vendor = vendor,
            status ="completed",
            acknowledgment_date__isnull = False
        )
        reponse_time = [(po.issue_date - po.acknowledgment_date ).days  for po in acknowledged_pos]
        average_response_time = sum(reponse_time)/len(reponse_time) if len(reponse_time) >0 else 0


                          # Fulfilemt Rate
        Completed_pos = Purchase_Order.objects.filter(vendor=vendor,status = "completed").count()
        total_pos = Purchase_Order.objects.filter(vendor=vendor).count()
        fulfilment_rate= Completed_pos/total_pos
        vendor_details = Vendor_details.objects.get(id=vendor.id)
        vendor_details.on_time_delivery_rate = on_time_delivery_rate
        vendor_details.quality_rating_avg = quality_rating_average
        vendor_details.average_response_time = average_response_time
        vendor_details.fulfillment_rate = fulfilment_rate
        vendor_details.save()

    