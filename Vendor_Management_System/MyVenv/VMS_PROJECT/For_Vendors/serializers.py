from rest_framework import serializers
from .models import Vendor_details , Purchase_Order
from datetime import date


class Vendor_detail_serializers(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor_details
        fields = ['id', 'name', 'contact_details', 'address', 'vendor_code']

class update_vendor_details(serializers.ModelSerializer):
    class Meta:
        model = Vendor_details
        fields=['name','contact_details','address']

        
class purchase_order_serializer(serializers.ModelSerializer):
        
    class Meta:
        model = Purchase_Order
        fields = ['id', 'po_number', 'vendor', 'order_date', 'delivery_date', 'items', 'quantity', 'status', 'issue_date']

    def validate_delivery_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Delivery Date cannot be in the past")
        return value
class Purchase_order_update_serializer(serializers.ModelSerializer):
    class Meta:
          model = Purchase_Order 
          fields = ['status','delivery_date','quality_rating'] 
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        
        if instance.status == 'completed':
            instance.quality_rating = validated_data.get('quality_rating', instance.quality_rating)
            if instance.quality_rating is None:
                raise serializers.ValidationError("Quality_Rating is required for completed status")
                
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.save()
        return instance
            

class Vendor_Performance_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor_details
        fields = ['id','name','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']
